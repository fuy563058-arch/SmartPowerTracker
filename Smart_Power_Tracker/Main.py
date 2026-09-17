from Appliance import ApplianceManager
from Calculations import Calculations
from FileManager import FileManager
from Suggestions import Suggestions


def get_positive_number(prompt):
    #Keeps asking until a valid, non-negative number is entered.
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a value of 0 or more.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_full_result(appliance, calc, suggest):
    #Prints one appliance's full results and its energy-saving suggestion.
    result = calc.calculate_all(appliance["wattage"], appliance["hours"])
    print("\n===== SMART POWER TRACKER =====")
    print(f"Appliance: {appliance['name']}")
    print(f"Power: {appliance['wattage']} watts")
    print(f"Usage: {appliance['hours']} hours/day")
    print(f"\nEstimated Usage: {result['daily_kwh']:.1f} kWh/day")
    print(f"Estimated Monthly Usage: {result['monthly_kwh']:.0f} kWh")
    print(f"Estimated Monthly Cost: P{result['monthly_cost']:,.0f}")
    print(f"\nSuggestion: {suggest.energy_suggestion(appliance, calc)}")


def show_menu():
    #Displays the main menu options.
    print("\n===== SMART POWER CONSUMPTION TRACKER =====")
    print("1. Add appliance")
    print("2. View appliances")
    print("3. Search appliance")
    print("4. Delete appliance")
    print("5. Exit")


def main_menu():
    #Controls the main menu and the overall program flow.
    calc = Calculations()
    suggest = Suggestions()
    file_manager = FileManager()

    appliance_manager = ApplianceManager(file_manager.load_data())

    while True:
        show_menu()
        choice = input("Select an operation (1-5): ").strip()

        if choice == "1":
            name = input("Appliance name: ").strip()
            wattage = get_positive_number("Enter wattage: ")
            hours = get_positive_number("Enter hours used per day: ")
            appliance = appliance_manager.add_appliance(name, wattage, hours)
            print_full_result(appliance, calc, suggest)
            file_manager.save_data(appliance_manager.view_appliances())
            print(f"\n'{name}' was added and saved.")

        elif choice == "2":
            appliances = appliance_manager.view_appliances()
            if not appliances:
                print("No appliances recorded yet.")
                continue
            for appliance in appliances:
                print_full_result(appliance, calc, suggest)

        elif choice == "3":
            appliances = appliance_manager.view_appliances()
            if not appliances:
                print("No appliances recorded yet.")
                continue

            keyword = input("Enter an appliance name to search: ").strip()
            if not keyword:
                print("Please enter something to search for.")
                continue

            matches = appliance_manager.search_appliance(keyword)
            if not matches:
                print(f"No appliance found matching '{keyword}'.")
                continue

            print(f"\nFound {len(matches)} matching appliance(s):")
            for index, appliance in matches:
                print_full_result(appliance, calc, suggest)

        elif choice == "4":
            appliances = appliance_manager.view_appliances()
            if not appliances:
                print("No appliances recorded yet.")
                continue

            print("\nSelect an appliance to delete:")
            for i, appliance in enumerate(appliances, start=1):
                print(f"{i}. {appliance['name']}")

            selection = input("Enter the number to delete (or 0 to cancel): ").strip()
            if selection == "0":
                print("Delete cancelled.")
                continue

            try:
                index = int(selection) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            removed = appliance_manager.delete_appliance(index)
            if removed is None:
                print("Invalid selection. No appliance was deleted.")
            else:
                file_manager.save_data(appliance_manager.view_appliances())
                print(f"'{removed['name']}' was deleted and the records were saved.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main_menu()