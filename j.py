def is_two_power(n):
    while(n > 0):
        if n >> 1 == 0:
            return True
        
    return False

print(is_two_power(6))
