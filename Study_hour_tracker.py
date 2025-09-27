import pandas as pd
from pathlib import Path

# File path (replace with your own path if needed)
FILE_PATH = Path(r"C:\Users\pujak\Downloads\schedule.txt")

def append_study_time(file_path: Path):
    """Append a new study record to the file."""
    if not file_path.exists():
        print("File not found. Creating a new one...")
        file_path.touch()
    
    try:
        date = input("Enter Date (DD/MM/YYYY): ").strip()
        time = input("Enter study time (HH:MM): ").strip()

        with open(file_path, "a") as f:
            f.write(f"\n{date} - {time}")

        print(" Study time appended successfully!")

    except Exception as e:
        print(" Could not append:", e)


def calculate_total_hours(file_path: Path):
    """Read study records and calculate total hours studied."""
    times = []

    with open(file_path, "r") as f:
        for line in f:
            if "-" in line:
                time_str = line.split("-")[1].strip() + ":00"
                times.append(time_str)

    # Convert to timedelta
    time_delta = pd.to_timedelta(times, errors="coerce")

    print("\n All study sessions:")
    print(time_delta)

    total_hours = round(time_delta.sum().total_seconds() / 3600, 2)
    print(f"\n Total study time = {total_hours} hours")


if __name__ == "__main__":
    append_study_time(FILE_PATH)
    calculate_total_hours(FILE_PATH)

