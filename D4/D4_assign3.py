#Dictionary

scraped_product = {
    "name": "Wireless Noise-Canceling Headphones", 
    "price": 149.99,
    "stock_status": True,
    "tags": ["audio", "electronics", "sale"]
    } 
scraped_product.update({"price": 119.00, "discount_code": "SAVE20"})

print(f'Product: {scraped_product["name"]} | New Price: ${scraped_product["price"]} | Discount Applied {scraped_product["discount_code"]}')
