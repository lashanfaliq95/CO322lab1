num_array=list()

length=int(input("Enter the number of elements in the array "))
print("Enter the elements in the array")
for i in range(length):
    n=input("num: ")
    num_array.append(int(n))

for i in range(1,length):#we assume the first element is the sorted array
    for j in range(0,i):#iterating and sorting the sorted section of the array
        if num_array[i]<num_array[j]:
            temp=num_array[j]
            num_array[j]=num_array[i]
            num_array[i]=temp

print(num_array)