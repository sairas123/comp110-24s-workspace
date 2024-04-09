"""Demonstrate Basic list Syntax"""

#Initalize an empty lsit 
grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <- literal

print(grocery_list)

#Add item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending: ")
print(grocery_list)

#Create an already populated list
grocery_list2: list[str] = ["banans", "milk", "bread"]
print("populated list:")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

#indexing
print("print first element of string")
print(grocery_list[0])

#Modifying by Index
print("Before change: ")
print(grocery_list)
grocery_list[1] = "almond milk"
print("After change:")
print(grocery_list)

#you can have duplicates
grocery_list.append("almond milk")
print("Add almond milk again: ")
print(grocery_list)

#Measuring length
print("Length of list:")
print(len(grocery_list))

#Removing an item
grocery_list.pop(1)
print("After removing almond milk:")
print(grocery_list)

#Function name: display
#parameter: list[str]
#return Nothing!
#Print out the list!
print("   Functions! ")

def display(word: list[str]) -> None:
    print(word)

display(grocery_list)
display(["Alyssa", "Erin", "Ak"])
print(x)

#create a list!
# name: crete
#parameters: str and str
#Rv: list[str]
#put both parameters into a list and return that list

def create(word1: str, word2: str) -> list[str] :
    my_list: list[str] = [word1, word2]
    return my_list

x: list[str] = create("Hello", "World") 
print(x)