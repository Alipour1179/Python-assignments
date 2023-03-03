#  exercise1:اسم یک دانش آموز را از ورودی بگیرد
# نمره سه درس را از ورودی بگیرد
# معدل دانش آموزا را محاسبه کنید
# معدل دانش آموزا را به همراه اسمش پرینت کنید
# معدل = نمره درس اول + نمره در دوم + نمره درس سوم و درنهایت تقسیم بر تعدادشان
name=input("what's your name?")
family=input("what's your family?")
number1=float(input("enter your math score"))
number2=float(input("enter your science score"))
number3=float(input("enter your art score"))
average=(number1+number2+number3)/3
print(name + ' '+family," 's average is ",average)

# exercise 2: برنامه ای بنویسید که نا شما را از ورودی دریافت نماید و تمام کاراکترهای
# نامتان را پرینت نمائید
# در انتها طول نامتان را پرینت نمائید.
name=input('enter your name')
print(name[0:len(name)])
print(name,"has",len(name),"characters")

# exercise 3: برنامه ای بنویسید که سه عدد را از ورودی دریافت نماید و
# عدد اول را با عدد دوم جمع و از عدد سوم کم کند
# و حاصل را پرینت کنید.
number1=float(input("enter the first number"))
number2=float(input("enter the second number"))
number3=float(input("enter the third number"))
A=number1+number2
B=number3-A
print(B)