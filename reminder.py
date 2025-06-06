import time

# Danh sách thuốc và thời gian uống (giây)
med_schedule = [
    {"name": "Paracetamol", "time": 3},
    {"name": "Vitamin C", "time": 6},
    {"name": "Amoxicillin", "time": 9}
]

print("🔔 Medicine Reminder Started!\n")

for med in med_schedule:
    time.sleep(med["time"])  # đợi số giây tương ứng
    print(f"💊 It's time to take: {med['name']}")
