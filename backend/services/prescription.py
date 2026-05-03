from collections import defaultdict
from backend.utils.generate_schedule import generate_exact_times, datetime_to_slot
from backend.utils.constants import SLOT_TIME_RANGES

def create_prescription(drug_name: str, frequency: str, duration: int, start_hour: int) -> dict:
    daily_schedule = generate_exact_times(frequency, start_hour, duration)
    
    full_schedule = []
    for dt in daily_schedule:
          full_schedule.append({
            "date": dt.strftime("%Y-%m-%d"),
            "time": dt.strftime("%H:%M:%S"),
            "slot": datetime_to_slot(dt),
            "slot_range": SLOT_TIME_RANGES[datetime_to_slot(dt)]
          })

    return {
        "drug_name": drug_name,
        "frequency": frequency.upper(),
        "duration": duration,
        "start_hour": start_hour,
        "full_schedule": full_schedule 
    }


def create_multi_drug_schedule(drugs: list):
    combined = []

    for drug in drugs:
        times = generate_exact_times(drug.frequency, drug.start_hour, drug.duration)

        for dt in times:
            combined.append({
                "drug": drug.drug_name,
                "datetime": dt
            })

    #  Sort by datetime
    combined.sort(key=lambda x: x["datetime"])

    #  Group by exact datetime
    grouped = defaultdict(list)

    for entry in combined:
        key = entry["datetime"]
        grouped[key].append(entry["drug"])

    #  Format final output
    final_schedule = []
    for dt, drugs_at_time in grouped.items():
        final_schedule.append({
            "date": dt.strftime("%Y-%m-%d"),
            "time": dt.strftime("%H:%M"),
            "slot": datetime_to_slot(dt),
            "slot_range": SLOT_TIME_RANGES[datetime_to_slot(dt)],
            "drugs": drugs_at_time
        })

    return sorted(final_schedule, key=lambda x: (x["date"], x["time"]))