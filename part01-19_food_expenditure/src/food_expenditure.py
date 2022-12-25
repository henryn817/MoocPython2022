# Write your solution here
numone = int(input("num?"))
numtwo = int(input("num?"))
numthree = int(input("num?"))
daily = ((numone * numtwo) + numthree)/7
weekly = ((numone * numtwo) + numthree)
roun = "{:.1f}".format(daily)

print(roun)
print("Average food expenditure:")
print (f"Daily: {roun} euros")
print (f"Weekly: {weekly} euros")