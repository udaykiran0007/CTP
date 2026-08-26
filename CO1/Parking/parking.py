from datetime import datetime
import math

class ParkingLot:
    def __init__(self, total_slots=100, rate_per_hour=20):
        self.total_slots = total_slots
        self.rate = rate_per_hour
        self.slots = {}          # slot_number : vehicle_number
        self.entry_time = {}     # vehicle_number : entry time

    # 1. Show available slots
    def available_slots(self):
        return self.total_slots - len(self.slots)

    # 2. Check if parking is full
    def is_full(self):
        return len(self.slots) == self.total_slots

    # 3. Allocate slot
    def park_vehicle(self, vehicle_no):
        if self.is_full():
            print("Parking Area is FULL!")
            return

        for slot in range(1, self.total_slots + 1):
            if slot not in self.slots:
                self.slots[slot] = vehicle_no
                self.entry_time[vehicle_no] = datetime.now()
                print(f"Vehicle {vehicle_no} parked at Slot {slot}")
                return slot

    # 4. Release slot and calculate bill
    def remove_vehicle(self, vehicle_no):
        slot = None

        for s, v in self.slots.items():
            if v == vehicle_no:
                slot = s
                break

        if slot is None:
            print("Vehicle not found!")
            return

        exit_time = datetime.now()
        duration = exit_time - self.entry_time[vehicle_no]

        hours = math.ceil(duration.total_seconds() / 3600)
        charge = hours * self.rate

        del self.slots[slot]
        del self.entry_time[vehicle_no]

        print(f"Vehicle {vehicle_no} left Slot {slot}")
        print(f"Parking Time : {hours} hour(s)")
        print(f"Total Charge : ₹{charge}")

    # 5. Display parking status
    def status(self):
        print("\n------ Parking Status ------")
        print(f"Total Slots     : {self.total_slots}")
        print(f"Occupied Slots  : {len(self.slots)}")
        print(f"Available Slots : {self.available_slots()}")

        if self.is_full():
            print("Status : FULL")
        else:
            print("Status : Available")

        print("----------------------------")


# ------------------ Main Program ------------------

parking = ParkingLot()

while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Check Availability")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vehicle = input("Enter Vehicle Number: ")
        parking.park_vehicle(vehicle)

    elif choice == "2":
        vehicle = input("Enter Vehicle Number: ")
        parking.remove_vehicle(vehicle)

    elif choice == "3":
        parking.status()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")