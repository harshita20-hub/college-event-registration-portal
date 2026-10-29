
"""College Event Registration Portal - standard library project."""

import json
from pathlib import Path
from uuid import uuid4

DATA_FILE = Path(__file__).with_name("registrations.json")

EVENTS = [
    {"id": "E101", "name": "Tech Fest", "category": "Technical", "date": "20-11-2026", "venue": "Main Auditorium", "capacity": 50},
    {"id": "E102", "name": "Cultural Night", "category": "Cultural", "date": "25-11-2026", "venue": "College Ground", "capacity": 100},
    {"id": "E103", "name": "Sports Meet", "category": "Sports", "date": "30-11-2026", "venue": "Sports Complex", "capacity": 75},
    {"id": "E104", "name": "Photography Workshop", "category": "Workshop", "date": "02-12-2026", "venue": "Seminar Hall", "capacity": 30},
]


def load_registrations():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open(encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        print("Warning: Registration data could not be read.")
        return []


def save_registrations(registrations):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(registrations, file, indent=2)


def event_by_id(event_id):
    return next(
        (event for event in EVENTS if event["id"] == event_id.upper()),
        None
    )


def seats_left(event, registrations):
    booked = sum(
        item["event_id"] == event["id"] for item in registrations
    )
    return max(0, event["capacity"] - booked)


def show_events(registrations, category=None):
    matches = [
        event for event in EVENTS
        if category is None
        or event["category"].casefold() == category.casefold()
    ]

    if not matches:
        print("No events found in that category.")
        return

    print("\nEVENTS")
    print("-" * 72)

    for event in matches:
        print(f"{event['id']} | {event['name']} ({event['category']})")
        print(f"Date: {event['date']} | Venue: {event['venue']}")
        print(
            f"Seats available: "
            f"{seats_left(event, registrations)}/{event['capacity']}"
        )
        print("-" * 72)


def read_student():
    details = {
        "name": input("Student name: ").strip(),
        "roll": input("Roll/registration number: ").strip(),
        "email": input("Email address: ").strip(),
        "department": input("Department/class: ").strip(),
    }

    if not all(details.values()):
        print("All student fields are required.")
        return None

    if (
        "@" not in details["email"]
        or "." not in details["email"].split("@")[-1]
    ):
        print("Please enter a valid email address.")
        return None

    return details


def register(registrations):
    show_events(registrations)

    event_id = input("Event ID: ").strip()
    event = event_by_id(event_id)

    if event is None:
        print("Event ID not found.")
        return

    if seats_left(event, registrations) == 0:
        print("This event is full.")
        return

    student = read_student()

    if student is None:
        return

    already_registered = any(
        r["roll"].casefold() == student["roll"].casefold()
        and r["event_id"] == event["id"]
        for r in registrations
    )

    if already_registered:
        print("This student is already registered for that event.")
        return

    record = {
        **student,
        "event_id": event["id"],
        "event_name": event["name"],
        "registration_id": uuid4().hex[:8].upper(),
    }

    registrations.append(record)

    try:
        save_registrations(registrations)
    except OSError as error:
        registrations.remove(record)
        print(f"Could not save registration: {error}")
        return

    print(
        f"\nRegistration successful! "
        f"Your ID is {record['registration_id']}."
    )
    print(
        f"Student: {student['name']} | Event: {event['name']} | "
        f"Seats left: {seats_left(event, registrations)}"
    )


def show_registrations(registrations):
    if not registrations:
        print("No registrations found.")
        return

    print("\nREGISTRATION LIST")

    for item in registrations:
        print(
            f"{item['registration_id']} | {item['name']} | "
            f"Roll: {item['roll']} | {item['department']}"
        )
        print(f"  {item['event_name']} ({item['event_id']}) | {item['email']}")


def find_student(registrations):
    roll = input("Student roll/registration number: ").strip().casefold()

    found = [
        item for item in registrations
        if item["roll"].casefold() == roll
    ]

    if not found:
        print("No registrations found for that student.")
        return

    for item in found:
        print(
            f"{item['name']} | {item['department']} | "
            f"{item['event_name']} | ID: {item['registration_id']}"
        )


def cancel_registration(registrations):
    reg_id = input("Registration ID to cancel: ").strip().upper()

    for item in registrations:
        if item["registration_id"] == reg_id:
            registrations.remove(item)

            try:
                save_registrations(registrations)
            except OSError as error:
                registrations.append(item)
                print(f"Could not save cancellation: {error}")
                return

            print(
                f"Cancelled {item['event_name']} registration. "
                "The seat is available again."
            )
            return

    print("Registration ID not found.")


def show_summary(registrations):
    print("\nEVENT SUMMARY")

    for event in EVENTS:
        left = seats_left(event, registrations)
        booked = event["capacity"] - left
        print(
            f"{event['name']}: {booked} registered, "
            f"{left} seats left"
        )

    print(f"Total registrations: {len(registrations)}")


def main():
    registrations = load_registrations()

    while True:
        print("\nCOLLEGE EVENT REGISTRATION PORTAL")
        print("1. View all events and seats")
        print("2. Filter events by category")
        print("3. Register for an event")
        print("4. View all registrations")
        print("5. Find a student's registrations")
        print("6. Cancel using registration ID")
        print("7. Event summary")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_events(registrations)
        elif choice == "2":
            category = input(
                "Category (Technical/Cultural/Sports/Workshop): "
            ).strip()
            show_events(registrations, category)
        elif choice == "3":
            register(registrations)
        elif choice == "4":
            show_registrations(registrations)
        elif choice == "5":
            find_student(registrations)
        elif choice == "6":
            cancel_registration(registrations)
        elif choice == "7":
            show_summary(registrations)
        elif choice == "8":
            print("Thank you for using the portal!")
            break
        else:
            print("Enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
