a=23
b="ravi"
print(a,b)

# Strings
a="Harry's"
print(a)
#  String slicing
print(a.split("'"))

print(a[0])
#  slice and print 0 to 3 characters.. 0 included and 3 excluded
print(a[0:3])

print(a[2:3])

print(a[:4]) # is same as 0 to 3
print(a[1:]) # is same as 1 to end of length

# Negative indices
print(a[-1]) # is same as getting last element
print(a[5])
print(a[-4:-1]) # opposite indices

# Slicing with skip value
name1 ="raviisgood"
print(name1[1:4:1])
print(name1[1:4:2]) # skip 1 value and go to 2nd
print(name1[0:4:2])

# String Functions

story="Hi My name is ravi"

print(len(story))
print(story.endswith("ravi"))
print(story.count("a"))
print(story.count("ravi"))
print(story.capitalize())
print(story.find("ravi"))

print(story.replace("ravi","14lucky"))

# customize letter 
letter= ''' Dear  <|Name|>
You are selected

Date: <|Date|>
'''
nameof= input("Enter your name\n ")
date= input("Enter date\n ")
letter=letter.replace("<|Name|>",nameof)
letter=letter.replace("<|Date|>",date)
print(letter)

# Double spaces detection
doublespaces=letter.find("  ")
print(doublespaces)


escapeLetter="Dear ravi, you are selected . thanks !"
print(escapeLetter)
formatter_escapeletter= "Dear ravi,\n\t you are selected .\n Thanks !"
print(formatter_escapeletter)
