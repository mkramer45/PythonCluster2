from datetime import date

name = input("Enter Your Name")
age = int(input("What is your age?"))
print("Hi " + name + " You will reach 100 years old by " + str((100-age)+date.today().year))  # must be string, not int

