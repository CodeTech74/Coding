string = str(input("Please Enter your own word"))
print(len(string))

char = str(input("Please Enter your own character"))
i = 0
count = 0

while(i < len(string)):
    if(string(i) == char):
        count = count + 1
        i = i + 1

print(f"The total number of times {char} has occurred in {string} = {count}")