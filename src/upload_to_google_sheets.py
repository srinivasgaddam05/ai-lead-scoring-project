import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Load scored data
df = pd.read_csv("data/scored_leads.csv")

# Replace NaN and infinite values with empty string
df = df.replace([float("inf"), float("-inf")], "")
df = df.fillna("")


# Google API scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# Load credentials
creds = Credentials.from_service_account_file("config/google_creds.json", scopes=scope)
client = gspread.authorize(creds)

# Open sheet
sheet = client.open("AI_Lead_Generation_Output").worksheet("Ranked_Leads")

# Clear old data
sheet.clear()

# Upload headers
sheet.append_row(df.columns.tolist())

# Upload rows
for _, row in df.iterrows():
    sheet.append_row(row.tolist())

print("Google Sheet updated successfully!")
