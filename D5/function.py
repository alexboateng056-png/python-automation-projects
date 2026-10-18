def clean_and_format_lead(raw_title, raw_price, raw_location, is_verified):
    #cleaning price (float, no "$", ",", and spacing)
   str_price = raw_price.replace("$","").replace(",", "").strip()
   clean_price = float(str_price)

   #cleaning text field (Sentence case, no space)

   clean_title = raw_title.strip().title()
   clean_location = raw_location.strip().title()

   lead_record = {
      "title": clean_title,
      "price": clean_price,
      "location": clean_location,
      "verified": is_verified
   }

   return lead_record


structure_lead = clean_and_format_lead("Suburban 3 Bedroom House", "$ 345,098", "tema, cocoa villa ", True)

print("--CLEANED CRM LEAD RECORD--")
for key, value in structure_lead.items():
   print(f"{key.capitalize()}: {value}")