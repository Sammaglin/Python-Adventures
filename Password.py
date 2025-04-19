import random
char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*'

file_path = "D:\Passwords.txt"

purpose = input("Enter the purpose of the password: ")
length = int(input("Enter the length of the password: "))
password = ""

for a in range (length):
    password += random.choice(char)

print (purpose)
print (password)

with open(file_path, "a") as pass_txt:
    pass_txt.write(f"{purpose}: {password}\n")

print (f"Password saved in {file_path} ✅")