#To print the empty list
#mylist = []
#print(f"{mylist}")

#To print the content of the list
mylist = [11, 22, 33]
print(f"{mylist}")

#To print the element from the list
print(mylist[2], mylist[0])
print(mylist[1])

#To print the string elment from the list
mylist = ["python", "class", "thur"]
print(mylist[0], mylist[2])

#To append the string and integer to the list
mylist.append("day3")
mylist.append(25)
print(mylist)

#To remove the element from the list
mylist.pop(1)
print(mylist)

#To replace the elements in the list
mylist[3] = "Thursday"
print(mylist)

#To add the multiple value
var=[10, "hai", 20, "hello"]
var.extend(mylist)
print(var)

#To remove the string from the list
var.pop()
print(var)

