#step 1: user's information

name= input("Enter your name please: ")

if len(name)>15:
    print("name is too long")
elif len(name)<=2:
    print("Name is too short")

age = int(input("Enter your age: "))

if age >115:
    print("enter a realistc age please")
elif age < 1:
    print("Enter a realistic age please")
# step 2: calculations

days = age*365
hours = days*24
minutes = hours*60
seconds = minutes*60

#step3:output

print (name ,"You have lived for",days,"days")
print(name ,"You have lived for",hours,"hours")
print(name ,"You have lived for",minutes,"minutes")
print(name ,"You have lived for",seconds,"seconds")
