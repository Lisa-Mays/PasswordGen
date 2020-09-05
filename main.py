# This program will generate a 10 character random password
# It will include uppercase, lowercase, numbers and random signs
import random

# Write Welcome Message
print('Welcome to the random password generator!')

# Generate 3 uppercase letters
ucletter1 = chr(random.randint(65, 90))
ucletter2 = chr(random.randint(65, 90))
ucletter3 = chr(random.randint(65, 90))

# Generate 3 lowercase letters
lcletter1 = chr(random.randint(97, 122))
lcletter2 = chr(random.randint(97, 122))
lcletter3 = chr(random.randint(97, 122))

# Generate 2 digits
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))

# Generate 2 punctuation signs
punct1 = chr(random.randint(33, 64))
punct2 = chr(random.randint(33, 64))

# Set password
password = [ucletter1, ucletter2, ucletter3, lcletter1, lcletter2, lcletter3, digit1, digit2, punct1, punct2]

# Shuffle password
random.shuffle(password)

# Print password
print("Your generated secure password is: ", '' .join(password))


