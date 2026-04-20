# Jeff Victorino
# 04/19/2026
# Module 4.2 Assignment

"""
CHANGES MADE TO PROGRAM:
1. Added a menu system (Highs / Lows / Exit).
2. Program loops until user chooses Exit.
3. Added ability to plot LOW temperatures in blue.
4. Added sys.exit() for clean program termination.
5. Added function to avoid repeating plotting code.
6. Added user instructions at program start.
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Function to read weather data from CSV
def get_weather_data():
    """Reads dates, highs, and lows from the CSV file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])   # NEW: read low temps column

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


# Function to create plots
def plot_temperatures(dates, temps, color, title):
    """Plots temperature data."""
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# Get data once at start
dates, highs, lows = get_weather_data()

# Menu loop
while True:
    print("\n--- Sitka Weather Viewer ---")
    print("1. View HIGH temperatures")
    print("2. View LOW temperatures")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        # Show highs in RED
        plot_temperatures(
            dates,
            highs,
            'red',
            "Daily High Temperatures - 2018"
        )

    elif choice == '2':
        # Show lows in BLUE
        plot_temperatures(
            dates,
            lows,
            'blue',
            "Daily Low Temperatures - 2018"
        )

    # terminate program
    elif choice == '3':
        print("Thank you for using the Sitka Weather Viewer. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice. Please select 1, 2, or 3.")