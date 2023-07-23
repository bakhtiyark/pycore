# Simple program to find square root of a number
def square_root1(number):
    for i in range(1, number):
        if(i * i > number):
            return i - 1

# More efficient way to find square root of a number
def square_root(number):
    low = 0 
    high = number
    while(low <= high):
        mid = (low + high) // 2
        if(mid * mid > number):
            high = mid - 1
        else:
            low = mid + 1
    return high

print(square_root(2400))