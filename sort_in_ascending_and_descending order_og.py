from array import array
#create an array
arr= array('i',[5,2,8,1,4])
print("Original Array: ", arr)
#bubble sort ascending
for i in range (len(arr)):
    for j in range (0,len(arr)-i-1):
        if arr[j]>arr[+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("ascending arder:",arr)
#bubble sort descending
for i in range(len(arr)):
    for j in range (0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("descending arder:",arr)