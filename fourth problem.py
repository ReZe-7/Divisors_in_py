number = int(input("Enter any number to find it's divisor: "))
x = range(1, number+1)
y = []
for divisor in x:
    if number % divisor == 0 :
        y.append(divisor)
print(y)
