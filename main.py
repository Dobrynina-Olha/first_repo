chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)
print(chars)  # Output: ['a', 'b', 'c', 1, 2]

chars = ['a', 'c']
chars.insert(1, 'b')
print(chars)  # Output: ['a', 'b', 'c']

chars = ['a', 'b', 'c']
chars.clear()
print(chars)  # Output: []

my_list = [1, 'Hello', 3.14]
my_list.append(7)
print(my_list)  # Output: [1, 'Hello", 3.14, 4]
           
x = [1, 2, 3] 
x[1] = -2
print(x)

x = ['a', 'b', 'c']
y = x.index('c')
print(y)  # Output: 2

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(6)
print(count_2)  # Output: 4

x = [1, 2, 3, 4, 5]
print(len(x))

x = [3,1,4,1,5,9,2]
x.sort()
print(x)

x = [3,1,4,1,5,9,2]
x.sort(reverse=True)
print(x)

x = ["apple", "banana", "cherry"]
x.sort(key=len)
print(x)  # Output: ['apple', 'banana', 'cherry']

nums = [3,1,4,1,5,9,2]
sorted_nums = sorted(nums)
print(sorted_nums)

nums = [3,1,4,1,5,9,2]
sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']

chars = ['a', 'b']
chars_copy = chars.copy()
print(chars_copy)  # Output: ['a', 'b']

chars = ['banana', 'apple', 'cherry']
chars.reverse()
print(chars)  # Output: ['cherry', 'apple', 'banana']

my_dict = {"name":"Alice", "age":25}
print(my_dict["name"])  # Output: Alice
my_dict["age"] = 28
print(my_dict)
my_dict["age"] = 32
print(my_dict)  # Output: {'name': 'Alice', 'age': 32}
my_dict["email"] ="alice@example.com"
print(my_dict)  # Output: {'name': 'Alice', 'age': 32, 'email': '

my_dict["surname"] = "Dobrynina"
print(my_dict)
my_dict["citizenship"] = "Ukraine"
print(my_dict)  # Output: {'name': 'Alice', 'age': 32, 'email': '
my_dict["name"] = "Olha"
print(my_dict)
print("name" in my_dict)  # Output: True
print("age" in my_dict)



 





