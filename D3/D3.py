#While loop
#food = input("Enter Your Favourate food (q to quite): ")

#while not food == "q":
#    print(f"{food} is your favourate.")
#   food = input("Enter Your Favourate food (q to quite): ")
#print("Byee")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not a valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")

# For loop
