from datetime import timedelta, datetime

log_file = "streak_log.txt"
today = datetime.now()
streak_days = [today.replace(hour=0, minute=0, second=0, microsecond=0)]
for i in range(1, 50):
    day = today.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=i)
    streak_days.append(day)

with open(log_file, "w") as f:
    for dt in sorted(streak_days):
        f.write(dt.isoformat() + "\n")
