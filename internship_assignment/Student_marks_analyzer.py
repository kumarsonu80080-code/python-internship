print("enter all five subject marks :")
print("Math , Physics , Chemistry , Hindi , English")

total_marks = 500
i = 1
total_obtained_marks = 0
for i in range(5):
    marks = int(input("enter marks :"))
    total_obtained_marks += marks

# math = int(input("enter marks of math :"))
# physics = int(input("enter the marks of physics :"))
# chemistry = int(input("enter the marks of chemistry :"))
# hindi = int(input("enter the marks of hindi :"))
# english = int(input("enter the marks of english :"))
# obtained_marks = math + physics + chemistry + hindi + english

print("total obtained marks : ",total_obtained_marks)
precentage = (total_obtained_marks / total_marks)*100
print("precentage is :",precentage)
if precentage >=90:
    print("grade 'A'")
elif precentage < 90 and precentage >= 75:
    print("grade 'B'")
elif precentage < 75 and precentage >= 60:
    print("grade 'c'")
elif precentage < 60 and precentage >= 40:
    print("grade 'D'")
else:
    print("Fail")