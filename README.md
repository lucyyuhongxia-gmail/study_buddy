# Study Buddy

A lightweight task manager web app built with Flask. Add, sort, and delete study tasks — no database required.

## Features

- Add tasks with a title and priority (High / Medium / Low)
- Tasks automatically sorted by priority on the page
- Delete tasks with one click
- Data persisted in a local JSON file (`tasks.json`)
- Clean black & white responsive design
- No database setup needed — runs out of the box

## Screenshot

```
┌──────────────────────────────────────────┐
│  Study Buddy                             │
│  Stay on top of your work. Add a task.   │
│                                          │
│  [________________________] [High ▾] [Add Task]
│                                          │
│  HIGH   Review Chapter 4            ✕    │
│  MEDIUM Do problem set              ✕    │
│  LOW    Organize notes              ✕    │
└──────────────────────────────────────────┘
```

## Tech Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5, CSS3, Jinja2 templates
- **Storage**: JSON file

## Project Structure

```
study_buddy/
├── app.py              # Flask application (routes & JSON storage)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main page template
├── static/
│   └── style.css       # Stylesheet
└── tasks.json          # Task data (auto-generated on first run)
```

## Getting Started

### Prerequisites

- Python 3.8 or later

### Installation

```bash
# Clone the repository
git clone https://github.com/lucyyuhongxia-gmail/study_buddy.git
cd study_buddy

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

Open your browser and visit **http://127.0.0.1:5000**.

## Usage

1. Type a task title (e.g. "Review Chapter 4")
2. Select a priority from the dropdown
3. Click **Add Task**
4. Tasks appear sorted: High → Medium → Low
5. Click the ✕ button to delete a task

All tasks are saved to `tasks.json` automatically. The file is created on first run.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Render the homepage with sorted task list |
| POST | `/add` | Add a new task (form fields: `title`, `priority`) |
| GET | `/delete/<id>` | Delete a task by its ID |

## License

This project is for educational purposes.
