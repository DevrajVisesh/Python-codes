#Given the array of n positive numbers, find the missing number.
def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)

    return total - sum_of_A

print("How many elements you want to enter:")
n=int(input())
A=[]
for i in range(n):
    number=int(input())
    A.append(number)
n=len(A)
sum(A)

miss = getMissingNo(A)
print(miss)
