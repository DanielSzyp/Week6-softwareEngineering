conversion_method = input("1. Feet to Meters\n2. Meters to Feet\n: ")
if conversion_method == '1':
        print("Chosen Feet to Meters")
        feet_input = int(input("Enter Feet: "))
        print(f"Entered {feet_input}")
        calculated_feet = feet_input / 3.281
        print(f"{calculated_feet} Meters")

if conversion_method == '2':
        print("Chosen Meters to Feet")
        Meters_input = int(input("Enter Meters"))
        print(f"Entered {Meters_input}")
        calculated_Feet = Meters_input * 3.2
        print(f"{calculated_Feet} Feet")