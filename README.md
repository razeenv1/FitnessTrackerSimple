# 🏋️‍♂️ FITNESS TRACKER & VISUALIZER 

A command-line fitness tracker designed to help you log your triumphs, monitor your physical efforts, and visualize your journey like a true champion. This mystical application stores your daily steps, calories burned, and exercise duration into a sacred scroll (`fitness_data.csv`) and transforms them into meaningful insights and visual charts.

---

## 📂 HOW TO INSTALL

1. **Navigate to your project directory** using PowerShell or CMD:

```powershell
cd "C:\Path\To\Your\Project"
```

Replace the path with the actual folder where your `.py` file is saved.

2. **Install required dependencies using:**

```powershell
pip install -r requirements.txt
```

If `pip` doesn't work, try:

```powershell
python -m pip install -r requirements.txt
```

---

## 📦 REQUIREMENTS

Your `requirements.txt` should contain:

```
pandas
matplotlib
```

No additional libraries are required. All other modules (like `csv`, `os`, and `datetime`) are built into Python.

---

## ▶️ HOW TO RUN THE APP

Once you’ve installed the dependencies, run the application using:

```powershell
python fitness_tracker.py
```

This will launch the interactive CLI where your journey begins.

---

## 🧠 APP OVERVIEW

When the app starts, it checks if the sacred scroll (`fitness_data.csv`) exists. If not, it will forge one with the correct headers. From there, you’re guided by a simple menu system:

```
=============================================
   Inside the Mind and Muscles of Champions  
      Fitness Tracking & Visualization       
=============================================
1. Add New Fitness Data
2. Analyze Fitness Data
3. Visualize Fitness Progress
4. Exit the Application
```

---

## ✍️ 1. ADD NEW FITNESS DATA

This lets you **log daily exercise data**, including:

- 📅 **Date** (format: `YYYY-MM-DD`)
- 👣 **Steps taken**
- 🔥 **Calories burned**
- ⏱️ **Workout duration in minutes**

Your inputs are validated to ensure they’re in proper format and not negative. The entry is then appended to `fitness_data.csv`.

If this file doesn't exist, the app will **automatically create it**, complete with headers:
```
Timestamp, StepsCount, CaloriesBurned, WorkoutDurationMinutes
```

---

## 📊 2. ANALYZE FITNESS DATA

This option reads your saved data and presents:

- ✅ **Total steps taken**
- 🔥 **Total calories burned**
- 🧮 **Average workout duration**
- 📈 **Detailed statistics** including:
  - Count
  - Mean
  - Standard Deviation
  - Min / Max
  - Percentiles

If the file is missing or empty, it will notify you to log data first.

---

## 📈 3. VISUALIZE FITNESS PROGRESS

Transforms your data into **beautiful charts**:

### 📅 Bar Chart – Last 7 Days of Steps
- X-axis: Dates
- Y-axis: Steps
- The **highest-performing day** is shown in a **golden glow** (`#F5A623`)
- All others in cool blue (`#4A90E2`)

### 🔴 Line Graph – Calories Burned Over Time
- Tracks calorie expenditure across all dates
- Smooth grid lines and a modern visual style
- Time on the X-axis, calories on the Y-axis

These visualizations give instant feedback and motivation.

---

## ❌ 4. EXIT

Gracefully exits the application when your training is complete.

---

## ⚠️ COMMON ERRORS & TROUBLESHOOTING

| Issue | Solution |
|-------|----------|
| `FileNotFoundError` | Run the app once and choose option 1 to create the CSV. |
| `Invalid date format` | Use format `YYYY-MM-DD` only. |
| `Graph doesn’t show` | Make sure `matplotlib` is installed properly. Try `pip install matplotlib --force-reinstall`. |
| `Nothing happens when I run it` | Check that you're running it from the correct folder and installed dependencies. |

---

## 🧾 FILE STRUCTURE

```
fitness_tracker.py
requirements.txt
README.md
fitness_data.csv  ← created automatically
```

---

## 🛠️ FUTURE IDEAS

- Add BMI and water intake tracking  
- Sync with smartwatches or fitness APIs  
- Export visualizations to PNG or PDF  
- Upgrade to a GUI using PyQt or Tkinter  
- Add daily motivational quotes

---

## ❤️ CREDITS

This app was built for fitness enthusiasts who want a lightweight, no-cloud, no-frills way to track their physical efforts and gain motivation through their own data.

---

## 🔓 LICENSE

This project is free to use, modify, or expand upon. Let the code serve you on your path to greatness.
