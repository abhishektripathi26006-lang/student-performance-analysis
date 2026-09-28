import matplotlib.pyplot as plt

def plot_all(df, subject_avg):
    # 1. Har student ka Average - Bar Chart
    plt.figure()
    plt.bar(df['Name'], df['Average'])
    plt.xticks(rotation=45)
    plt.title("1. Student Average Marks")
    plt.tight_layout()
    plt.savefig("chart1_student_average.png")

    # 2. Subject Average - Bar Chart
    plt.figure()
    plt.bar(subject_avg.index, subject_avg.values)
    plt.title("2. Subject Wise Average")
    plt.savefig("chart2_subject_avg.png")

    # 3. Attendance vs Marks - Scatter
    plt.figure()
    plt.scatter(df['Attendance'], df['Average'])
    plt.xlabel("Attendance")
    plt.ylabel("Average Marks")
    plt.title("3. Attendance vs Average")
    plt.savefig("chart3_attendance.png")

    # 4. Top 5 Students
    top5 = df.sort_values('Average', ascending=False).head(5)
    plt.figure()
    plt.bar(top5['Name'], top5['Average'])
    plt.title("4. Top 5 Students")
    plt.savefig("chart4_top5.png")

    # 5. Maths Distribution - Histogram
    plt.figure()
    plt.hist(df['Maths'], bins=5)
    plt.title("5. Maths Marks Distribution")
    plt.savefig("chart5_maths_dist.png")

    print("5 Charts saved as PNG files!")