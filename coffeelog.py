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