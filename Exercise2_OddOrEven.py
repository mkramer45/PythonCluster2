inputNumber = int(input("Enter a number: "))
inputNumber %= 2  # this is the modulus operator ... so in this scenario, we are taking the inputNumber integer variable
# and dividing by 2 ... when divided by 2, an even number won't contain any decimals, while odds will ... this is how we determine if odd or even
# modulus operator has to deal with focusing on the decimals after division

if inputNumber == 0:
    print("You have entered an even number! ")
else:
    print("You have entered an odd number! ")
