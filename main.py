import calendar
from collections import Counter
from datetime import datetime, date
import os
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich import box
import typer

app = typer.Typer()
console = Console()

DEFAULT_LOG_FILE = Path.home() / ".streak_log.txt"
LOG_FILE = Path(os.getenv("STREAK_LOG_FILE", DEFAULT_LOG_FILE))


def load_timestamps() -> Counter:
    if not LOG_FILE.exists():
        return Counter()
    dates = Counter()
    with open(LOG_FILE) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = datetime.fromisoformat(line.strip()).date()
            dates[d] += 1
    return dates


def save_timestamp(date: datetime) -> None:
    with open(LOG_FILE, "a") as f:
        f.write(date.isoformat() + "\n")


def get_color_for_count(count: int) -> str:
    match count:
        case 0:
            return "#d7ffd7"
        case 1:
            return "#afff87"
        case 2:
            return "#5fd700"
        case 3:
            return "#00af00"
        case 4:
            return "#008700"
        case _:
            return "#005f00"


def _filter_dates_for_month(dates: Counter, year: int, month: int) -> set[date]:
    return {date for date in dates if date.year == year and date.month == month}


def longest_streak(dates: Counter, year: int, month: int) -> int:
    filtered = sorted(_filter_dates_for_month(dates, year, month))
    if not filtered:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(filtered)):
        if (filtered[i] - filtered[i - 1]).days == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak


@app.command()
def add():
    """Add today's timestamp to your streak log."""
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    save_timestamp(today)
    console.print(f"✅ Added {today.date()} to streak log.")


@app.command()
def show(month: str = typer.Option(None, help="Month to show in YYYYMM format")):
    """Show calendar view with streak highlights."""
    dates = load_timestamps()

    now = datetime.today()
    year, month_num = (now.year, now.month)
    if month:
        try:
            year, month_num = int(month[:4]), int(month[4:])
        except (ValueError, IndexError):
            console.print("❌ Invalid month format. Use YYYYMM.", style="bold red")
            raise typer.Exit()
        else:
            if month_num < 1 or month_num > 12:
                console.print("❌ Month must be between 01 and 12.", style="bold red")
                raise typer.Exit()

    cal = calendar.Calendar()
    table = Table(
        title=f"Coding Streak: {calendar.month_name[month_num]} {year}",
        box=box.ROUNDED,
        pad_edge=False,
        padding=(0, 0),
        show_lines=True,
    )
    for short_day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]:
        table.add_column(short_day)

    month_days = cal.monthdayscalendar(year, month_num)

    for week in month_days:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            else:
                date = datetime(year, month_num, day).date()
                if date in dates:
                    count = dates[date]
                    color = get_color_for_count(count)
                else:
                    color = "#999999"
                row.append(f"[on {color}] {day:^5} [/on {color}]")
        table.add_row(*row)

    console.print(table)
    streak = longest_streak(dates, year, month_num)
    days_str = "day" if streak == 1 else "days"
    console.print(
        f"Longest streak this month: [bold green]{streak} {days_str}[/bold green]"
    )


if __name__ == "__main__":
    app()
