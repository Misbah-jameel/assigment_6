# Step 1: Custom Exception banao
class InvalidAgeError(Exception):
    pass

# Step 2: Function jo check kare
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18!")
    else:
        print("Access granted ✅")

# Step 3: Try-Except block
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Error:", e)
