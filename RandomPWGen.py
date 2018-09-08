import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(-_=+)'
password = ''

print('Password Generator')
print('==================')
length = input("Enter your password length: ")
length = int(length)

for i in range(length):
    password += random.SystemRandom().choice(chars)
print("Password: ", password)

