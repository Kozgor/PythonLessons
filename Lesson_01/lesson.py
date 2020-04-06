# def sum(a,b):
#     print("Function", a + b)
# a= int(input("First number"))
# b= int(input("Second number"))

# sum(a, b)

# def sum(a,b):
#     return a+ b
# a= int(input("First number"))
# b= int(input("Second number"))
# res = sum(a,b)
# print("Result = ", res)

# global globo

# def sum(a = 0, b = 0):
#     globo = "Vars"
#     return a + b
# a= int(input("First number"))
# b= int(input("Second number"))
# res = sum(a,b)
# print("Result = ", res, globo)

# def sum (*params):
#     res = 0
#     for item in params:
#         print(item)
#         res +=item
#     return res
# result = sum(2,3,5,12,234,234235,23512,12,14)
# print("Result =", result)

# tmp = 10

# for i in range(0, tmp):
#     print(i)

# a = int(input("First number"))
# b = int(input("Second number"))

# def sum(a, b):
#     res = 0
#     for i in range(a+1, b):
#         print("i = ", i)
#         res +=i
#     return res
# result = sum(a, b)
# print("Result => ", result)

# distance = int(input("Enter distance in km\n"))
# time = int(input("Enter time in hours\n"))

# def sport(d, t):
#     result = distance/time
#     return result
# print("Speed is:", sport(distance, time), "km/h")

# arr = [2,3,4,5,1]
# print(arr, "Type -> ", type(arr))
# for i in arr:
#     print(i)
# arr[2] = 100500
# print(arr, "Type -> ", type(arr))

# arr = [3, 5, 9, 3, 5, 1, 5]
# print(arr)

# arr.append("LAST ONE")
# print(arr)

# arr.insert(2, 0.2344)
# print(arr)

# arr.remove(3)
# print(arr)

# print("Index 9 =>", arr.index(9))

# print("Arr length = ", len(arr))
# print("Arr 1 count = ", arr.count(1))
# print("After pop =>", arr.pop())
# print("Min =>", min(arr))
# print("Max =>", max(arr))

# arr2 = [3, 5, 12, 56, [100, 101, 102], 20]
# print(arr2)
# arr2[4][1] = 99
# print(arr2)

# person = ["Jinx", "Garen", "Kassadin", "Katarina", "Darius", "Draven", "Kalista", "Vel'Koz"]
# for i in person:
#     print(i)
# person.sort()
# for i in person:
#     print(i)

# lang = ['C++', "Python", "Java Script", "C#", "Java", "PHP", "HTML", "CSS"]

# prog = lang
# print(prog)
# prog[0] = "Kotlin"
# print("Prog ", prog)
# print("Lang", lang)

# import copy

# prog =copy.deepcopy(lang)
# prog[0] = "Kotlin"
# print("Prog" , prog)
# print("Lang" , lang)

# partOne = lang[:2]
# partTwo = lang[2:5:2]
# print(partOne)
# print(partTwo)

car = ("Jinx", "Caitlyn", "Blitzcrang", "Leona")
#print("Car: " , car)
# for i in car:
#     print(i)
# print(car[-1])

# print(len(car))
# print("Jinx count =", car.count("Jinx"))
# i=0
# while i < len(car):
#     print(car[i])
#     i += 1

# person = ("Bill", 34)

# name, age = person
# print("Name", name, "Age", age)

countries = {
    "UA": "Ukraine",
    "US": "United State of America",
    "CA": "Canada"
}

# for value in countries.values():
#     print("==",value,"==")

# for key, value in countries.items():
#     print(key, "===", value)
# countries.pop('US')
# print('-------------------------------------')
# for key, value in countries.items():
#     print(key, "===", value)

# print(countries["UA"])

# print(countries.get('US'))
# countries["It"] = "Italy"
# print(countries)
