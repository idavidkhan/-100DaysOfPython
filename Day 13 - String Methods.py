# Strings are immutable 

a = "David"
b = "David!! !!!!!!!!  David"

print(len(a))
print(a)
print(a.upper())  # converts a string to upper case.
print(a.lower())  # converts a string to lower case.
print(a.rstrip("!"))  # removes any white spaces before and after the string
print(a.replace("David" , "Joseph")) # replaces all occurences of a string with another string
print(a.split(" "))  # splits the given string at the specified instance and returns the separated strings as list items
Heading = "intro to python"
print(Heading.capitalize())  # capatalize the first letter of line 


str1 = "Welcome to the console"
print(len(str1))
print(len(str1.center(50)))
print(a.count("David")) # returns the number of times the given value has occurred within the given string.


print(a.endswith("!!!")) # The endswith() method checks if the string ends with a given value.If yes then return True, else return False.


str2 = "Welcome to the Console !!!"
print(str2.endswith("to" , 4, 10)) # We can even also check for a value in-between the string by providing start and end index positions.


str3 = "He's name is Dan. He is an honest man."
print(str3.find("is")) # The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
# print(str1.index("ishh"))


str4 = "WelcomeToTheConsole2"
print(str4.isalnum()) # This method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.


str5 = "Welcome"
print(str5.isalpha()) # This method returns True only if the entire string only consists of A-Z, a-z.



str6 = "hello world"
print(str6.islower()) # The islower() method returns True if all the characters in the string are lower case, else it returns False.


str7 = "We wish you a Merry Christmas\n"
print(str7.isprintable())  # The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

str8 = "         "       #using Spacebar
print(str8.isspace())  # The isspace() method returns True only and only if the string contains white spaces, else returns False.


str9 = "  "       #using Tab
print(str9.isspace()) # 


str10 = "World Health Organization" 
print(str10.istitle())  # The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str11 = "To kill a Mocking bird"
print(str11.istitle()) 


str11 = "Python is a Interpreted Language" 
print(str11.startswith("Python"))  # This method checks if the string starts with a given value. If yes then return True, else return False.


str12 = "Python is a Interpreted Language" 
print(str12.swapcase())  # This method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str13 = "His name is Dan. Dan is an honest man."
print(str13.title())  # The title() method capitalizes each letter of the word within the string.


