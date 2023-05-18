# int(whole numbers) , float (numbers with decimal), round. 
# when defining a number with 2 decimals with round > number=round(input,2)

print("=== BILL SPLITTER ===")

myBill = float(input("What was the bill?: "))
tip=float(input("How much % tip are you paying/have you paid?: "))
numberOfPeople = int(input("How many people?: "))
answer = round((myBill+myBill*tip/100) / numberOfPeople,2)
print("You all owe", answer)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
# squared = 5**2

# remainder of a division
# modulo = 15 % 4

# whole number division
# divisor = 15 // 2