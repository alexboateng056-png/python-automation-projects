import csv

def process_and_filter_crm_data (input_filename= "crm_leads_export.csv", output_filename= "qualified_leads.csv", max_budget = 350000):

    qualified_leads = []
    total_scanned = 0
    total_price = 0.0

    with open(input_filename, mode = "r", newline="", encoding="utf-8" ) as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            price = float(row["price"])
            is_verified = row["verified"] == "True"

            if price <= max_budget and is_verified:
                qualified_leads.append(row)
                total_price += price
            total_scanned += 1
            
    avg_price = total_price / len(qualified_leads) if qualified_leads else 0

    fieldnames1 = ["title", "price", "location", "verified"]

    with open(output_filename, mode = "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames1)

        writer.writeheader()

        for lead in qualified_leads:
            writer.writerow(lead)
    print("---AUTOMATION REPORT---\n")
    print(f"Total Leads Found: {len(qualified_leads)} | Total Scanned: {total_scanned} | Average Price: {avg_price}")

process_and_filter_crm_data(input_filename="c:/Users/Alexander_Boateng/Desktop/personal/python/crm_leads_export.csv")
