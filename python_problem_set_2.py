#!/usr/bin/env python3

count = 80
if count < 0:
  message = "is a negative number"
  print(count, message)
elif count < 50 and count / 2 == int:
  message = "is less than 50 and its an even number"
  print (count, message)
elif count > 50 and count / 3 == int:
  message = "is greater than 50 and it's divisible by 3"
  print (count, message)
else:
  message = "is a postive number"
  print(count, message)