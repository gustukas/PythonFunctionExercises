x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("ZeroDivisionError - You cannot divide a number by zero.")
finally:
    print("All done!")