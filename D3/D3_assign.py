# Part 1: The for loop for pagination
pages= [1, 2, 3, 4, 5]

print("--Starting Preparation Scraping--")
for page in pages:
        print(f"Scraping product data from page {page}")

# Part 2: The while loop for connection retry simulation
print("--Testing Server Connection--")

attempt = 0
max_attempt = 3

while attempt < max_attempt:
    print("Attempting to connect to server... ")
    attempt += 1
print("Connection successfull on attempt 3!")