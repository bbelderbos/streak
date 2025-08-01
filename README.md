# 🟩 streak — Simple CLI Streak Tracker

Track your daily coding (or any habit) streak using a terminal-based calendar.

Powered by [`typer`](https://typer.tiangolo.com/) and [`rich`](https://rich.readthedocs.io/), uses a simple (configurable) text file for tracking.

---

## 🚀 Features

- ✅ Log daily activity with one command
- ✅ View your streak as a calendar with heatmap-style colors
- ✅ Background cell coloring to visualize frequency
- ✅ Track current streak for any given month
- ✅ Uses only standard library + Typer + Rich

---

## 📦 Setup

```
git clone git@github.com:bbelderbos/streak.git
cd streak

uv sync

# export STREAK_LOG_FILE=...
# defaults to ~/.streak_log.txt

uv run main.py add        # logs today's activity
uv run main.py show       # shows current month
uv run main.py show --month 202508  # show any month (YYYYMM)
```

Consistency is king! Keep your streak going! 💪 📈
