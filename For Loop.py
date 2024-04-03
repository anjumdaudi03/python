for x in range(5):
    print(x)

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi" + friend)

values = [23, 52, 59, 37,48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print ("Total sum: " +str(sum) + " -Average: " + str(sum/length))

product = 1
for n in range(1,10):
  product = product * n

print(product)


# For converting f to cencius\

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))

 # Next


for n in range(10, 0, -2):
    print(n)


for number in range(2,7+1):
    print(number*3)


for x in range(2, -2, -1):
    print(x)


# The loop should print 2, 1, 0, -1

for i in [8,9,10]:
    print(i)

for i in range (5):
    print("Access denied")


name = [" Ana salve", "Diana Puri", "Sania M"]
for i in name:
    print("Welcome,",  i)


for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]" , end=" ")
    print()


teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)


greeting = 'Hello'
for char in greeting:
	print(char)

for i in range(len(greeting)):
    print(i)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”
print(string1[-10:])  # Prints “Earthlings” again
print(string1[55:]) # Prints “” 


greetings = ["Hello", "world"]
print(" ".join(greetings)) # Prints "Hello world"
#You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!") # Prints "Hello, Alice!"


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")

# https://www.tutorialsteacher.com/python/python-map-function

for n in range(10):
  print(n+n)

input = "Four score and seven years ago"
for c in range(len(input)):
        if c in ['a', 'e', 'i', 'o', 'u']:
             print(c)


def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
    print(format_phone("2025551212")) # Outputs: (202) 555-1212