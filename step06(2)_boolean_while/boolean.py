total_students = 10
students_arr = []
is_present = False  # we assign boolean value in capitalize form
index = 0


# make students array of dictionaries
while index <= 10:
    students_arr.append({"name": "student" + str(index), "present": is_present})
    index = index + 1
print(students_arr)


# take attendance
student_no = 0
print("Write yes or no if your name is called\n ")
while student_no <= total_students:

    answer = input("student" + str(student_no) + " present?\n")
    print("student answer: " + answer)
    if answer.lower() == "yes":
        students_arr[student_no]["present"] = True
        student_no = student_no + 1 #incrementing loop
    elif answer.lower() == "no":
        students_arr[student_no]["present"] = False
        student_no = student_no + 1 #incrementing loop
    else:
        print("Wrong Input")

# print result
print("\nAttendence completed!")
print("Students Array \n" + str(students_arr))