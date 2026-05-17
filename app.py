"""Study Buddy — a simple task list Flask app with JSON storage."""

import json
import os
from datetime import datetime, timezone

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

DATA_FILE = "tasks.json"
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


# ── JSON persistence ────────────────────────────────────────────────

def load_tasks() -> list[dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_tasks(tasks: list[dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as fh:
        json.dump(tasks, fh, indent=2, ensure_ascii=False)


# ── Helpers ─────────────────────────────────────────────────────────

def sorted_tasks(tasks: list[dict]) -> list[dict]:
    return sorted(tasks, key=lambda t: (PRIORITY_ORDER.get(t["priority"], 99), t["created_at"]))


def next_id(tasks: list[dict]) -> int:
    return max((t["id"] for t in tasks), default=0) + 1


# ── Routes ──────────────────────────────────────────────────────────

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=sorted_tasks(tasks))


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    priority = request.form.get("priority", "medium")

    if not title:
        return redirect(url_for("index"))

    tasks = load_tasks()
    tasks.append({
        "id": next_id(tasks),
        "title": title,
        "priority": priority,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id: int):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))


# ── Entrypoint ──────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", 5000)),
        debug=os.environ.get("DEBUG", "false").lower() == "true",
    )
