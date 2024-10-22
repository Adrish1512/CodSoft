import random
import string

def generate(length):
    pas=[random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice(string.punctuation)]
    remlen=length-len(pas)
    all=random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.punctuation)
    pas+=[random.choice(all) for i in range(remlen)]
    random.shuffle(pas)
    return ''.join(pas)

length=int(input('Enter length of the password: '))
if length>=8:
    pas=generate(length)
    print("Generated Password for you: ", pas)
else:
    print("Length of the Password should atleast be 8.")