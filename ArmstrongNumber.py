# Armstrong number of order n - n digit no which is sum of digits to the power n
# Here for 3 digits
def degree(n):
    d = 0
    while n>0:
        if n // 10 >= 0:
            d += 1
            n = n // 10
    return(d)
        
def Armstrong(num):
    nsum = 0
    d = degree(num)
    tmp = num
    while tmp> 0:
        digit = tmp % 10
        nsum += digit ** d
        tmp = tmp // 10

    if nsum == num:
        return(True)
    else:
        return(False)

def ArmstrongNos(n1, n2):
    a_nums = []
    for num in range(n1, n2+1):
        if Armstrong(num):
            a_nums.append(num)
    print("Armsstrong Numbers between: ", n1, n2, " are: ")
    for i in a_nums:
        print (i, end=", ")
        
'''
num = int(input("Give a number: "))
if Armstrong(num):
    print(num, " is Armstrong")
else:
    print(num, " is NOT armstrong")


'''
n1, n2 = map(int, input("Give a range as two numbers: ").split())
print(n1, n2)
ArmstrongNos(n1, n2)


