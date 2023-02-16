def prime():
    a = 1
    number = int(input("Enter a Number: "))
    if number <= 1:
        return -1
    else:
        for i in range(2,number):
            if number % i == 0:
                return -1
            else:
                for j in range(2,number+1):
                    a += j
                return 'Number is Prime \nIts sum is ' + str(a)

print(prime())

