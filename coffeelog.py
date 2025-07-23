from datetime import datetime

def show_menu():
    print("\nBean-There-Rated-That")
    print("1. Log a new coffee")
    print("2. View coffee log")
    print("3. Exit")
    print("4. View only high-rated coffees (8–10)")
    print("5. Show total number of coffees logged")
    print("6. Clear all coffee logs")  # NEW

def log_coffee():
    name = input("Coffee name: ")
    coffee_type = input("Coffee type (e.g., iced, latte, espresso): ")
    location = input("Where did you buy it?: ")
    rating = input("Rate it (1–10): ")
    while not rating.isdigit() or not (1 <= int(rating) <= 10):
        print("Please enter a valid number from 1 to 10.")
        rating = input("Rate it (1–10): ")
    notes = input("Optional notes: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("coffee_log.txt", "a") as file:
        file.write(f"{timestamp} | {name} | {coffee_type} | {location} | {rating} | {notes}\n")
    print("Coffee logged!")

    def view_log():
    try:
        with open("coffee_log.txt", "r") as file:
            print("\nTimestamp | Name | Type | Location | Rating | Notes")
            print("-" * 80)
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No coffee log found.")

def filter_high_rated():  
    try:
        with open("coffee_log.txt", "r") as file:
            print("\nHigh-Rated Coffees (8–10):")
            print("-" * 80)
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) >= 6 and parts[4].isdigit() and int(parts[4]) >= 8:
                    print(line.strip())
    except FileNotFoundError:
        print("No coffee log found.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1–4): ")
        if choice == "1":
            log_coffee()
        elif choice == "2":
            view_log()
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            filter_high_rated()  
        else:
            print("Invalid choice. Try again.")
        elif choice == "5":
        show_count()
        elif choice == "6":
        confirm = input("Are you sure you want to delete all logs? (y/n): ")
        if confirm.lower() == "y":
                with open("coffee_log.txt", "w") as file:
                    file.write("")  # Clears the file
                print("Coffee log cleared.")
        else:
                print("Cancelled. Coffee log not cleared.")

if __name__ == "__main__":
    main()

def show_count():
    try:
        with open("coffee_log.txt", "r") as file:
            lines = file.readlines()
            print(f"\nTotal coffees logged: {len(lines)}")
    except FileNotFoundError:
        print("No coffee log found.")
