# Import required Python libraries
import csv
import random
from faker import Faker

# Initialize Faker (used to generate fake data)
fake = Faker()

# Get user input for how many rows to generate and the filename for the CSV file
num_rows = int(input("Enter the number of rows that you want to generate in the CSV file: "))
csv_file = input("Enter the name of the CSV file (e.g., data.csv): ")

# Predefined Adjective-Noun Pairs for Store Names
store_name_pairs = [
    ("Trendy", "Corner"),
    ("Urban", "Treasures"),
    ("Rustic", "Emporium"),
    ("Blissful", "Boutique"),
    ("Vintage", "Vault"),
    ("Cozy", "Nook"),
    ("Modern", "Marvels"),
    ("Chic", "Avenue"),
    ("Elegant", "Essentials"),
    ("Timeless", "Hub"),
    ("Enchanted", "Sanctuary"),
    ("Serene", "Haven"),
    ("Artisan", "Deals"),
    ("Whimsy", "Closet"),
    ("Stylish", "Elegance"),
    ("Radiant", "Shoppe"),
    ("Unique", "Oasis"),
    ("Luxe", "Marketplace"),
    ("Happy", "Reflections"),
    ("Golden", "Merchant"),
    ("Harmony", "Perfection"),
    ("Dapper", "Cabinet"),
    ("Classy", "Creations"),
    ("Eclectic", "Enclave"),
    ("Shimmer", "Shop"),
    ("Purely", "Quest"),
    ("Majestic", "Finds"),
    ("Polished", "Loft"),
]

# Open the CSV file in write mode ('w') and automatically close it after writing
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)  # Create a CSV writer object to write data to the file

    # Writing the header row (column names)
    header = [
        "StoreName",
        "StoreType",
        "StoreOpeningDate",
        "Address",
        "City",
        "State",
        "Country",
        "Region",
        "Manager Name",
    ]
    writer.writerow(header)  # Write the header row into the CSV file

    # Loop to generate fake data for each row, based on the number of rows entered by the user
    for _ in range(num_rows):
        # Pick a random (adjective, noun) pair
        adjective, noun = random.choice(store_name_pairs)

        # Combine them to form a store name
        store_name = f"The {adjective} {noun}"

        # Creating a list of fake data for one row
        row = [
            store_name,
            random.choice(["Exclusive", "MBO", "SMB", "Outlet Stores"]),
            fake.date(),
            fake.address().replace("\n", " ").replace(",", " "),
            fake.city(),
            fake.state(),
            fake.country(),
            random.choice(["North", "South", "East", "West"]),
            fake.first_name(),
        ]

        writer.writerow(row)

print("The process completed successfully.")
