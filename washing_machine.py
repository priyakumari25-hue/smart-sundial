
import time

print("Project Name: Washing Machine")
print("Made by: Priya Kumari")
print("-" * 40)
print("    WELCOME TO WASHING MACHINE")
print("-" * 40)


class WashingMachine:

    def __init__(self):
        self.power = False
        self.weight = 0
        self.water_level = "Not Selected"
        self.program = "Not Selected"
        self.duration = 0
        self.water = False
        self.detergent = False
        self.stage = "Standby"

    def run_timer(self, seconds):
        for remaining in range(seconds, 0, -1):
            minutes = remaining // 60
            secs = remaining % 60

            print(
                f"Time Remaining: {minutes:02d}:{secs:02d}",
                end="\r",
                flush=True
            )
            time.sleep(1)

        print("Time Remaining: 00:00")

    def power_on(self):
        self.power = True
        self.stage = "Ready"
        print("\nMachine is now ON!")
        print("Starting Time:", time.strftime("%I:%M:%S %p"))

    def power_off(self):
        self.power = False
        self.stage = "Standby"
        print("\nMachine is now OFF!")

    def select_weight(self):
        while True:
            try:
                weight = float(input("\nEnter clothes weight (1-7 kg): "))

                if 1 <= weight <= 7:
                    self.weight = weight

                    if weight <= 2:
                        self.water_level = "Low"
                    elif weight <= 4:
                        self.water_level = "Medium"
                    else:
                        self.water_level = "High"

                    print("Water Level:", self.water_level)
                    break
                else:
                    print("Enter weight between 1 and 7 kg.")

            except ValueError:
                print("Please enter a valid number.")

    def select_program(self):
        print("\n1. Quick Wash - 1 minutes")
        print("2. Normal Wash - 3 minutes")
        print("3. Heavy Wash - 4 minutes")
        print("4. Soft Wash - 2 minutes")

        programs = {
            "1": ("Quick Wash", 1),
            "2": ("Normal Wash", 3),
            "3": ("Heavy Wash", 4),
            "4": ("Soft Wash", 2)
        }

        while True:
            choice = input("Select wash program: ").strip()

            if choice in programs:
                self.program, self.duration = programs[choice]
                print("Selected Program:", self.program)
                print("Wash Time:", self.duration, "minutes")
                break
            else:
                print("Please select 1, 2, 3 or 4.")

    def check_water(self):
        while True:
            choice = input(
                "\nIs water available? (yes/no): "
            ).lower().strip()

            if choice == "yes":
                self.water = True
                print("Water supply is available.")
                break
            elif choice == "no":
                print("Please arrange water first.")
            else:
                print("Enter yes or no.")

    def add_detergent(self):
        while True:
            choice = input(
                "Have you added detergent? (yes/no): "
            ).lower().strip()

            if choice == "yes":
                self.detergent = True
                print("Detergent check complete.")
                break
            elif choice == "no":
                print("Please add detergent first.")
            else:
                print("Enter yes or no.")

    def close_lid(self):
        while True:
            choice = input(
                "Is the machine lid closed? (yes/no): "
            ).lower().strip()

            if choice == "yes":
                print("Lid is closed.")
                return True
            elif choice == "no":
                print("Please close the lid.")
            else:
                print("Enter yes or no.")

    def start_wash(self):
        if not self.power:
            print("Machine is OFF!")
            return False

        if not self.water or not self.detergent:
            print("Please check water and detergent.")
            return False

        if not self.close_lid():
            return False

        total_seconds = self.duration * 60
        start_time = time.strftime("%I:%M:%S %p")

        print("\nWASHING STARTED!")
        print("Program:", self.program)
        print("Total Wash Time:", self.duration, "minutes")
        print("Starting Time:", start_time)

        current_stage = ""

        for remaining in range(total_seconds, 0, -1):
            elapsed = total_seconds - remaining
            progress = elapsed / total_seconds

            if progress < 0.10:
                stage = "Filling Water"
                message = "Water is filling into the drum."
            elif progress < 0.60:
                stage = "Washing Clothes"
                message = "Washing clothes..."
            elif progress < 0.80:
                stage = "Rinsing Clothes"
                message = "Rinsing clothes with clean water..."
            else:
                stage = "Draining Water"
                message = "Draining dirty water..."

            if stage != current_stage:
                current_stage = stage
                self.stage = stage
                print("\n" + message)

            minutes = remaining // 60
            seconds = remaining % 60

            print(
                f"Time Remaining: {minutes:02d}:{seconds:02d}",
                end="\r",
                flush=True
            )

            time.sleep(1)

        print("Time Remaining: 00:00")

        self.stage = "Wash Complete"
        print("\nWASHING COMPLETED!")
        print("Starting Time:", start_time)
        print("Completed Time:", time.strftime("%I:%M:%S %p"))

        return True

    def spin_dry(self):
        if not self.power:
            print("Machine is OFF!")
            return False

        if not self.close_lid():
            return False

        while True:
            try:
                duration = int(
                    input("Enter spin-dry time (1-10 minutes): ")
                )

                if 1 <= duration <= 10:
                    break
                else:
                    print("Enter time between 1 and 10 minutes.")

            except ValueError:
                print("Enter a valid number.")

        start_time = time.strftime("%I:%M:%S %p")

        self.stage = "Spinning Clothes"

        print("\nSPIN DRY STARTED!")
        print("Drying Time:", duration, "minutes")
        print("Starting Time:", start_time)

        self.run_timer(duration * 60)

        self.stage = "Drying Complete"

        print("\nRemoving extra water from clothes...")
        print("SPIN DRY COMPLETED!")
        print("Starting Time:", start_time)
        print("Completed Time:", time.strftime("%I:%M:%S %p"))
        print("Clothes may still be slightly damp.")

        return True

    def show_status(self):
        print("\n--------- MACHINE STATUS ---------")
        print("Power:", "ON" if self.power else "OFF")
        print("Weight:", self.weight, "kg")
        print("Water Level:", self.water_level)
        print("Wash Program:", self.program)
        print("Wash Duration:", self.duration, "minutes")
        print(
            "Water Supply:",
            "Available" if self.water else "Unavailable"
        )
        print(
            "Detergent:",
            "Added" if self.detergent else "Not Added"
        )
        print("Current Stage:", self.stage)
        print("Current Time:", time.strftime("%I:%M:%S %p"))
        print("----------------------------------")


machine = WashingMachine()

while True:
    choice = input(
        "\nDo you want to turn ON the machine? (yes/no): "
    ).lower().strip()

    if choice == "yes":
        machine.power_on()
        break
    elif choice == "no":
        print("Thank you for using Washing Machine!")
        raise SystemExit
    else:
        print("Please enter yes or no.")


while machine.power:
    machine.select_weight()
    machine.select_program()
    machine.check_water()
    machine.add_detergent()

    wash_success = machine.start_wash()

    if not wash_success:
        print("Washing could not be completed.")
        machine.power_off()
        break

    dry_success = machine.spin_dry()

    if not dry_success:
        print("Spin drying could not be completed.")
        machine.power_off()
        break

    machine.show_status()

    choice = input(
        "\nDo you want to wash more clothes? (yes/no): "
    ).lower().strip()

    if choice == "yes":
        machine.weight = 0
        machine.water_level = "Not Selected"
        machine.program = "Not Selected"
        machine.duration = 0
        machine.water = False
        machine.detergent = False
        machine.stage = "Ready"

        print("\nReady for the next load!")

    elif choice == "no":
        machine.power_off()
        print("\nThank you for using Smart Washing Machine!")
        print("Have a nice day!")
        break

    else:
        print("Invalid choice. Machine will now turn OFF.")
        machine.power_off()
        print("Thank you for using Washing Machine!")
        break
