import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*(){}[]\|/?"
amount = 4
use_for = lower_case + upper_case + numbers + symbols
pass_length = 24

while amount >= 0:
    password = "".join(random.sample(use_for,pass_length))
    amount -=1
    print(f"Your new generated password: {password}")
