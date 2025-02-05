# 1 to 100 units – Rs. 10/unit
# 100 to 200 units – Rs. 15/unit
# 200 to 300 units – Rs. 20/unit
# above 300 units – Rs. 25/unit
# units take from the user
# 570

unit=int(input("Enter the units: "))
bill=0

if (unit<=100):
    amount=unit*10
    
    bill +=amount
    
    
if(unit>100 and unit<=200):
    unit=unit-100
    amount=unit*15
    bill+=amount+1000
    
elif(unit>200 and unit <=300):
    unit=unit-200
    amount=unit*20
    bill+=amount+2500
    
else:
    unit=unit-300
    amount=unit*25
    bill +=amount+4500
print(bill)
        
