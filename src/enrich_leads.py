import pandas as pd

# Load raw leads
raw_df = pd.read_csv("data/raw_leads.csv")

# ---- Enrichment Logic ---- #

def infer_industry(company_name):
    company_name = company_name.lower()
    if "ai" in company_name or "data" in company_name:
        return "AI / Data"
    elif "tech" in company_name or "cloud" in company_name:
        return "Technology"
    else:
        return "IT Services"

def infer_company_size(title):
    title = title.lower()
    if "founder" in title or "co-founder" in title:
        return "Startup"
    elif "head" in title or "manager" in title:
        return "Mid-size"
    else:
        return "Enterprise"

def infer_location():
    return "India"

# Apply enrichment
raw_df["Industry"] = raw_df["Company_Name"].apply(infer_industry)
raw_df["Company_Size"] = raw_df["Job_Title"].apply(infer_company_size)
raw_df["Person_Location"] = raw_df.apply(lambda x: infer_location(), axis=1)
raw_df["Company_HQ"] = raw_df.apply(lambda x: infer_location(), axis=1)

# Placeholder enrichment (intentionally blank for now)
raw_df["Email"] = ""
raw_df["LinkedIn_Profile"] = ""

# Save enriched data
raw_df.to_csv("data/enriched_leads.csv", index=False)

print("Lead enrichment completed. File saved as data/enriched_leads.csv")
