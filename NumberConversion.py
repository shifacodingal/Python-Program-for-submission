def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')

# Adding a newline after each binary conversion for clarity
print("Binary of 5:", end=' ')
DecimalToBinary(5)
print()  # Newline

print("Binary of 23:", end=' ')
DecimalToBinary(23)
print()  # Newline

print("Binary of 5:", end=' ')
DecimalToBinary(5)
print()  # Newline
