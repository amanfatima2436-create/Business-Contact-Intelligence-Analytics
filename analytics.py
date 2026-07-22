import pandas as pd

from src.data_loading.load_data import load_data
from src.data_cleaning.clean_data import clean_data
from src.visualization.visualize_data import(
    plot_lead_quality_distribution, 
    plot_contact_completeness_distribution, 
    plot_seniority_distribution, 
    plot_contact_information_coverage,
    plot_enrichment_priority_distribution
)

print("=" * 60)
print("Business Contact Intelligence Analytics")
print("=" * 60)

print("Project Started Successfully")

# Load Dataset
data = load_data()

# Clean Dataset
data = clean_data(data)

# Preview Data
print("\nFirst 5 Rows:")
print(data.head())

# Dataset Shape
print("\nDataset Shape:")
print(data.shape)

print("\nTotal Rows:")
print(data.shape[0])

print("\nTotal Columns:")
print(data.shape[1])

# Column Names
print("\nColumn Names:")
print(data.columns)

# Dataset Information
print("\nDataset Information:")
data.info()

# Missing Values
print("\nMissing Values:")
print(data.isnull().sum())

# Duplicate Records
print("\nDuplicate Records:")
print(data.duplicated().sum())

# Duplicate Company Names
print("\nDuplicate Company Names:")
print(data[data.duplicated("law_firms_name", keep=False)])

# Duplicate Websites
print("\nDuplicate Websites:")
print(data[data.duplicated("website", keep=False)])

# Duplicate Email Addresses
print("\nDuplicate Email Addresses:")
print(data[data.duplicated("email", keep=False)])

# Phone Number Audit
print("\nPhone Number Audit:")
print(data["phone_number"].head(10))

print("\nPhone Number Data Type:")
print(data["phone_number"].dtype)

# Phone Number Length Check
phone_lengths = data["phone_number"].dropna().astype(str).map(len)

print("\nPhone Number Lengths:")
print(phone_lengths.value_counts().sort_index())

print("\nPhone Numbers with Unusual Length:")

# Create a mask only for non-missing phone numbers
phone_mask = data["phone_number"].notna()

# Convert non-missing phone numbers to strings and check their length
unusual_mask = (
    data.loc[phone_mask, "phone_number"]
    .astype(str)
    .map(len)
    .isin([10, 11, 12])
    .eq(False)
)

print(
    data.loc[
        data.loc[phone_mask].index[unusual_mask],
        ["law_firms_name", "phone_number"]
    ]
)

# ==============================
# Email Audit
# ==============================

print("\nEmail Audit:")

# Missing Emails
print("\nMissing Emails:")
print(data[data["email"].isna()][
    ["law_firms_name", "first_name", "last_name", "title"]
])

# Email Format Validation
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

invalid_emails = data[
    data["email"].notna() &
    ~data["email"].str.match(email_pattern)
]

print("\nInvalid Email Addresses:")
print(invalid_emails[
    ["law_firms_name", "email"]
])

# Duplicate Email Addresses
duplicate_emails = data[
    data["email"].notna() &
    data["email"].duplicated(keep=False)
].sort_values("email")

print("\nDuplicate Email Addresses:")
print(duplicate_emails[
    ["law_firms_name", "first_name", "last_name", "email"]
])

# Email Domains
email_domains = (
    data["email"]
    .dropna()
    .str.split("@")
    .str[-1]
    .str.lower()
)

print("\nEmail Domain Distribution:")
print(email_domains.value_counts().head(20))

# ==============================
# Contact Completeness Analysis
# ==============================

print("\nContact Completeness Analysis:")

# Count available contact information
contact_fields = [
    "phone_number",
    "email"
]

data["contact_completeness"] = (
    data[contact_fields]
    .notna()
    .sum(axis=1)
)

print("\nContact Completeness Score:")
print(
    data[
        [
            "law_firms_name",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "contact_completeness"
        ]
    ].head(20)
)

# Completeness Distribution
print("\nContact Completeness Distribution:")
print(
    data["contact_completeness"]
    .value_counts()
    .sort_index()
)
print("\nIncomplete Contact Records:")

print(
    data[
        data["contact_completeness"] < 2
    ][
        [
            "law_firms_name",
            "first_name",
            "last_name",
            "title",
            "phone_number",
            "email"
        ]
    ]
)

# ==============================
# Contact Seniority Analysis
# ==============================

print("\nContact Seniority Analysis:")

# Title Distribution
print("\nTitle Distribution:")

title_distribution = (
    data["title"]
    .str.strip()
    .str.lower()
    .value_counts()
)

print(title_distribution)


# Identify senior contacts using title keywords
senior_keywords = [
    "owner",
    "ceo",
    "president",
    "founder",
    "partner",
    "chair",
    "shareholder",
    "principal",
    "director"
]

data["is_senior_contact"] = (
    data["title"]
    .str.lower()
    .apply(
        lambda title: any(
            keyword in title
            for keyword in senior_keywords
        )
    )
)

# Senior Contact Count
senior_count = data["is_senior_contact"].sum()

print("\nSenior Decision Maker Contacts:")
print(senior_count)

# Non-Senior Contact Count
non_senior_count = len(data) - senior_count

print("\nNon-Senior Contacts:")
print(non_senior_count)

# Senior Contact Percentage
senior_percentage = (
    senior_count / len(data)
) * 100

print("\nSenior Decision Maker Percentage:")
print(f"{senior_percentage:.2f}%")

# ==============================
# Lead Quality Scoring
# ==============================

print("\nLead Quality Scoring:")

# Start score at 0
data["lead_quality_score"] = 0

# Senior decision maker
data.loc[
    data["is_senior_contact"],
    "lead_quality_score"
] += 3

# Email available
data.loc[
    data["email"].notna(),
    "lead_quality_score"
] += 2

# Phone available
data.loc[
    data["phone_number"].notna(),
    "lead_quality_score"
] += 2

# Website available
data.loc[
    data["website"].notna() &
    (data["website"].str.strip() != ""),
    "lead_quality_score"
] += 1

# Contact name available
data.loc[
    data["first_name"].notna() &
    data["last_name"].notna(),
    "lead_quality_score"
] += 1


# Classify lead quality
def classify_lead(score):

    if score >= 8:
        return "High Quality Lead"

    elif score >= 5:
        return "Medium Quality Lead"

    else:
        return "Low Quality Lead"


data["lead_quality"] = data[
    "lead_quality_score"
].apply(classify_lead)


# Lead Quality Distribution
print("\nLead Quality Distribution:")
print(
    data["lead_quality"]
    .value_counts()
)


# Average Lead Quality Score
print("\nAverage Lead Quality Score:")
print(
    round(
        data["lead_quality_score"].mean(),
        2
    )
)


# Top Quality Leads
print("\nTop Quality Leads:")

print(
    data.sort_values(
        "lead_quality_score",
        ascending=False
    )[
        [
            "law_firms_name",
            "first_name",
            "last_name",
            "title",
            "email",
            "phone_number",
            "lead_quality_score",
            "lead_quality"
        ]
    ].head(20)
)

# ==============================
# Medium Quality Lead Analysis
# ==============================

print("\nMedium Quality Leads:")

medium_leads = data[
    data["lead_quality"] == "Medium Quality Lead"
]

print(
    medium_leads[
        [
            "law_firms_name",
            "first_name",
            "last_name",
            "title",
            "phone_number",
            "email",
            "lead_quality_score"
        ]
    ]
)

print("\nMedium Lead Missing Information:")

print(
    medium_leads[
        [
            "law_firms_name",
            "phone_number",
            "email"
        ]
    ].isna().sum()
)

# ==============================
# Business Contact Coverage KPIs
# ==============================

print("\nBusiness Contact Coverage KPIs:")

total_contacts = len(data)

# Phone Coverage
phone_coverage = (
    data["phone_number"].notna().sum()
    / total_contacts
) * 100

# Email Coverage
email_coverage = (
    data["email"].notna().sum()
    / total_contacts
) * 100

# Complete Contact Coverage
complete_contacts = (
    data["contact_completeness"] == 2
).sum()

complete_contact_percentage = (
    complete_contacts
    / total_contacts
) * 100

# Senior Decision Maker Coverage
senior_coverage = (
    data["is_senior_contact"].sum()
    / total_contacts
) * 100

# High Quality Lead Coverage
high_quality_leads = (
    data["lead_quality"] == "High Quality Lead"
).sum()

high_quality_percentage = (
    high_quality_leads
    / total_contacts
) * 100


print("\nTotal Contacts:")
print(total_contacts)

print("\nPhone Coverage:")
print(f"{phone_coverage:.2f}%")

print("\nEmail Coverage:")
print(f"{email_coverage:.2f}%")

print("\nComplete Contact Coverage:")
print(f"{complete_contact_percentage:.2f}%")

print("\nSenior Decision Maker Coverage:")
print(f"{senior_coverage:.2f}%")

print("\nHigh Quality Lead Coverage:")
print(f"{high_quality_percentage:.2f}%")

# ==============================
# Company Level Analysis
# ==============================

print("\nCompany Level Analysis:")

# Number of contacts per company
contacts_per_company = (
    data["law_firms_name"]
    .value_counts()
)

print("\nContacts Per Company:")
print(contacts_per_company)

# Companies with more than one contact
multiple_contact_companies = (
    contacts_per_company[
        contacts_per_company > 1
    ]
)

print("\nCompanies with Multiple Contacts:")
print(multiple_contact_companies)

# Total unique companies
unique_companies = data["law_firms_name"].nunique()

print("\nTotal Unique Companies:")
print(unique_companies)

# ==============================
# Potential Duplicate Companies
# ==============================

print("\nPotential Duplicate Company Analysis:")

# Normalize company names
data["normalized_company_name"] = (
    data["law_firms_name"]
    .str.lower()
    .str.replace(r"[^a-z0-9]", "", regex=True)
)

# Find duplicate normalized company names
potential_duplicate_companies = data[
    data["normalized_company_name"].duplicated(
        keep=False
    )
].sort_values(
    "normalized_company_name"
)

print("\nPotential Duplicate Companies:")

print(
    potential_duplicate_companies[
        [
            "law_firms_name",
            "website",
            "first_name",
            "last_name",
            "email"
        ]
    ]
)
# ==============================
# Data Enrichment Priority
# ==============================

print("\nData Enrichment Priority Analysis:")


def assign_enrichment_priority(row):

    phone_missing = pd.isna(row["phone_number"])
    email_missing = pd.isna(row["email"])

    if phone_missing and email_missing:
        return "High Priority"

    elif phone_missing or email_missing:
        return "Medium Priority"

    else:
        return "Low Priority"


data["enrichment_priority"] = data.apply(
    assign_enrichment_priority,
    axis=1
)


# Priority Distribution
print("\nEnrichment Priority Distribution:")

print(
    data["enrichment_priority"]
    .value_counts()
)


# High and Medium Priority Contacts
print("\nContacts Requiring Data Enrichment:")

print(
    data[
        data["enrichment_priority"] != "Low Priority"
    ][
        [
            "law_firms_name",
            "first_name",
            "last_name",
            "title",
            "phone_number",
            "email",
            "enrichment_priority"
        ]
    ]
)

# ==============================
# Save Processed Analytics Data
# ==============================

processed_data_path = (
    "data/processed/business_contact_analytics.csv"
)

data.to_csv(
    processed_data_path,
    index=False
)

print("\nProcessed analytics data saved successfully.")

print(
    f"File location: "
    f"{processed_data_path}"
)

# ==============================
# Visualizations
# ==============================

print("\nGenerating Lead Quality Distribution Chart...")

plot_lead_quality_distribution(data)

print("\nGenerating Contact Completeness Distribution Chart...")

plot_contact_completeness_distribution(data)

print("\nGenerating Seniority Distribution Chart...")

plot_seniority_distribution(data)

print("\nGenerating Contact Information Coverage Chart...")

plot_contact_information_coverage(data)

print("\nGenerating Data Enrichment Priority Chart...")

plot_enrichment_priority_distribution(data)