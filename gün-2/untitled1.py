"""
Created on Sun Jan 26 23:19:26 2025
@author: Casper
"""
print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("How much tip would you like to give? 10,12 or 15\n"))
number_of_people = int(input("How many people split the bill?\n"))
final_bill = round(total_bill*(1+percentage/100)/number_of_people,2)
print(f"Each person should pay:${final_bill}")
