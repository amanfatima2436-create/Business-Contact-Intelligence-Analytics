import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ==============================
# Load Processed Analytics Data
# ==============================

DATA_PATH = Path(
    "data/processed/business_contact_analytics.csv"
)

data = pd.read_csv(DATA_PATH)


# ==============================
# Dashboard KPIs
# ==============================

total_contacts = len(data)

phone_coverage = (
    data["phone_number"].notna().sum()
    / total_contacts
) * 100

email_coverage = (
    data["email"].notna().sum()
    / total_contacts
) * 100

complete_contact_coverage = (
    data["contact_completeness"].eq(2).sum()
    / total_contacts
) * 100

senior_decision_maker_coverage = (
    data["is_senior_contact"].sum()
    / total_contacts
) * 100

high_quality_lead_coverage = (
    data["lead_quality"]
    .eq("High Quality Lead")
    .sum()
    / total_contacts
) * 100


# ==============================
# Print Dashboard KPIs
# ==============================

print("=" * 60)

print(
    "BUSINESS CONTACT INTELLIGENCE "
    "ANALYTICS DASHBOARD"
)

print("=" * 60)

print(
    f"\nTotal Contacts: "
    f"{total_contacts}"
)

print(
    f"Phone Coverage: "
    f"{phone_coverage:.2f}%"
)

print(
    f"Email Coverage: "
    f"{email_coverage:.2f}%"
)

print(
    f"Complete Contact Coverage: "
    f"{complete_contact_coverage:.2f}%"
)

print(
    f"Senior Decision Maker Coverage: "
    f"{senior_decision_maker_coverage:.2f}%"
)

print(
    f"High Quality Lead Coverage: "
    f"{high_quality_lead_coverage:.2f}%"
)


# ==============================
# Chart Output Directory
# ==============================

CHARTS_DIR = Path(
    "dashboard/charts"
)

CHARTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ==============================
# 1. KPI Overview Chart
# ==============================

kpi_names = [
    "Phone Coverage",
    "Email Coverage",
    "Complete Contacts",
    "Senior Decision Makers",
    "High Quality Leads"
]

kpi_values = [
    phone_coverage,
    email_coverage,
    complete_contact_coverage,
    senior_decision_maker_coverage,
    high_quality_lead_coverage
]

plt.figure(figsize=(10, 6))

plt.bar(
    kpi_names,
    kpi_values
)

plt.title(
    "Business Contact Intelligence KPI Overview"
)

plt.xlabel(
    "KPI"
)

plt.ylabel(
    "Coverage Percentage (%)"
)

plt.xticks(
    rotation=25,
    ha="right"
)

plt.ylim(
    0,
    100
)

plt.tight_layout()

plt.savefig(
    CHARTS_DIR
    / "kpi_overview.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==============================
# 2. Lead Quality Distribution
# ==============================

lead_quality_distribution = (
    data["lead_quality"]
    .value_counts()
)

plt.figure(figsize=(8, 5))

plt.bar(
    lead_quality_distribution.index,
    lead_quality_distribution.values
)

plt.title(
    "Lead Quality Distribution"
)

plt.xlabel(
    "Lead Quality"
)

plt.ylabel(
    "Number of Leads"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    CHARTS_DIR
    / "lead_quality_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==============================
# 3. Enrichment Priority
# ==============================

enrichment_distribution = (
    data["enrichment_priority"]
    .value_counts()
    .reindex(
        [
            "High Priority",
            "Medium Priority",
            "Low Priority"
        ],
        fill_value=0
    )
)

plt.figure(figsize=(8, 5))

plt.bar(
    enrichment_distribution.index,
    enrichment_distribution.values
)

plt.title(
    "Data Enrichment Priority Distribution"
)

plt.xlabel(
    "Enrichment Priority"
)

plt.ylabel(
    "Number of Contacts"
)

plt.tight_layout()

plt.savefig(
    CHARTS_DIR
    / "enrichment_priority.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==============================
# 4. Contact Information Coverage
# ==============================

contact_coverage = {
    "Phone Available":
        data["phone_number"].notna().sum(),

    "Email Available":
        data["email"].notna().sum(),

    "Both Available":
        (
            data["phone_number"].notna()
            &
            data["email"].notna()
        ).sum()
}

plt.figure(figsize=(8, 5))

plt.bar(
    contact_coverage.keys(),
    contact_coverage.values()
)

plt.title(
    "Contact Information Coverage"
)

plt.xlabel(
    "Contact Information"
)

plt.ylabel(
    "Number of Contacts"
)

plt.xticks(
    rotation=15
)

plt.tight_layout()

plt.savefig(
    CHARTS_DIR
    / "contact_information_coverage.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==============================
# 5. Senior Decision Maker Analysis
# ==============================

seniority_distribution = {
    "Senior Decision Makers":
        data["is_senior_contact"].sum(),

    "Non-Senior Contacts":
        (
            ~data["is_senior_contact"]
        ).sum()
}

plt.figure(figsize=(8, 5))

plt.bar(
    seniority_distribution.keys(),
    seniority_distribution.values()
)

plt.title(
    "Senior vs Non-Senior Contacts"
)

plt.xlabel(
    "Contact Category"
)

plt.ylabel(
    "Number of Contacts"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    CHARTS_DIR
    / "seniority_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()


# ==============================
# Dashboard Completed
# ==============================

print(
    "\nVisual Dashboard Generated Successfully."
)

print(
    f"Charts saved in: "
    f"{CHARTS_DIR}"
)