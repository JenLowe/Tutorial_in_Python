def numbers():
  num = 1
  print (num)
  print (type(num))
  print ("int is short for Integer. An integer is a type of number that is a whole number. That is to say not a fraction.")
  input("Press enter to continue\n")
  num2 = 1.5
  print (num2)
  print (type(num2))
  print ("float is short for Floating Point Number. A flot can have up to 15 ditgits after the decimal point. we can see this by the code below where √2 is irrational but only 15 of it 16 ditgits show. We can sometimes get errors in our maths because of this")
  import math
  num3 = math.sqrt(2)
  print(num3)
  input("Press enter to continue\n")
  num4 = 2 + 1j
  print (num4)
  print (type(num4))
  print ("we also have complex numbers. that can be writen in the form x+yj if you don't know what a complex number is don't worry. \n") 
  input("Press enter to continue\n")
  print ("Python picks the type of number formating that it thinks is best but you can change that by useing num = float(num) or num = int(num) ect.")
  print (num)
  print (type(num))
  num = float(num)
  print (num)
  print (type(num))
  num = int(num)
  print (num)
  print (type(num))
  input("Press enter to continue\n")

def lists():
  print ("We have diffent kinds of ways to have muitple items of data.")
  input("Press enter to continue\n")
  text  = "Hello world 1"
  print (text)
  print (type(text))
  print ("str is short for String. A string is what we use for text. A Unicode lookup table is used for strings. we tell python we are making a sring by useing \" \" a string is really a list of only unicode symbols as such we can use some things we would use on a list on a string like for loops")
  input("Press enter to continue\n")
  for letter in text:
    print (letter) 
  input("Press enter to continue\n")
  new_list = [text, 1, 1.5, "more text", 5.2]
  print (new_list)
  print (type(new_list))
  print("A list is an odered set of different items of data. we can hold any type of data in a list. (yes this include lists).\n")
  print ("we tell python we are making a list by useing []\n")
  input("Press enter to continue\n")
  print("One thing to remember with lists is we start counting from 0. So the 1st item in a list is the 0 item (look at code line 49)\n")  
  print (new_list[0]) # 
  print ("list[0] to get item 0 from the list") 
  print (new_list[1]) 
  print ("list[1] to get item 1 from the list") 
  input("Press enter to continue\n")
  print("list can be modify which our next data type can not be")
  input("Press enter to continue\n")
  new_tuple= (1,"some text", 5, 2.5)
  print (new_tuple)
  print (type (new_tuple))
  print ("A Tuple is much like a list but we can not edit data once it is put in a tuple \n")
  print ("We tell python we are making a list by useing () \n")
  print (new_tuple[2])
  print ("a tuple is faster than a list but other that this an being immutable is it much like a list\n")
  input("Press enter to continue\n")
  print("set is are unorded data that removes duplicates of data")
  new_set = {1,"text", 4,1,3}
  print(new_set)
  print(type (new_set))
  input("Press enter to continue\n")
  print("As can be seen by looking in the code the set only have one 1 even though I put 2 in the set (look at code line 65)")
  input("Press enter to continue\n")
  print("we can not get items form a set like we would a list (list[x]) as there is no oder to a set")
  input("Press enter to continue\n")
  new_set.add(5)
  print(new_set)
  new_set.remove("text")
  print(new_set)
  print("we can use set.add and set.remove to edit a set")
  input("Press enter to continue\n")
  print ("we can still use for loops for a set")
  for things in new_set:
    print (things)
  input("Press enter to continue\n")

def dicts(): 
  print ("Dictionarys work a lot like sets in that they are unorded data that removes duplicates \n")
  print ("Dictionarys have a data in pairs called key-value pairs")
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "key":"value"
  }
  print(thisdict)
  print (type(thisdict),"\n")
  print("look at line 87 in code")
  input("Press enter to continue\n")
  print ("Dictionaries cannot have two items with the same key")
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "key":"value"
  }
  print (thisdict)
  print("As you can see by looking at the code (line 101 and 102) items with the same key of year was removed \n")
  input("Press enter to continue\n")
  thisdict = {
  "brand": "Ford",
  "model": "Ford",
  "year": 1964,
  "key":"value"
  }
  print (thisdict)
  print ("However items with diffent keys can have the same value\n")
  input("Press enter to continue\n")
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "key":"value"
  }
  print (thisdict["brand"])
  print ("Much as we can find an item in a list with its index number we can use the key of a item to find its value (see code line 123)\n")
  print (thisdict["key"])
  print("look at code line 125")
  input("Press enter to continue\n")

def ect():
  print ("The last data type we will look at is Boolean\n")
  print ("Boolean can only have 2 values \nTure \n or \nFalse")
  input("Press enter to continue\n")
  x = bool(1)
  print (x)
  print (type(x))
  print("bool is short for Boolean")
  print("We can bool(1) is Ture and bool(0) is False")
  input("Press enter to continue\n")
  print ("most of the time we use we use Booleans in if statements when asking if something is ture of false")
  y = 10 
  a = y == 10
  print (a)
  print (type(a))
  print ("as seen in the code we set y to 10 then ask is y the same as 10 it returns Ture")
  input("Press enter to continue\n")
  print ("The last types of data are all Binary types. You are unlikey to use these but if you want more info on them go to https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview \n")
  input("Press enter to end\n")


print ("Look at both code and console output \n")
numbers()
lists()
dicts()
ect()
