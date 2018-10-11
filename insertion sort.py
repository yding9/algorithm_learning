#insertion sort in nondecreasing order
def insertion_sort(list):
  for i in range(1,len(list)):
    value = list[i]
    hole = i
    while hole > 0 and list[hole-1] > value:
      list[hole] = list[hole-1]
      hole = hole -1
    list[hole] = value
  return list

def main():
  print (insertion_sort([5,3,4,2,1,6,9,7,8]))
  print (insertion_sort([3,3,2,1,7,5,6,5]))
  
if __name__ == '__main__':
  main()



#insertion sort in nonincreasing order
"""
def insertion_sort_decrease(list):
  for i in range(1,len(list)):
    value = list[i]
    hole = i
    while hole > 0 and value > list[hole-1]:
      list[hole] = list[hole-1]
      hole = hole -1
    list[hole] = value
  return list
  
print (insertion_sort_decrease([2,5,3,1,4]))
"""
