import numpy as np

class student:
    def __init__(self):
        self.data = np.array([])

    def Add_data(self, data):
        self.data = np.array(data)
        print(self.data)

    def Total(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            n = np.sum(self.data, axis=1).reshape(-1, 1)
            s = np.hstack([self.data, n])
            print(s)

    def average(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            p = np.average(self.data, axis=1).reshape(-1, 1)
            s = np.hstack([self.data, p])
            print(s)

    def pass_fail(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            n = np.sum(self.data, axis=1)

            con = [n >= 50]
            ch = ["pass"]

            gr = np.select(con, ch, default="fail")
            gr_rol = gr.reshape(-1, 1)

            re = np.hstack([self.data, gr_rol])
            print(re)

    def lower_upper(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            n = np.sum(self.data, axis=1)

            print(f"Highest Score = {np.max(n)}")
            print(f"Lowest Score = {np.min(n)}")

    def Grade_Distribution(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            n = np.sum(self.data, axis=1)

            con = [
                (n >= 90),
                (n >= 80) & (n < 90),
                (n >= 60) & (n < 80),
                (n >= 50) & (n < 60)
            ]

            ch = ["A", "B", "C", "D"]

            gr = np.select(con, ch, default="Fail")
            gr_rol = gr.reshape(-1, 1)

            re = np.hstack([self.data, gr_rol])
            print(re)

    def Student_Ranking(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            n = np.sum(self.data, axis=1)

            t = np.sort(n)

            con = [
                n >= t[-1],
                n >= t[-2],
                n >= t[-3],
                n >= np.median(n)
            ]

            ch = ["First", "Second", "Third", "Fourth"]

            gr = np.select(con, ch, default="No Rank")
            gr_rol = gr.reshape(-1, 1)

            re = np.hstack([self.data, gr_rol])
            print(re)

    def Subject_Average(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            print(np.mean(self.data, axis=0))

    def Highest_Marks_Per_Subject(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            print(np.max(self.data, axis=0))

    def Lowest_Marks_Per_Subject(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            print(np.min(self.data, axis=0))

    def Pass_Percentage(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            n = np.sum(self.data, axis=1)

            percentile = (
                n / (np.size(self.data, axis=1) * 100) * 100
            ).reshape(-1, 1)

            re = np.hstack([self.data, percentile])

            con = [percentile >= 50]
            ch = ["pass"]

            gr = np.select(con, ch, default="fail")
            gr = gr.reshape(-1, 1)

            r = np.hstack([re, gr])

            print(r)

    def Overall_mean(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            print(f"Overall Mean = {np.mean(self.data)}")

    def Overall_median(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            print(f"Overall Median = {np.median(self.data)}")

    def Overall_standard_deviation(self):
        if self.data.size == 0:
            print("array is empty")
        else:
            print(f"Overall Standard Deviation = {np.std(self.data)}")


st = student()

while True:
    print("\n===== Mini Data Analysis Engine =====")
    print("1. Add Data")
    print("2. Total Marks")
    print("3. Average Marks")
    print("4. Pass/Fail")
    print("5. Highest/Lowest Score")
    print("6. Grade Distribution")
    print("7. Student Ranking")
    print("8. Subject Average")
    print("9. Highest Marks Per Subject")
    print("10. Lowest Marks Per Subject")
    print("11. Pass Percentage")
    print("12. Overall Mean")
    print("13. Overall Median")
    print("14. Overall Standard Deviation")
    print("15. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        rows = int(input("Enter Number of Students: "))

        data = []

        for i in range(rows):
            row = list(map(int, input(f"Student {i+1}: ").split()))
            data.append(row)

        st.Add_data(data)

    elif ch == 2:
        st.Total()

    elif ch == 3:
        st.average()

    elif ch == 4:
        st.pass_fail()

    elif ch == 5:
        st.lower_upper()

    elif ch == 6:
        st.Grade_Distribution()

    elif ch == 7:
        st.Student_Ranking()

    elif ch == 8:
        st.Subject_Average()

    elif ch == 9:
        st.Highest_Marks_Per_Subject()

    elif ch == 10:
        st.Lowest_Marks_Per_Subject()

    elif ch == 11:
        st.Pass_Percentage()

    elif ch == 12:
        st.Overall_mean()

    elif ch == 13:
        st.Overall_median()

    elif ch == 14:
        st.Overall_standard_deviation()

    elif ch == 15:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")