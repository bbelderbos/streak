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

Green cells == building up the streak:

<img width="649" height="457" alt="Screenshot 2025-08-01 at 20 14 20" src="https://github.com/user-attachments/assets/2d313c63-178b-4eab-b25e-ef572089fcb0" />

More of same day logged = greener cell:

<img width="655" height="459" alt="Screenshot 2025-08-01 at 20 14 30" src="https://github.com/user-attachments/assets/66a30d00-44e2-4360-8897-83236b869e58" />

Calculates longest streak for month:

<img width="644" height="401" alt="Screenshot 2025-08-01 at 20 14 38" src="https://github.com/user-attachments/assets/67789dc3-b741-47f2-8a9a-76315f938751" />

Check a previous month:

<img width="646" height="401" alt="Screenshot 2025-08-01 at 20 18 13" src="https://github.com/user-attachments/assets/d400f014-5bc2-4e28-959b-276bcf2a593c" />

---

Consistency is king! Keep your streak going! 💪 📈
