import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

PATH_TO_DATA = 'fitness_data.csv'

def initialize_data_file():
    if not os.path.exists(PATH_TO_DATA):
        with open(PATH_TO_DATA, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Timestamp', 'StepsCount', 'CaloriesBurned', 'WorkoutDurationMinutes'])

def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val < 0:
                raise ValueError
            return val
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def record_data():
    print("\n--- Add Fitness Record ---")
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            date_val = datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    steps = get_positive_int("Enter steps: ")
    calories = get_positive_int("Enter calories burned: ")
    duration = get_positive_int("Enter workout duration (minutes): ")

    with open(PATH_TO_DATA, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date_val, steps, calories, duration])

    print("Record added successfully.")

def analyze_data():
    try:
        df = pd.read_csv(PATH_TO_DATA)
        if df.empty:
            print("No data found.")
            return
        
        total_steps = df['StepsCount'].sum()
        total_calories = df['CaloriesBurned'].sum()
        avg_duration = df['WorkoutDurationMinutes'].mean()

        print(f"\nTotal Steps: {total_steps:,}")
        print(f"Total Calories: {total_calories:,}")
        print(f"Average Duration: {avg_duration:.2f} minutes")
        print("\nDetailed Statistics:\n", df.describe())

        # Identify best and worst step days
        best_day = df.loc[df['StepsCount'].idxmax()]
        worst_day = df.loc[df['StepsCount'].idxmin()]
        print(f"\nBest Step Day: {best_day['Timestamp']} - {best_day['StepsCount']} steps")
        print(f"Worst Step Day: {worst_day['Timestamp']} - {worst_day['StepsCount']} steps")

        # Export statistics
        stats_file = 'fitness_summary.csv'
        df.describe().to_csv(stats_file)
        print(f"\nSummary exported to {stats_file}")

    except FileNotFoundError:
        print("Data file not found.")

def visualize_data():
    # Generate step bar chart and calorie line chart
    try:
        df = pd.read_csv(PATH_TO_DATA)
        if df.empty:
            print("No data to visualize.")
            return

        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # Plot last 7 days steps
        recent = df.tail(7)
        plt.style.use('seaborn-v0_8-darkgrid')
        fig, ax = plt.subplots(figsize=(12, 7))
        colors = ['#4A90E2'] * len(recent)
        peak_idx = recent['StepsCount'].idxmax()
        if pd.notna(peak_idx):
            colors[recent.index.get_loc(peak_idx)] = '#F5A623'
        ax.bar(recent['Timestamp'].dt.strftime('%Y-%m-%d'), recent['StepsCount'], color=colors)
        ax.set_title('Steps - Last 7 Days', fontsize=18, fontweight='bold')
        ax.set_xlabel('Date')
        ax.set_ylabel('Steps')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Plot calories over time
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.plot(df['Timestamp'], df['CaloriesBurned'], marker='o', color='#D0021B')
        ax.set_title('Calories Over Time', fontsize=18, fontweight='bold')
        ax.set_xlabel('Date')
        ax.set_ylabel('Calories')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        fig.autofmt_xdate()
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Data file not found.")

def search_by_date_range():
    try:
        df = pd.read_csv(PATH_TO_DATA)
        if df.empty:
            print("No data found.")
            return
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        start = datetime.strptime(input("Start date (YYYY-MM-DD): "), '%Y-%m-%d')
        end = datetime.strptime(input("End date (YYYY-MM-DD): "), '%Y-%m-%d')
        filtered = df[(df['Timestamp'] >= start) & (df['Timestamp'] <= end)]
        print(filtered if not filtered.empty else "No records in range.")
    except Exception as e:
        print("Error:", e)

def delete_record():
    try:
        df = pd.read_csv(PATH_TO_DATA)
        date_str = input("Enter date to delete (YYYY-MM-DD): ")
        df = df[df['Timestamp'] != date_str]
        df.to_csv(CELESTIAL_PATH_TO_DATA, index=False)
        print("Record deleted if it existed.")
    except FileNotFoundError:
        print("Data file not found.")

def main():
    initialize_data_file()
    while True:
        print("\n=== Fitness Tracker ===")
        print("1. Add Data")
        print("2. Analyze Data")
        print("3. Visualize Data")
        print("4. Search by Date Range")
        print("5. Delete Record")
        print("6. Exit")
        choice = input("Select option (1-6): ")
        if choice == '1':
            record_data()
        elif choice == '2':
            analyze_data()
        elif choice == '3':
            visualize_data()
        elif choice == '4':
            search_by_date_range()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()


