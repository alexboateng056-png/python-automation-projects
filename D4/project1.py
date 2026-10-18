print("--E-COMERCE PRICE TRACKER BOT--")

#name = input("Enter Product Name To Track Price: ").upper().strip()
#target_price = input("Enter Your Target Price You Want To Purchase: ")
product_catalog ={
    'product_1': {"name": "Washing Machine", "current_price": 1500.00, "target_budget": 2000.00},
    'product_2': {"name": "Rice Cooker", "current_price": 250, "target_budget": 150}, 
    'product_3': {"name": "Heater", "current_price": 90, "target_budget": 100}
    }
for product_id, detail in product_catalog.items():
    name = detail["name"]
    current_price = detail["current_price"]
    target_budget = detail["target_budget"]
    if current_price <= target_budget:
        print(f"🔥 DEAL Alert: {name} is on sale for ${current_price:.2f} (Target was ${target_budget:.2f})!")
    else:
        print(f"⏳ Watching: {name} is currently ${current_price:.2f} (Waiting for ${target_budget:.2f}).")
