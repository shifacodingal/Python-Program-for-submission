num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0

while n > 0:
    digit = n % 10
    total = total * 10 +digit
    n //= 10
print(total)
if total == num:
    print("Palindrome Number")
else:
    print("Not an Palindrome Number")