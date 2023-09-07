def find_leap(y):
  if (y % 400 == 0) and (y % 100 == 0):
    print(y, " is a leap year")
  elif (y % 4 == 0) and (y % 100 != 0):
    print(y, " is a leap year")
  else:
    print(y, " is not a leap year")


y = int(input("Please enter the Year : "))
find_leap(y)