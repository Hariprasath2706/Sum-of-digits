n = int(input("Enter the number: "))
sumvar = 0
while n > 0:
    rem = n % 10          
    sumvar = sumvar + rem 
    n = n // 10           
print("Sum of digits:", sumvar)
