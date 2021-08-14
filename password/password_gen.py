import random
import string


s  = []
s.extend(string.ascii_lowercase)
s.extend(string.ascii_uppercase)
s.extend(string.digits)
s.extend(string.punctuation)

random.shuffle(s)
len = int(input("Enter the password length: "))
t = "".join(s[0:len])
print(t)
