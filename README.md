# Bhagavad Gita AI Search Web App

A Flask-based web application that enables users to **search Bhagavad Gita verses** by meaning, word, or emotion. It uses **keyword matching** and **sentiment analysis** to find relevant verses, and displays the verse text, transliteration, word meanings, and translations.

---

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Running the Application](#running-the-application)  
- [Project Structure](#project-structure)  
- [Data Files](#data-files)  
- [Advanced Features](#advanced-features)  
- [How It Works](#how-it-works)  
- [Future Enhancements](#future-enhancements)  
- [Contributing](#contributing)  
- [Contact](#contact)  

---

## Features

### Basic Features
- Search verses by keywords appearing in translation or word meanings.
- Semantic sentiment-based search to find emotionally relevant verses.
- Displays:
  - Verse text in Sanskrit
  - Transliteration
  - Word meanings
  - English translation
  - Sentiment polarity score for each verse

### Planned/Advanced Features (optional)
- **Verse of the Day:** Display a daily verse randomly or scheduled.
- **Favorite/Bookmark Verses:** Allow users to save favorite verses using browser localStorage or sessions.
- **Dark/Light Mode:** Toggle between dark and light UI themes with preference persistence.
- **Copy/Share Verse:** Buttons to copy verse text or share on WhatsApp/Twitter.
- **Download as PDF/Image:** Export verses as styled PDF documents or shareable quote images.
- **Chapter Summaries:** Display markdown-based summaries per chapter.
- **Progress Tracker:** Track chapters or verses read by the user.

---

## Installation

### Prerequisites

- Python 3.8 or above
- `pip` (Python package manager)

### Clone the repository

```bash
git clone https://github.com/rahulupadhyay22/gita-chatgpt.git
cd gita-chatgpt
```

### Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Running the Application
Start the Flask development server:
```bash
python app.py
```
By default, the app runs on http://localhost:5000

Open this URL in your browser to start searching Bhagavad Gita verses.

---

### Project Structure
```bash
gita-chatgpt/
│
├── app.py                  # Main Flask app code
├── verse.json              # Bhagavad Gita verses data (Sanskrit, transliteration, word meanings)
├── translation.json        # English translations of verses
├── summary.md              # Chapter summaries in markdown (for advanced feature)
├── templates/
│   └── index.html          # Main HTML template for search and display
├── static/
│   └── (css/js files)      # Optional static files for styling and scripts
├── requirements.txt        # Python dependencies (optional)
└── README.md               # This documentation file
```

---

### Data Files

- verse.json — Contains all the verses with:
- chapter_number
- verse_number
- id
- text (Sanskrit)
- transliteration
- word_meanings
- translation.json — Contains verse translations indexed by verse id.
- summary.md — Markdown file with chapter-wise summaries for future display.

Make sure these files are in the root directory or adjust paths accordingly in app.py

---

### How It Works (Overview)
1 Data Loading:
- The app loads all verses and translations into memory for quick access.

2 Search Logic:

- Takes user input query and converts it to lowercase.

- Finds verses where the query matches directly in translation or word meanings.

- Uses TextBlob sentiment analysis to find verses with a sentiment polarity close to that of the query for “semantic” matches.

- Limits results to a maximum of 3 direct and 3 sentiment matches for performance.

3 Rendering Results:

- Prepares display data including verse text, transliteration, word meanings, translations, and sentiment scores.

- Renders results in a user-friendly card layout in the browser.

---

### Future Enhancements
- Persistent user accounts with saved bookmarks and reading progress.

- AI-powered "Ask a Question" feature using Google PaLM or OpenAI GPT APIs.

- Mobile-friendly responsive design.

- Integration with social media for sharing favorite verses.

- Scheduled "Verse of the Day" email or notification.

---

### Contributing

Contributions are welcome! To contribute:

- Fork the repository.

- Create a new feature branch (git checkout -b feature-name).

- Commit your changes (git commit -m "Add new feature").

- Push to the branch (git push origin feature-name).

- Create a Pull Request describing your changes.

---

### Contact
Created and maintained by Rahul Upadhyay

GitHub: https://github.com/rahulupadhyay22

----
### License
This project is open source and available under the MIT License.


---

If you want, I can help you generate a `requirements.txt` or add a usage demo. Just ask!





