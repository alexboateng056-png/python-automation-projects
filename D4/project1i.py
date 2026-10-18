print("--REAL ESTATE LEAD QUALIFIER--")
property_leads = [
    {"title": "3-Bedroom Suburban House", "price": 220000 , "verified": True},
    {"title": "5-Bedroom Urban House", "price": 3000000, "verified": False },
    {"title": "2-Bedroom City House", "price": 1800000 , "verified": True },
    {"title": "Single Room Appartment", "price": 65000, "verified": False }
]

for property in property_leads:
    title = property["title"]
    price = property["price"]
    verified = property["verified"]

    if price <= 250000 and verified == True:
        print(f"✅ QUALIFIED LEAD: {title} listed at ${price:.2f} is ready for the CRM!")
    else:
        print(f"❌ Skipped: {title} does not meet criteria.")