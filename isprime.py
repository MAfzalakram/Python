n = int(input("Enter a number?"))
prime = 1
i = 2
while i < n:
    if n%i == 0:
        prime = 0
    i = i + 1
if prime == 0:
    print("Not a prime")
else:
    print("a prime")

