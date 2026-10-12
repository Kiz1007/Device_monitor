
print("SIMULATED DEVICE MONITORING SYSTEM")
print("----------------------------------")
print("[1] View Readings")
print("[2] Add Readings")
print("[3] Classify Readings")
print("[4] Generate Summary")
print("[5] Exit")

def view_readings(readings):
    print("CURRENT READINGS")
    print("----------------")
    
    if not readings:
        print("No readings available.")
    
    for i, in readings in enumerate(readings, start=1):
        print(f"Reading {i}: {readings} C")
    
    def add_reading(readings):
        new_reading = int(input("Enter new reading:"))
        readings.append(new_reading)
        print("Reading added successfully.")
        ValueError
    print("Invalid input. Enter a whole number only")
    
def classify_readings(readings):
    if readings < 30:
        return "NORMAL"
    elif readings <= 35:
        return "WARNING"
    else:
        return "CRITICAL"
    
def display_classifications(readings):
    print("CLASSIFIED READINGS")
    print("-------------------")
    if not readings:
       print("No Readings Available")

    for i, readings in enumerate(readings, start=1):
         status = classify_readings(readings)
print(f"Readings {int}: {classify_readings} C - {status}")

def generate_summary(readings):
    print("MONITORING SUMMARY")
    print("------------------")
    if not readings:
       print("No Rreadings Available")
    
    total = sum(readings)
    count = len(readings)
    average = total / count
    minimum = min(readings)
    maximum = max(readings)

    print(f"Number of readings : {count}")
    print(f"Total of readings  : {total}")
    print(f"Average temperature: {average:.2f} °C")
    print(f"Minimum temperature: {minimum} °C")
    print(f"Maximum temperature: {maximum} °C")

    NORMAL = sum(1 for r in readings if classify_readings(r) == "NORMAL")
    WARNING = sum(1 for r in readings if classify_readings(r) == "WARNING")
    CRITICAL = sum(1 for r in readings if classify_readings(r) == "CRITICAL")
    print()
    print(f"NORMAL   : {normal} ({normal / count * 100:.2f}%)")
print(f"WARNING  : {warning} ({warning / count * 100:.2f}%)")
print(f"CRITICAL : {critical} ({critical / count * 100:.2f}%)")
    
if critical > 0:
    overall_status = "ATTENTION REQUIRED"
elif warning > 0:
    ovearall_status = "MONITORING REQUIRED"
else:
    overall_status = "ALL SYSTEMS NORMAL"

print(f"OVERALL STATUS {overall_status}")

def main():
    readings = [28, 31, 35, 37, 29]
    
print()
classify_readings(readings)
    
Choice = input("ENTER CHOICE:").strip()

if choice == "1":
    view_readings(readings)
elif choice == "2":
    add_readings(readings)
elif choice == "3":
    display_classifications(readings)
elif choice == "4":
    generate_summary(readings)
elif choice =="5":
    print("Thank you for using the Device Monitoring System.")
    breakpoint
else:
    print("\nInvalid choice. Please select 1 to 5.")
    
if __name__ == "__main__":
    main()