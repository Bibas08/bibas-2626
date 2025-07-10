#find and repalce
name = "Bibas"
print(name.find("Bibas"))
replace = name.replace("Bibas", "Bibas Kumar")
print(replace)

#escape sequence characters
text = "My name is Bibas \n\tand \nI am 21 years old."
print(text)


#wap to detect double space in a string
name = "My  name  is  Bibas"
if "  " in name:
    print("Double space detected.")
  
  #replace double space from problem 3 with single space
name = "My  name  is  Bibas"
name = name.replace("  ", " ")
print(name)

#wap to format the following letter using escape sequence characters
letter = "Dear students,\n\tThis python course is going well\n\tThank you"

