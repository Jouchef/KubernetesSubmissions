import random
import string
import time

def create_rand_string(length = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def update_file(random_string):
    time_stamp = time.strftime("%H:%M:%S", time.localtime())
    with open("/app/logs/log.txt", "a") as f:
        f.write(f"[{time_stamp}] {random_string}\n")
        print(f"[{time_stamp}] {random_string} written to /app/logs/log.txt")


if __name__ == "__main__":
    random_string = create_rand_string()
    print(f"Generated random string: {random_string}")
    while True:
        update_file(random_string)
        time.sleep(5)