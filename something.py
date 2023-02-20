print("Something")

name = input("Please input a name. ")
print("Hello, " + name + ".")

phrase = input("Please input a string. ")
reverse = ""

for letter in phrase:
	reverse = letter + reverse

print(upper(reverse))
