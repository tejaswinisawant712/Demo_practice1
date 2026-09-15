import random  #Choose random
import string

length=int(input("Enter password length"))

characters=string.ascii_letters+string.digits+string.punctuation   #ascii==upper + lowercase letters

password= ""

for i in range(length):      #len of pass
    password+=random.choice(characters)

print("Generated Password:", password)    