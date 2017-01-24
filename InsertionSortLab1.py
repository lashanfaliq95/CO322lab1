"""num_array=list()

length=int(input("Enter the number of elements in the array "))
print("Enter the elements in the array")
for i in range(length):
    n=input("num: ")
    num_array.append(int(n))"""


def insertionSort(num_array):
    length = len(num_array)
    if length == 0:
        return ("error empty array")
    for i in range(1, length):  # we assume the first element is the sorted array
        for j in range(0, i):  # iterating and sorting the sorted section of the array
            if num_array[i] < num_array[j]:
                temp = num_array[j]
                num_array[j] = num_array[i]
                num_array[i] = temp

    return (num_array)


import unittest


class TestinsertionSort(unittest.TestCase):
    def test_whenNull(self):
        self.assertEqual(insertionSort([]), "error empty array")

    def test_oneElement(self):
        self.assertEqual(insertionSort([5]), [5])

    def test_TwoElement(self):
        self.assertEqual(insertionSort([5, 4]), [4, 5])

    def test_equalElement(self):
        self.assertEqual(insertionSort([1, 2, 1]), [1, 1, 2])

    def test_allZeros(self):
        self.assertEqual(insertionSort([0, 0, 0]), [0, 0, 0])

    def test_threeElements(self):
        self.assertEqual(insertionSort([3, 1, 9]), [1, 3, 9])

    def test_negativeElements(self):
        self.assertEqual(insertionSort([1, -1, 5]), [-1, 1, 5])

    def test_varitaionarray(self):
        self.assertEqual(insertionSort([90000, 0.0089, -100000, 800000, 60, -5, 0.1]),
                         [-100000, -5, 0.0089, 0.1, 60, 90000, 800000])


if __name__ == '__main__':
    unittest.main()
