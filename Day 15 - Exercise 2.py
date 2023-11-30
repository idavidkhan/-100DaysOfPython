import time
timestamp = time.strftime(" %H : %M : %S")
print(timestamp)


time = int(time.strftime(" %H "))
if (time <= 10 ):
    print("Good Morning")
elif (time > 10 and time <= 3):
    print("Good Afternoon")
elif (time > 3 and time <= 6):
    print("Good Evening")
else:
    print("Good Night")
