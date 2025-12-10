str1 = input("Please Enter a sentence: ")
total = 1 

for i in range(len(str1)): 

    if(str1[i] == ' ' ):
    
        total = total + 1

print("Total Number of Words in this String = ", total)