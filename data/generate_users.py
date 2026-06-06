import json
import random

names = [
    "Rahul",
    "Priya",
    "Aman",
    "Sneha",
    "Arjun",
    "Neha",
    "Rohit",
    "Ananya",
    "Karan",
    "Meera",
    "Aditya",
    "Pooja",
    "Vikram",
    "Riya",
    "Sarthak",
    "Nidhi",
    "Ayush",
    "Ishita",
    "Harsh",
    "Kavya"
]

users = []

for i in range(1, 21):

    purchases = random.sample(
        range(101, 201),
        random.randint(1, 5)
    )

    cart = random.sample(
        range(101, 201),
        random.randint(1, 3)
    )

    users.append(
        {
            "id": i,
            "name": names[i - 1],
            "purchase_history": purchases,
            "search_history": [
                "Laptop",
                "Mouse",
                "Headphones"
            ],
            "cart_items": cart
        }
    )

with open(
    "data/users.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        users,
        file,
        indent=4
    )

print(
    "20 users generated successfully!"
)