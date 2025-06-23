def swap(x, y):
    temp = x
    x = y
    y = temp

def reverse_loop(numbers):
 
    reverse = []
    for i in range(len(numbers) -1, -1, -1):
        number = numbers[i]
        reverse.append(number)

    return reverse



def reverse_twopointers(numbers):
    start = 0
    end = len(numbers) -1
    while (start < end):
        temp = numbers[start]
        numbers[start] = numbers[end]
        numbers[end] = temp
        start += 1
        end -= 1
    
    return numbers
numbers = [7,5,7,9,0,1,3,-1]
print(reverse_twopointers(numbers))
