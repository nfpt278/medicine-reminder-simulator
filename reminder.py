import time
from datetime import datetime

# Danh sách thuốc và giờ uống thuốc (định dạng HH:MM)
med_schedule = [
    {"name": "Paracetamol", "time": "08:00"},
    {"name": "Vitamin C", "time": "14:00"},
    {"name": "Amoxicillin", "time": "20:00"}
]

reminded = set()

print("🔔 Real-Time Medicine Reminder Started!\n")
print("⏳ Waiting for the scheduled medicine times...")

while True:
    now = datetime.now().strftime("%H:%M")

    for med in med_schedule:
        if med["time"] == now and med["name"] not in reminded:
            print(f"💊 {now} → It's time to take: {med['name']}")
            reminded.add(med["name"])

    time.sleep(30)
