'''
Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

dollarAmount = 8.69

piggyBank = {
    "pennies": 0, // 0.01 // 1cent
    "nickels": 0, // 0.05 // 5cents
    "dimes": 0, // 0.1 // 10cents
    "quarters": 0 // 0.25 // 25cents
}

# Your magic Python code here
That should produce the following output.

#>>> print(piggyBank)
{ 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }
'''
newDollarAmount = 0
roundedAmount = 0
piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0, 
    "quarters": 0 
}


dollarAmount = 10.17

piggyBank["quarters"] = dollarAmount // 0.25
newDollarAmount = dollarAmount - piggyBank["quarters"]*0.25

piggyBank["dimes"] = newDollarAmount // 0.1
newDollarAmount -= piggyBank["dimes"] * 0.1

piggyBank["nickels"] = newDollarAmount // 0.05
newDollarAmount -= piggyBank["nickels"] * 0.05

piggyBank["pennies"] = newDollarAmount // 0.01
newDollarAmount -= piggyBank["pennies"] * 0.01
roundedAmount = round(newDollarAmount,2)
piggyBank["pennies"] += roundedAmount * 100

print (f'Dollar Amount: {dollarAmount} Quarters: {piggyBank["quarters"]} Dimes: {piggyBank["dimes"]} Nickels: {piggyBank["nickels"]} Pennies: {piggyBank["pennies"]}')


