#Biletmatik
print("Welcome to the rollercoaster!")
height = int(input("What is your height?\n"))
if height<120: 
   print("You can't ride you should grow up.")
else:
   print("Enjoy!")

#Check Odd or Even

sayi = int(input("Bir sayı giriniz: \n"))
if sayi%2 ==0:
    print("girdiginiz sayi çift")
else:
    print("girdiginiz sayi tek")
    

#Biletmatik level 2
print("Welcome to the rollercoaster!")
height = int(input("What is your height?\n"))
if height> 120: 
   age = int(input("How old are you?\n"))
   if age <=18:
       print("You should pay $7")
   else:
       print("You shold pay $12")
else:
   print("You can't ride you should grow up.")
   
   
   
#Biletmatik level 3
print("Welcome to the rollercoaster!")
height = int(input("What is your height?\n"))
if height> 120: 
   age = int(input("How old are you?\n"))
   if age <=12:
       print("You should pay $5")
   elif age <=18:
       print("You should pay $7")
   else:
       print("You shold pay $12")
else:
   print("You can't ride you should grow up.")
   
   
#♥BMI Calculator
weight = 60
height = 1.62

bmi = weight / (height ** 2)
print(bmi)
if bmi < 18.50:
   print("underweight")
elif bmi < 25:   
    print("normal weight")
else:
    print("overweight")
    
#Biletmatik level 4
print("Welcome to the rollercoaster!")
height = int(input("What is your height?\n"))
if height> 120: 
   age = int(input("How old are you?\n"))
   photo = input("Do you want to take photo?")
   if age <=12:
       print("Child ticket is $5")
   elif age <=18:
       print("Young ticket is $7")
   else:
       print("Adult ticket is $12")
   if photo == "yes":
      if age <=12:
          print("Child ticket with photo is $8")
      elif age <=18:
          print("Young ticket with photo is $11")
      else:
          print("Adult ticket with photo is $15")
       
else:
   print("You can't ride you should grow up.")
   

#Biletmatik level 4 - way2
print("Welcome to the rollercoaster!")
height = int(input("What is your height?\n"))
bill = 0
if height> 120: 
   age = int(input("How old are you?\n"))
   if age <=12:
       bill = 5
       print("Child ticket is $5")
   elif age <=18:
        bill = 7
        print("Young ticket is $7")
   else:
       bill = 12
       print("Adult ticket is $12")
   photos = input("Do you want to take photo say y for yes say n for no\n")    
   if photos == "y":
      bill += 3
      
   print(f"Your final bill is {bill}")
else:
   print("You can't ride you should grow up.")

#Pizza Order Practice
print("Welcome to the Pizza Deliveries")
size = input("What size pizza you want? S, M or L?\n")
pepperoni = input("Do you want pepperoni on your pizza? y or n\n")
extra_cheese = input("Do you want extra cheese? y or n\n")

bill = 0
if size =="S":
    bill = 15
elif size == "M":
     bill =20
else:
    bill = 25
if pepperoni =="y":
   if size == "S":
       bill +=2 
   else:
       bill +=3
if extra_cheese =="y":
   bill +=1 
   
print(f"Your final bill is {bill}")


#Biletmatik level 5
print("Welcome to the rollercoaster!")
height = int(input("What is your height?\n"))
bill = 0
if height> 120: 
   age = int(input("How old are you?\n"))
   if age <=12:
       bill = 5
       print("Child ticket is $5")
   elif age <=18:
        bill = 7
        print("Young ticket is $7")
   elif age <= 55 and age >=45:
       bill = 0
       print("You guys need to be happy!")
   else:
       bill = 12
       print("Adult ticket is $12")
   photos = input("Do you want to take photo say y for yes say n for no\n")    
   if photos == "y":
      bill += 3
      
   print(f"Your final bill is {bill}")
else:
   print("You can't ride you should grow up.")
     