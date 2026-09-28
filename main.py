import pandas as pd
import analysis
import charts

# 1. Data Load
df = pd.read_csv("data/students.csv")

# 2. Average Calculate
df = analysis.calculate_average(df)

# 3. Print Reports
print("=== Full Data with Average ===")
print(df)

print("\n=== Subject Wise Average ===")
subject_avg = analysis.subject_average(df)
print(subject_avg)

print("\n=== Top 5 Students ===")
print(analysis.top_students(df))

# 4. Generate 5 Charts
charts.plot_all(df, subject_avg)

print("\nProject Completed Successfully!")