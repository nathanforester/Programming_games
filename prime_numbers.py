# if the number

num = input()
while True:
    num = int(input())
    for i in range(2, num+1):
        if (num % i) == 0:
            print(num, '', 'is not a prime number')
            break
    else:
        print(num, '', 'is a prime number')

    def prime_number(num):
        for j in range(2, num+1):
            if (num % j) == 0:
                return num + 'is not a prime number'
            else:
                return num + 'is a prime number'




