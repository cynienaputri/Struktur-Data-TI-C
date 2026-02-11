#Access List Items
thislist = ["apple", "banana", "cherry"]

#Negative Indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Change Item Value
thislist = ["apple",  "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Insert Items
thislist= ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pinapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
print.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist(0)
print(thislist) 

#Loop Lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Range/len
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#Sort Lists
thislist= {"orange", "mango", "kiwi", "pinapple", "banana"}
thislist.sort()
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Join List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)