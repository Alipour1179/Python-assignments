#  برنامه ای بنویسید که سه عدد از ورودی بگیرد
# بزرگترین عدد را نمایش دهد
# کوچکترین عدد را نمایش دهد
# میانگین اعداد را محاسبه نماید
# میانگین یعنی جمع عددعا تقسیم بر تعدادشون
x=int(input("input number1:"))
y=int(input("input number2:"))
z=int(input("input number3:"))
if x > y and x > z:
    print(x,"  is greater than  ", y ," and ", z)
if y > x and y > z:
    print(y,"  is greater than  ", x ," and ", z)
if z > x and z > y:
    print(z,"  is greater than  ", y  ," and ",x)
if x < y and x < z:
    print(x,"  is lower than  ", y ," and ", z)
if y < x and y < z:
    print(y,"  is lower than  ", x ," and ", z)
if z < x and z < y:
    print(z,"  is lower than  ", y  ," and ",x)
average=(x+y+z)/3
print("the average of three numbers is equal to",int(average))    