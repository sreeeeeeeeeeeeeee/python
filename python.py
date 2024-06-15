a=int(input('enter a number :'))
last_digit=a%10
if last_digit %3==0:
    print("the last digit is divisible by 3")
else:
    print("last number is not divisible by 3")