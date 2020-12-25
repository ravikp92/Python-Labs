# Dictionary
a={
    "key":"value",
    "key2": "value2",
    "marks":[1,2,3,4],
    "nested":{"nestedkey":"valueof nested"}
}
print(a)
print(a['key'])
a['marks']=[15,6,7,8]
print(a['marks'])
print(a['nested']['nestedkey']) # Nested

print(a.keys())
print(type(a.keys())) # <class 'dict_keys'>

print(a.values())  # <class 'dict_values'>
print(type(a.values()))


print(a.items()) # dict_items

updateItem={
    "test":"update"
}
a.update(updateItem)
print(a.items())

print(a.get("test"))
print(a["test"])

# Difference is that get does not throw error just return none but array will throw an error 
print(a.get("test2"))
# print(a["test2"])


# Sets

a={1,2,3,4,1}
print(a)
print(type(a)) # <class 'set'>
b={}
print(type(b)) # empty dict <class 'dict'>

c=set()
print(type(c)) # empty set <class 'set'>
c.add(2)
c.add(5)
c.add(5)
c.add(5)
c.add((1,2,3)) # tuples can be added as that can't be changed
# c.add([1,2,3]) # TypeError: unhashable type: 'list'
# c.add({1,2,3}) # TypeError: unhashable type: 'set'
print(c) # Non repetitive elements

print(len(c))
c.remove(5)
print(c)
print(c.pop())
print(c)
print(c.pop())
c.add(2)
c.add(5)
c.add(5)
c.add(5)
print(c)

c.union({3,4,5})
print(c)
c.intersection({3,4,5})
print(c)


# Program

mydict={
    "flakey" : "doubtful",
    "gutted": "guilty",
    "splashed": "faltu kharcha"
}

print("Options are : ", mydict.keys())
user=input("Enter to get meaning of complex words: \n")
print("The meaning "+user+" is : ",mydict.get(user))


s={18,"18",18.0}
print(s)
print(len(s))

# Program create Dictionary 
favlang={}
a1=input('Enter your favorite language Ravi ')
a2=input('Enter your favorite language puri ')
a3=input('Enter your favorite language p ')

favlang['Ravi']=a1
favlang['puri']=a2
favlang['p']=a3

print(favlang)


