# Import required Python libraries
import random
import csv

# Get user input for how many rows to generate and the filename for the CSV file
num_rows = int(input("Enter the number of rows that you want to generate in the CSV file: "))
csv_file = input("Enter the name of the CSV file (e.g., data.csv): ")

# Static Data: Product Names, Categories and Brand Names
product_names = [
    "Headphones", "Water Filter", "Air Conditioner", "Telescope", "Smart Light", "Sheets", "Binoculars",
    "Grill", "Surfboard", "Fan", "Lamp", "Soap", "Mattress", "Keyboard", "Juicer", "Pillow", "Backpack",
    "Jacket", "Speaker", "Glasses", "Antivirus", "Toothpaste", "Bed", "Showerhead", "Blender", "Supplement",
    "Suitcase", "Lawn Mower", "Drone", "Fitness Tracker", "Washing Machine", "Vacuum Cleaner", "Microwave",
    "Coffee Maker", "Refrigerator", "Electric Kettle", "Dishwasher", "Oven", "Stove", "Hair Dryer",
    "Electric Shaver", "Electric Toothbrush", "Camera", "Smartphone", "Tablet", "Laptop", "Printer", "Monitor",
    "Smartwatch", "Router", "Projector", "VR Headset", "Game Console", "Smart Thermostat", "Smart Doorbell",
    "Home Security Camera", "Electric Scooter", "Bicycle", "Electric Car", "Helmet", "Treadmill", "Elliptical",
    "Dumbbells", "Yoga Mat", "Camping Tent", "Sleeping Bag", "Flashlight", "Portable Charger", "Power Bank",
    "Bluetooth Speaker", "Earbuds", "Portable Hard Drive", "Memory Card", "External SSD", "Wi-Fi Extender",
    "Laser Printer", "3D Printer", "Sewing Machine", "Air Purifier", "Humidifier", "Dehumidifier", "Robot Vacuum",
    "Pet Feeder", "Pet Bed", "Pet Toy", "Cat Tree", "Dog Leash", "Dog Collar", "Bird Cage", "Aquarium",
    "Fish Food", "Dog House", "Cat Litter Box", "Pet Carrier", "Bird Feeder", "Plant Pot", "Garden Hose",
    "Lawn Sprinkler", "BBQ Grill", "Patio Furniture", "Outdoor Umbrella", "Fire Pit", "Garden Tools",
    "Hiking Boots", "Sleeping Pad", "Cooler", "Water Bottle", "Thermos", "Backpacking Stove", "Camping Chair",
    "Tent", "Tarp", "Rain Jacket", "Hiking Backpack", "Trekking Poles", "Hammock", "Fishing Rod", "Tackle Box",
    "Kayak", "Paddleboard", "Life Jacket", "Snorkel Gear", "Wetsuit", "Ski Goggles", "Snowboard", "Ski Poles",
    "Sled", "Snow Shovel", "Ice Skates", "Basketball", "Soccer Ball", "Tennis Racket", "Golf Clubs",
    "Baseball Glove", "Volleyball", "Badminton Set", "Ping Pong Table", "Dart Board", "Board Game", "Puzzle",
    "Toy Car", "Action Figure", "Doll", "Building Blocks", "Art Supplies", "Craft Kit",
]

category_names = [
    "Electronics", "Home Appliances", "Home & Furniture", "Health & Fitness", "Kitchen & Dining",
    "Outdoor & Garden", "Sports & Recreation", "Pets", "Toys & Games", "Arts & Crafts",
]

brand_names = [
    "LuxeAura", "UrbanGlow", "EtherealEdge", "VelvetVista", "ZenithStyle",
]

# Open the CSV file in write mode ('w') and automatically close it after writing
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)

    # Writing the header row (column names)
    header = ["ProductName", "Category", "Brand", "UnitPrice"]
    writer.writerow(header)

    # Loop to generate data for each row, based on the number of rows entered by the user
    for _ in range(num_rows):
        row = [
            random.choice(product_names),
            random.choice(category_names),
            random.choice(brand_names),
            random.randint(100, 1000),
        ]
        writer.writerow(row)

print("The CSV file was generated successfully!")