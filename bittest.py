
str1 = "iS"
str2 = "Is this the real life? Is this just fantasy?"
str2 = str2.lower()
str1 = str1.lower()
print([i for i in range(len(str2)) if str2.startswith(str1, i)])


