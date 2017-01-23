

num_array=list()

length=int(input("Enter the number of elements in the array "))
print("Enter the elements in the array")
for i in range(length):
    n=input("num: ")
    num_array.append(int(n))

sorted_array=list()

for i in range(length):#to get the minimum for each iteration
    min=10000#to sort in ascending order
    for j in range(length):#to get the minimum
        if num_array[j]<min:
            min=num_array[j]

    for z in range(length):
        if min==num_array[z]:
            num_array[z]=10000
            break
    sorted_array.append(min)

print(sorted_array)
