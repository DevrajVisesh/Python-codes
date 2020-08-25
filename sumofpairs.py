## Given an array of numbers, find pairs of numbers whose sum is k.

#X=[-1,5,7,-1,5]
#n=len(X)
#print("Enter the target element:")
#k=int(input())
#Y=[]
#for i in range(0,n):
#    a=X.pop()
#    b=k-a
#    if b in X:
#        Y.append((a,b))
#print(Y)

# to find pairs with given sum. 

def getPairs(arr, n, sum):

	count = 0

	for i in range(0, n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == sum:
				print(arr[i], arr[j])


arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("The pairs are", getPairs(arr, n, sum))

