
def partition(Array, low, high):


  pivot = Array[high]


  j = low - 1


  for k in range(low, high):
    if Array[k] <= pivot:

      j = j + 1


      (Array[j], Array[k]) = (Array[k], Array[j])


  (Array[j + 1], Array[high]) = (Array[high], Array[j + 1])


  return j + 1


def quickSort(Array, low, high):
  if low < high:


    pi = partition(Array, low, high)


    quickSort(Array, low, pi - 1)


    quickSort(Array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)





