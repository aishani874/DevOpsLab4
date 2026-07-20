name = input("Enter student name : ")
roll_no = input("Enter roll no. : ")

eng = input("English : ")
math = input("Math : ")
cse = input("Computer Science : ")
phy = input("Physics : ")

avg = (int(eng)+int(math)+int(cse)+int(phy))/4

print(f"Percentage = {avg}:.2f")

