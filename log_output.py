import random
import string
import time



def gen_rand_str(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

while True:
    length = 10
    random_string = gen_rand_str(length)
    print(random_string)
    time.sleep(5)