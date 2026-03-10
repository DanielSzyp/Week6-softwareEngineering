current_Time = int(input("What is the time?"))
hours_to_Wait = int(input("How many hours would you like to wait?"))
temp = current_Time + hours_to_Wait
while temp >= 24:
    temp -= 24
print(f"Time of alarm: {temp}")