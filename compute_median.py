from array import array
a1= array('i',[1,2,3,4,5])
n= len(a1)
if n%2==0:
    median1= a1[n//2]
    median2= a1[n//2-1]
    median= (median1+median2)/2
else:
    median= a1[n//2]
print("Original Array: ", a1)
print("Median: ", median)