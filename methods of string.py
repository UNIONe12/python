a = "suraj yadav"
b = "SURAJ YADAV"
# uppper and lower  case of string
print(a.upper()) 
print(a.lower())
#to cut same part from string
print(a.strip("yadav")) 
#for replaceing the same part from string 
print(a.replace("suraj ", "r.k sons "))
#for makeing the string in a list
print(a.split(" "))
#captlise mathode for string 
print(a.capitalize())
print(b.capitalize())
#center methode for string
print(a.center(100))
#count in the string 
print(a.count("suraj")) 
# to find index of first time occurance of the word or num  string 
print(a.find("yadav"))
#to conferm that string is ending/starting wih that paticuler word
print(a.endswith("yadav"))
print(a.endswith("raj",2,3))
print(a.startswith("s"))
#to check that string  is in spacial case are capital or not in true/false
c= "ToTheTasj"
print(c.isalnum())
#to check that word first latter are capital or not in true/false
e="The Is "
print(e.istitle())
#to check that string has words only  or not in true/false
print(c.isalpha())
#to check that string is printable  or not in true/false
d= "tothe\n "
print(d.isprintable())
#to check that string all latter are lower/uper case or not in true/false
print(d.islower())
print(d.isupper())
#to check that string  has only blank space  or not in true/false
print(d.isspace())
#to convert every word in uper case
print(d.title())
#to convert every word from lower uper and vise-versa to in uper case
print(d.swapcase())




