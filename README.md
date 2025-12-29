# AI Lead Identification & Scoring System (India)

This project is a reproducible AI-powered data pipeline that identifies business leads, enriches their profiles, and ranks them based on their likelihood to engage.

## What this project does
1. Takes a list of professionals (name, title, company)
2. Enriches each lead with business signals
3. Applies a transparent scoring model (0–100)
4. Ranks leads by probability
5. Publishes results to a live Google Sheet

## Pipeline Flow
Raw Leads CSV → Enrichment → Scoring → Ranking → Google Sheets Output

## Scoring Logic
Leads are scored based on:
- Role seniority
- Industry relevance
- Company size
- Geographic signal
- Engagement signal

Each lead receives a final Probability Score between 0 and 100.

## Output
The ranked lead list is published in a Google Sheet for easy verification.

## How to run
1. Install dependencies  
pip install -r requirements.txt

2. Run enrichment  
python src/enrich_leads.py

3. Run scoring  
python src/scoring_engine.py

4. Upload to Google Sheets  
python src/upload_to_google_sheets.py
