

"""num_array=list();
length=int(input("Enter the number of elements in the array "))
print("Enter the elements in the array")
for i in range(length):
    n=input("num: ")
    num_array.append(int(n))"""


def bubblesort(num_array):
    length=len(num_array)
    if(length==0):
        return ("error empty array")

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
    def test_whenNull(self):
        self.assertEquals(bubblesort([]),"error empty array")
    def test_oneElement(self):
        self.assertEquals(bubblesort([5]),[5])
    def test_TwoElements(self):
        self.assertEquals(bubblesort([5,4]),[4,5])
    def test_equalElement(self):
        self.assertEquals(bubblesort([1,2,1]),[1,1,2])
    def test_allZeros(self):
        self.assertEquals(bubblesort([0,0,0]),[0,0,0])
    def test_threeElements(self):
        self.assertEquals(bubblesort([3,1,9]),[1,3,9])
    def test_negativeElements(self):
        self.assertEquals(bubblesort([1,-1,5]),[-1,1,5])
    def test_varitaionarray(self):
        self.assertEquals(bubblesort([90000,0.0089,-100000,800000,60,-5,0.1]),[-100000,-5,0.0089,0.1,60,90000,800000])


if __name__ == '__main__':
    unittest.main()