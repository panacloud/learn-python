# name = input("Please enter your name: ")
# print("Hello, " + name + "!")  # Hello Hammad

prompt = "Welcome to SMU"
prompt += "\nWhat is your name? "  # concatenating strings
name = input(prompt)
print("\nHello, " + name.title() + "!")


marks = input("Enter your English marks out of 100:\n")
marks = int(marks)  # converting string value in integer value

if (marks >= 0) and (marks <= 59):
    print("Failed")
elif (marks >= 60) and (marks <= 70):
    print("B Grade")
elif (marks >= 71) and (marks <= 80):
    print("A Grade")
elif (marks >= 81) and (marks <= 100):
    print("A-one Grade")
else:
    print("Wrong Input")



