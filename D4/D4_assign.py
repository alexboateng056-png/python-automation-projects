# E-Commerce Cleaner
print("--The E-Commerce Cleaner--")

raw_urls_list = [
    "https://store.com/products/laptop-pro",
    "https://store.com/products/wireless-mouse",
    "https://store.com/products/laptop-pro",          
    "https://store.com/products/mechanical-keyboard",
    "https://store.com/products/wireless-mouse",      
    "https://store.com/products/gaming-monitor",
    "https://store.com/products/laptop-pro",         
    "https://store.com/products/usb-c-hub"
]
print(f"Total raw URLs collected: {len(raw_urls_list)}")

unique_urls = set(raw_urls_list)

unique_urls_list = list(unique_urls)
print(f"Unique URLs list: {unique_urls_list}")
print(f"Total new URLs collected: {len(unique_urls_list)}")
