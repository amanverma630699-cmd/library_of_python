# ===== ARRAY CALCULATOR =====

# 1. Create Array
# 2. View Array
# 3. Add Number
# 4. Subtract Number
# 5. Multiply Number
# 6. Divide Number
# 7. Sum
# 8. Average
# 9. Maximum
# 10. Minimum
# 11. Pass Count
# 12. Fail Count
# 13. Topper
# 14. Lowest Score
# 15. Grade Distribution
# 16. Present Count
# 17. Absent Count
# 18. Attendance Percentage
# 19. Matrix Transpose
# 20. Matrix Sum
# 21. Matrix Mean
# 22. Matrix Shape
# 23. Matrix Flatten
# 24. Sort Array
# 25. Reverse Array
# 26. Find Median
# 27. Square Array
# 28. Square Root
# 29. Find Index
# 30. Exit
import numpy as np


class array_calculator:
    def __init__(self):
        self.array = np.array([])
        self.array_Attend_Track = np.array([])

    def create_array(self):
        self.array = np.array([
            list(map(int, input("Enter student Numbers (row1): ").split())),
            list(map(int, input("Enter student Numbers (row2): ").split()))
        ])
        self.array_Attend_Track = np.array([
            list(map(int, input("Enter Attendance 1 = Present 0 = Absent (row1): ").split())),
            list(map(int, input("Enter Attendance 1 = Present 0 = Absent (row2): ").split()))
        ])

    def view_array(self):
        print(self.array)

    def Add_Number(self, num):
        print(self.array + num)

    def Subtract_Number(self, num):
        print(self.array - num)

    def Multiple_Number(self, num):
        if num == 0:
            print("you can't multiply by zero")
        else:
            print(self.array * num)

    def divide_Number(self, num):
        if num == 0:
            print("you can't divide by zero")
        else:
            print(self.array / num)

    def array_sum(self):
        print(np.sum(self.array))

    def average(self):
        if self.array.size == 0:
            print("array is empty")
        else:
            print(np.average(self.array))

    def array_max(self):
        if self.array.size == 0:
            print("array is empty")
        else:
            print(np.max(self.array))

    def array_min(self):
        if self.array.size == 0:
            print("array is empty")
        else:
            print(np.min(self.array))

    def Pass_(self):
        # Prints pass/fail for each element
        for val in np.ravel(self.array):
            print(f"{val}: {'pass' if val >= 40 else 'fail'}")

    def Fail_(self):
        for val in np.ravel(self.array):
            print(f"{val}: {'fail' if val < 40 else 'pass'}")

    def lower_upper(self):
        sorting = np.sort(np.ravel(self.array))
        if sorting.size:
            print(sorting[0])
            print(sorting[-1])
        else:
            print("array is empty")

    def Grade_Distribution(self):
        for val in np.ravel(self.array):
            if 90 <= val <= 100:
                grade = 'A'
            elif 80 <= val < 90:
                grade = 'B'
            elif 70 <= val < 80:
                grade = 'C'
            elif 60 <= val < 70:
                grade = 'D'
            elif 50 <= val < 60:
                grade = 'E'
            else:
                grade = 'F'
            print(f"{val}: {grade}")

    def Attendance_Tracker(self):
        present = np.sum(self.array_Attend_Track)
        total = self.array_Attend_Track.size
        absent = total - present
        pct = (present / total * 100) if total else 0
        print(present)
        print(np.average(self.array_Attend_Track) if total else 0)
        print(absent)
        print(f"{pct}%")

    def Matrix_Transpose(self):
        print(self.array.T)
        print(self.array_Attend_Track.T)

    def Matrix_Sum(self):
        print(np.sum(self.array))
        print(np.sum(self.array_Attend_Track))

    def Matrix_Mean(self):
        print(np.mean(self.array))
        print(np.mean(self.array_Attend_Track))

    def Matrix_Shape(self):
        print(self.array.shape)
        print(self.array_Attend_Track.shape)

    def Matrix_Median(self):
        print(np.median(self.array))
        print(np.median(self.array_Attend_Track))

    def Matrix_Flatten(self):
        print(self.array.flatten())
        print(self.array_Attend_Track.flatten())

    def Matrix_Sort(self):
        print(np.sort(self.array))
        print(np.sort(self.array_Attend_Track))

    def Matrix_Reverse(self):
        print(self.array[::-1])
        print(self.array_Attend_Track[::-1])

    def matrix_square(self):
        print(self.array ** 2)

    def matrix_square_root(self):
        print(np.sqrt(self.array))

    def matrix_find_index(self):
        print(np.where(self.array))
      
    