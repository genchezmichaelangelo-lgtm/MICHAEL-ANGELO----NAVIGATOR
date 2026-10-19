print("=====Mobile Legends Skins Budget Calculator=====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

A = float(input("Enter your budget for Mobile Legends skins: "))
B = float(input("Price Of Layla Skin: "))
C = float(input("Price Of Alucard Skin: "))
D = float(input("Price Of Miya Skin: "))

print("BUYER NAME: ", name)
print("BUYER AGE: ", age)

E = B + C + D
print("TOTAL COST OF SKINS: ", E)

F = A - E
print("REMAINING BUDGET: ", F)