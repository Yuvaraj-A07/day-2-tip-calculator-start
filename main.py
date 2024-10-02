#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome To Tip Calculator")
bill=float(input("What was the total bill?$ "))
tip_per=float(input("What percentage of tip would you like to give? "))
percentage=(bill)*(tip_per/100)
t_bill=bill+percentage
people=int(input("How many people split the bill? "))
pay=(t_bill)/people
ind_bill=round(pay,2)
print("Each person should pay",ind_bill)
