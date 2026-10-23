import csv

def export_to_csv (lead_list, filename = "crm_lead_export.csv"):
   
    fieldnames = ["title", "price", "location", "verified"]

    with open (filename, mode = 'w', newline="", encoding= "utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames)

        writer.writeheader()

        for lead in lead_list:
            writer.writerow(lead)
    print(f"Successfully! Exported {len(lead_list)} leads to {filename}")