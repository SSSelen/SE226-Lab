name=input("What is your name? ")
print("Hello" , name)
id=input("What is your Student ID? ")
print("Your ID is " , id)

print("Enter var 1: ")
var1=input()
var1=int(var1)
print("Enter var2: ")
var2=input()
var2=int(var2)
sum=var1+var2
print(sum)
diff=var1-var2
print(diff)
prod=var1*var2
print(prod)

name=input("What is your name? ")
gradeLab=input("What is your lab grade? ")
grade=int(gradeLab)
lab=grade*25/100
gradeMidterm=input("What is your midterm grade? ")
grade=int(gradeMidterm)
midterm=grade*35/100
gradeFinal=input("What is your grade? ")
grade=int(gradeFinal)
final=grade*40/100
score=lab+final+midterm
print("Name: ", name)
print("Lab: ", lab)
print("Midterm: ", midterm)
print("Final:", final)
print("Last Score: ", score)

print("*\n**\n***\n**\n*")
