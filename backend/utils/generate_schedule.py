from datetime import datetime, timedelta
from backend.utils.constants import SLOT_TIME_RANGES, FREQUENCY_INTERVALS

def generate_schedule(frequency: str) -> list:
    frequencies = {
        "OD": [1],
        "BD": [1, 5],
        "TDS": [1, 3, 5],
        "QID": [1, 3, 4, 6],

    }

    if frequency not in frequencies:
        raise ValueError(f"Unsupported frequency: {frequency}")

    return frequencies[frequency]



def datetime_to_slot(dt: datetime):
    hour = dt.hour
    if 5 < hour <= 9:
        return 1
    elif 9 < hour <= 12:
        return 2
    elif 12 < hour <= 15:
        return 3
    elif 15 < hour <= 18:
        return 4
    elif 18 < hour <= 21:
        return 5
    else:
        return 6  # 21:00–06:00 treated as late night




def generate_exact_times(frequency: str, start_hour: int, days: int):
    frequency = frequency.upper()

    if frequency not in FREQUENCY_INTERVALS:
        raise ValueError(f"Unsupported frequency: {frequency}")

    interval = FREQUENCY_INTERVALS[frequency]

    # Start from today at given hour
    start_time = datetime.now().replace(
        hour=start_hour, minute=0, second=0, microsecond=0
    )

    schedule = []
    total_doses = int((24 / interval) * days)

    current_time = start_time

    for dose in range(total_doses):
        schedule.append(current_time)
        current_time += timedelta(hours=interval)

    return schedule