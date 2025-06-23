def isPalindrome(n : int) -> bool:
    original_number = n
    reversed_number = 0
   
    while (original_number != 0):
        reversed_number = original_number % 10 + reversed_number * 10
        original_number = original_number // 10 
    
    if n == reversed_number:
        return True
    else:
        return False
    
print(isPalindrome(int(313)))