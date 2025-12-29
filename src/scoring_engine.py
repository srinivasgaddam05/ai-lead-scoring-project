import pandas as pd

# Load enriched leads
df = pd.read_csv("data/enriched_leads.csv")

# ---------------- SCORING FUNCTIONS ---------------- #

def score_role(title):
    title = title.lower()
    if "founder" in title or "cto" in title:
        return 30
    elif "head" in title:
        return 25
    elif "manager" in title:
        return 15
    else:
        return 5

def score_industry(industry):
    if industry == "AI / Data":
        return 25
    elif industry == "Technology":
        return 15
    else:
        return 5

def score_company_size(size):
    if size == "Startup":
        return 20
    elif size == "Mid-size":
        return 10
    else:
        return 5

def score_location(location):
    if location == "India":
        return 15
    else:
        return 5

def score_engagement(linkedin):
    if linkedin:
        return 10
    else:
        return 5

# ---------------- APPLY SCORING ---------------- #

df["Role_Score"] = df["Job_Title"].apply(score_role)
df["Industry_Score"] = df["Industry"].apply(score_industry)
df["Company_Size_Score"] = df["Company_Size"].apply(score_company_size)
df["Location_Score"] = df["Person_Location"].apply(score_location)
df["Engagement_Score"] = df["LinkedIn_Profile"].apply(score_engagement)

# Final Probability Score
df["Probability_Score"] = (
    df["Role_Score"]
    + df["Industry_Score"]
    + df["Company_Size_Score"]
    + df["Location_Score"]
    + df["Engagement_Score"]
)

# Rank leads
df = df.sort_values(by="Probability_Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)

# Keep only required final columns
final_df = df[
    [
        "Rank",
        "Probability_Score",
        "Full_Name",
        "Job_Title",
        "Company_Name",
        "Industry",
        "Person_Location",
        "Company_HQ",
        "Company_Size",
        "Email",
        "LinkedIn_Profile",
    ]
]

# Save scored leads
final_df.to_csv("data/scored_leads.csv", index=False)

print("Scoring completed. File saved as data/scored_leads.csv")
