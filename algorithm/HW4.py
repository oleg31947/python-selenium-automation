# import random
# print(range(4))
# r1 = random.randint(0, 10)
# print(r1)

# from random import randint
# #
# length = int(input(f"Input length of array: "))
# array = []
# for i in range(length):
#     item = randint(-100, 100)
#     array.append(item)
# print(array)

def absolute_sum(array):
   summ = 0
   flag = False
   for item in array:
      if flag == True:
        summ += abs(item)
      else:
         if item < 0:
           flag = True
   return summ

print(absolute_sum([5, 3, -2, 8, 6]))