from flask import Flask, render_template, request
import json
from textblob import TextBlob

app = Flask(__name__)

# Load verses
with open("verse.json", "r", encoding="utf-8-sig") as f:
    verses_list = json.load(f)

# Build verse maps for quick lookup
verse_map = {}
verse_id_to_chapter_verse = {}
for v in verses_list:
    ch = v['chapter_number']
    vn = v['verse_number']
    vid = v['id']
    verse_map[(ch, vn)] = v
    verse_id_to_chapter_verse[vid] = (ch, vn)

# Load translations
with open("translation.json", "r", encoding="utf-8-sig") as f:
    translations_list = json.load(f)

translation_map = {}
for t in translations_list:
    vid = t['verse_id']
    if vid in verse_id_to_chapter_verse:
        ch, vn = verse_id_to_chapter_verse[vid]
        translation_map[(ch, vn)] = t['description']

# Helper functions
def get_verse_text(ch, vn):
    return verse_map.get((ch, vn), {}).get('text', '')

def get_transliteration(ch, vn):
    return verse_map.get((ch, vn), {}).get('transliteration', '')

def get_word_meanings(ch, vn):
    return verse_map.get((ch, vn), {}).get('word_meanings', '')

def get_translation(ch, vn):
    return translation_map.get((ch, vn), '')

# Search function
def search_verses(query):
    query_lower = query.lower()
    sentiment_query = TextBlob(query).sentiment.polarity
    direct_matches = []
    sentiment_matches = []

    for (ch, vn), v in verse_map.items():
        translation = get_translation(ch, vn).lower()
        word_meanings = get_word_meanings(ch, vn).lower()

        if query_lower in translation or query_lower in word_meanings:
            direct_matches.append((ch, vn))
        else:
            combined_text = translation + " " + word_meanings
            sentiment_score = TextBlob(combined_text).sentiment.polarity
            if abs(sentiment_score - sentiment_query) < 0.2:
                sentiment_matches.append((ch, vn))

    # ✅ Limit to max 3 results
    return direct_matches[:3], sentiment_matches[:3], sentiment_query


@app.route("/", methods=["GET", "POST"])
def index():
    user_query = ""
    direct_results = []
    sentiment_results = []
    sentiment_score = 0

    if request.method == "POST":
        user_query = request.form.get("query", "").strip()
        if user_query:
            direct_results, sentiment_results, sentiment_score = search_verses(user_query)

    def prepare_display(ch_vn_list):
        results = []
        for ch, vn in ch_vn_list:
            results.append({
                "chapter": ch,
                "verse": vn,
                "text": get_verse_text(ch, vn),
                "transliteration": get_transliteration(ch, vn),
                "word_meanings": get_word_meanings(ch, vn),
                "translation": get_translation(ch, vn),
                "sentiment": TextBlob(get_translation(ch, vn)).sentiment.polarity
            })
        return results

    direct_verses = prepare_display(direct_results)
    sentiment_verses = prepare_display(sentiment_results)

    return render_template("index.html",
                           user_query=user_query,
                           matched_verses=direct_verses,
                           sentiment_verses=sentiment_verses,
                           query_sentiment=sentiment_score)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
