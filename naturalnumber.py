num = int(input("Enter a number: "))
if num < 0:
    print("Negative numbers are not allowed")
else:
    sum = 0
    i = num  
    while(i > 0):
        sum += i
        i -= 1
    print(f"sum of first {num} natural number is",sum)
