#پاسخ سوال1:
# name=input("what's your name?")
# family=input("what's your family?")
# number1=float(input("enter your math score:"))
# number2=float(input("enter your science score:"))
# number3=float(input("enter your art score:"))
# total=number1+number2+number3
# average=(total)/3
# print(name + ' '+family,"'s total score is:",total)
# print(name + ' '+family,"'s average is:",average)

#پاسخ سوال2:
# name=input("enter a name:")
# for i in range(len(name)-1,-1,-1):
#     print(name[i])

#پاسخ سوال3:
# students = []

# for i in range(5):
#     name = input("Enter studnt name:")
#     students.append(name)

# print("Firt student:", students[0])
# print("Last student:",students[-1])

# new_student = input("enter a new student name:")
# students.append(new_student)

# remove_students = input("enter a new student name to remove:")
# if remove_students in students:
#     students.remove(remove_students)
# else:
#     print("Student not found in list.")

# print("Updated student list:",students)

#پاسخ سوال4:
list = []
sum = 0
for j in range(4):
    number=int(input("enter a number:"))
    sum = sum + number
    list.append(sum)
print(list)
print(list[0:3])

#پاسخ سوال5:
# n=2
# for i in range(n):
#     print(" "*(n-i-1)+"*"*(2*i+1))