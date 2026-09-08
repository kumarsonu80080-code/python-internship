# WAP to take input from 1 to n and find which number is even, odd. and find there sum.
i = 1  
sum = 0  
sum_even = 0
sum_odd = 0
n = int(input("enter the number :"))
for i in range(n+1):  #using for loop for print 1 to n numbers.
    sum += i
    print(i)
    if i % 2 == 0:
        print("number is even :",i)
        sum_even += i
    else:
        print("number is odd :",i)
        sum_odd += i
print("sum of n numbers :",sum)
print("sum of 1 to n even numbers :",sum_even)
print("sum of 1 to n odd numbers :",sum_odd)