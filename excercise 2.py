num= int(input('please enter a number'))
total = 0

while num > 10:
    digit = num % 10
    total = total + digit
    num = num // 10
print('the average of all digits for ',num,' is ',total/total_digits)
