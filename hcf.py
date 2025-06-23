def findHCF(number1 , number2):
    if number2 != 0:
        while (True):
            remainder = number1 % number2
            if remainder == 0:
                return f"HCF of {number1}, {number2} is {number2}"
            else:
                number1 = number2
                number2 = remainder


print(findHCF(90,180))

