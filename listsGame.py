
print("Welcome to the List Game")
print("Make List B be the same as List A")
aList = [2,4,6,8,10,15,20]
bList = [4,5,6,8,798,15]
print("List A:", aList)
print("List B:", bList)

def show_menu():
  print("1. Append")
  print("2. Remove")
  print("3. Insert")
  print("4. Pop")
  print("5. Print")
  print("6. DONE: Check Results")

while True:
  show_menu()
  choice = input("Select an option: ")
  if choice == "1":
    value = int(input("Append what value?"))
    bList.append(value)
  elif choice == "2":
    value = int(input("Remove what value?"))
    bList.remove(value)
  elif choice == "3":
    index = int(input("Insert what index?"))
    value = int(input("Insert what value?"))
    bList.insert(index,value)
  elif choice == "4":
    index = int(input("Pop what index?"))
    bList.pop(index)
  elif choice == "5":
    print(bList)
  elif choice == "6":
    if aList == bList:
      print("All Matched! You win")
    else:
      print("No Match, You lose")
    break
  else:
    print("Invalid input, try again")


'''
 append()	Adds an element at the end of the list
 clear()	Removes all the elements from the list
 copy()	Returns a copy of the list
 count()	Returns the number of elements with the specified value
 extend()	Add the elements of a list (or any iterable), to the end of the current list
 index()	Returns the index of the first element with the specified value
 insert()	Adds an element at the specified position
 pop()	Removes the element at the specified position
 remove()	Removes the first item with the specified value
 reverse()	Reverses the order of the list
 sort()	Sorts the list
 '''





































