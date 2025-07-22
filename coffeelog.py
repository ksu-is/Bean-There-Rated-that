from datetime import datetime  # ← make sure this is at the top of the file

def log_coffee():
    name = input("Coffee name: ")
    location = input("Where did you buy it?: ")
    rating = input("Rate it (1–10): ")
    notes = input("Optional notes: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("coffee_log.txt", "a") as file:
        file.write(f"{timestamp} | {name} | {location} | {rating} | {notes}\n")
    print("Coffee logged!")
