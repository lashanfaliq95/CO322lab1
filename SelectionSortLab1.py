"""num_array=list()

length=int(input("Enter the number of elements in the array "))
print("Enter the elements in the array")
for i in range(length):
    n=input("num: ")
    num_array.append(int(n))"""


def selectionsort(num_array):
    length = len(num_array)
    if length == 0:
        return ("error empty array")
    sorted_array = list()

    for i in range(length):  # to get the minimum for each iteration
        min = 1000000000  # to sort in ascending order
        for j in range(length):  # to get the minimum
            if num_array[j] < min:
                min = num_array[j]

        for z in range(length):
            if min == num_array[z]:  # removing the already inserted element
                num_array[z] = 1000000000
                break
        sorted_array.append(min)

    return (sorted_array)


import unittest


class TestSelectionSort(unittest.TestCase):
    def test_whenNull(self):
        self.assertEqual(selectionsort([]), "error empty array")

    def test_oneElement(self):
        self.assertEqual(selectionsort([5]), [5])

    def test_TwoElements(self):
        self.assertEqual(selectionsort([5, 4]), [4, 5])

    def test_equalElement(self):
        self.assertEqual(selectionsort([1, 2, 1]), [1, 1, 2])

    def test_allZeros(self):
        self.assertEqual(selectionsort([0, 0, 0]), [0, 0, 0])

    def test_threeElements(self):
        self.assertEqual(selectionsort([3, 1, 9]), [1, 3, 9])

    def test_negativeElements(self):
        self.assertEqual(selectionsort([1, -1, 5]), [-1, 1, 5])

    def test_varitaionarray(self):
        self.assertEqual(selectionsort([90000, 0.0089, -100000, 800000, 60, -5, 0.1]),
                         [-100000, -5, 0.0089, 0.1, 60, 90000, 800000])


if __name__ == '__main__':
    unittest.main()
