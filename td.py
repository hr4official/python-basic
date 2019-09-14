# nested list
#my_list = ["mouse", [8, 4, 6], ['a']]
#print(my_list[1])


# empty list
my_list1 = []
# list of integers
my_list2 = [1, 2, 3]
# list with mixed datatypes
my_list3 = [1, "Hello", 3.4]


#slice lists
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])

#We can add one item to a list using append() method or add several items using extend() method.



#Here is an example to make a list with each item being increasing power of 2.


pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)


#This code is equivalent to

pow2 = []
for x in range(10):
   pow2.append(2 ** x)