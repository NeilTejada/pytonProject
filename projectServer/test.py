# Dictionaries 

user = {
    "name": "Neil",
    "last_name":"Tejada",
    "age":37,
}
print(user)
print(type(user))

print(user["name"] + user["last_name"])
print(len(user["name"])) #counts the characters
print(len(user)) 

# an array is a list in python
number = [1,2,3]
print(number)

number.append(4)
print(number)

# len = length
print(len(number)) 

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]


def exc1():
#print all the numbers
    total = 0
    count = 0
    count2 = 0

    for age in ages:
        total += age
        print(age)

#count how many numbers are less than 30
        if age < 30:
            count += 1
        print(total)
        print("There are" + str(count) + "number that are less then 30")

#count how many numbers are between 30 and 50
        if age > 30 and age < 50:
            count2 += 1
            print("There are" + str(count2) + "numbers that are between 30 and 50")




#call the function
exc1()