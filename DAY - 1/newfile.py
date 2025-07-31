
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())


# Authenticate and connect to Google Sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("D:\PYTHON\GOOGLEPY\halogen-pride-467310-h4-3b17c25042b9.json", scope)
client = gspread.authorize(creds)
sheet = client.open("DemoProject").sheet1  # Use your actual sheet name

def generate_question():
    while True:
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        op = random.choice(['+', '-', '*', '//', '%'])
        if op in ['//', '%'] and n2 == 0:
            continue
        que = f"{n1} {op} {n2}"
        ans = eval(que)
        return que, ans

while True:
    q, ans = generate_question()
    print(f"\nQuestion: {q}")
    
    user_input = input("Enter your answer (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thanks for playing!")
        break

    try:
        user_ans = int(user_input)
        result = "Correct" if user_ans == ans else "Wrong"
        print("🎉 7 Crore!!" if result == "Correct" else f"💸 0 Crore!! Correct answer was: {ans}")
        
        # Store in Google Sheet
        sheet.append_row([q, ans, user_ans, result])

    except ValueError:
        print("⚠️ Invalid input! Please enter a number or 'exit'.")
