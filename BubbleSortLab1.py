

"""num_array=list();
length=int(input("Enter the number of elements in the array "))
print("Enter the elements in the array")
for i in range(length):
    n=input("num: ")
    num_array.append(int(n))"""


def bubblesort(num_array):
    length=len(num_array)
    length1 = length

    for i in range(length):#to keep getting the largest and putting it to the right corner
        swap = False
        for j in range(length1):#to get the largest to the right  corner
            if j==length-1:
                break
            if num_array[j]>num_array[j+1]:
                temp=num_array[j+1]
                num_array[j+1]=num_array[j] #swapping
                num_array[j]=temp
                swap=True
        if swap==False:
            break
        length1=length1-1
    return(num_array)


print(bubblesort([]))
import unittest
class TestBubbleSort(unittest.TestCase):
    def test_when_null(self):
        self.assertEquals(bubblesort([]),[])
    def test_only_twoelements(self):
        self.assertEquals(bubblesort([5,4]),[4,5])
    def test_same_element(self):
        self.assertEquals(bubblesort([1,1,1]),[1,1,1])

if __name__ == '__main__':
    unittest.main()