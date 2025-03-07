import pandas as pd
import re

def get_valid_input(prompt,pattern,error_message):
    while True:
        user_input=input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print(f"Invalid input! {error_message}")

first_name=get_valid_input("Enter the first Name: ", r"^[A-Za-z]{2,}$","Only alphabets, at least two characters.")
last_name=get_valid_input("Enter the last Name: ", r"^[A-Za-z]{2,}$","Only alphabets, at least two characters.")
age=get_valid_input("Enter Age: ",r"^\d{1,3}$","Only numbers upto three digits.")
phone_number=get_valid_input("Enter Phone number: ",r"^\d{10}$","only 10 digits numbers.")

encrypt_number=phone_number[:3] + "XXXXXXX"
data ={
    'First Name':[first_name],
    'Last Name':[last_name],
    'Age': [int(age)],
    'Phone Number': [encrypt_number]
}

label=[1]
df=pd.DataFrame(data,index=(label))

print(df)
