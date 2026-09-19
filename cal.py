def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1 - n2
def multiple(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def avg(n1,n2):
    return (n1 + n2)/2
def per(n1,n2):
      return (n1 * n2) / 100
print("please select a operation:\n " \
      "1. addition\n" \
      "2. sub\n" \
      "3. multiplication\n" \
      "4. division\n" \
      "5.average\n" \
      "6. persentege\n ")
select = int(input("select a operetion from 1,2,3,4,5 6: "))

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
        print(num1, "-", num2, "=", sub(num1, num2))
elif select == 3:
         print(num1, "*", num2, "=", multiple(num1, num2))
elif select == 4:
         print(num1, "/", num2, "=", divide(num1, num2))
elif select == 5:
          print("(",num1,"+", num2, ")", "/","2","=",avg(num1, num2))
elif select == 6:
      print(num1, "%", num2, "=", per(num1,num2) )
else:
      print("invaild operation")