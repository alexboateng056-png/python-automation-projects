import csv


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

def export_to_csv (lead_list, filename = "crm_leads_export.csv"):
   
    fieldnames = ["title", "price", "location", "verified"]

    with open (filename, mode = 'w', newline="", encoding= "utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames)

        writer.writeheader()

        for lead in lead_list:
            writer.writerow(lead)
    print(f"Successfully! Exported {len(lead_list)} leads to {filename}")

raw_leads_data = [
    ("   4-bedroom executive townhouse   ", " $ 320,000 ", " east legon, accra ", True),
    ("2-bedroom modern apartment", " $ 150,000 ", " osu, accra ", True),
    ("unfinished commercial land", " $ 450,000 ", " tema community 25 ", False)
] 

processed_leads = []

for raw_title, raw_price, raw_location, raw_verified in raw_leads_data:
    clean_leads_data = clean_and_format_lead(raw_title, raw_price, raw_location, raw_verified)
    processed_leads.append(clean_leads_data)

export_to_csv(processed_leads)