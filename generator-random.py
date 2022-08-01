import random
import string

password="".join([random.choice(string.ascii_letters) for _ in range(10)])
print (password)