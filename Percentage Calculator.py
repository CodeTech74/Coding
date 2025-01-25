print("Enter Marks Obtained in 4 subjects")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
coding = int(input("coding :"))

# Let's calculate the percentage of marks
sum = math+english+science+coding
print("sun of math,english,science and coding")
p = (sum/400)*100
print(end="Percentage Mark = ")
print(p)