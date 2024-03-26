print("Welcome to the tip calculator!")

total_bill = int(input("What was the total bill: $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?" ))
split = int(input("How many people to split the bill? "))

tip_as_percent = tip/100
total_tip_amount = total_bill * tip_as_percent

final = (total_bill + total_tip_amount) / split

print(f"Each person should pay: ${final}")
