import matplotlib.pyplot as plt
from pathlib import Path


# ==============================
# Charts Output Directory
# ==============================

CHARTS_DIR = Path("src/visualization/charts")

CHARTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ==============================
# 1. Lead Quality Distribution
# ==============================

def plot_lead_quality_distribution(data):
    """
    Create and save a bar chart
    showing lead quality distribution.
    """

    lead_quality_counts = (
        data["lead_quality"]
        .value_counts()
    )

    plt.figure(figsize=(8, 5))

    lead_quality_counts.plot(
        kind="bar"
    )

    plt.title("Lead Quality Distribution")
    plt.xlabel("Lead Quality")
    plt.ylabel("Number of Leads")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig(
        CHARTS_DIR / "lead_quality_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==============================
# 2. Contact Completeness
# ==============================

def plot_contact_completeness_distribution(data):
    """
    Create and save a bar chart
    showing contact completeness distribution.
    """

    completeness_counts = (
        data["contact_completeness"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    completeness_counts.plot(
        kind="bar"
    )

    plt.title("Contact Completeness Distribution")
    plt.xlabel("Contact Completeness Score")
    plt.ylabel("Number of Contacts")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig(
        CHARTS_DIR / "contact_completeness_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==============================
# 3. Senior vs Non-Senior
# ==============================

def plot_seniority_distribution(data):
    """
    Create and save a bar chart
    showing senior vs non-senior contacts.
    """

    seniority_counts = (
        data["is_senior_contact"]
        .map({
            True: "Senior Decision Maker",
            False: "Non-Senior Contact"
        })
        .value_counts()
    )

    plt.figure(figsize=(8, 5))

    seniority_counts.plot(
        kind="bar"
    )

    plt.title("Senior vs Non-Senior Contacts")
    plt.xlabel("Contact Category")
    plt.ylabel("Number of Contacts")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig(
        CHARTS_DIR / "seniority_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==============================
# 4. Contact Information Coverage
# ==============================

def plot_contact_information_coverage(data):
    """
    Create and save a bar chart
    showing phone and email coverage.
    """

    coverage_counts = {
        "Phone Available": data["phone_number"].notna().sum(),
        "Email Available": data["email"].notna().sum(),
    }

    plt.figure(figsize=(8, 5))

    plt.bar(
        coverage_counts.keys(),
        coverage_counts.values()
    )

    plt.title("Contact Information Coverage")
    plt.xlabel("Contact Information")
    plt.ylabel("Number of Contacts")

    plt.tight_layout()

    plt.savefig(
        CHARTS_DIR / "contact_information_coverage.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()


# ==============================
# 5. Data Enrichment Priority
# ==============================

def plot_enrichment_priority_distribution(data):
    """
    Create and save a bar chart
    showing data enrichment priority.
    """

    priority_counts = (
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
        priority_counts.index,
        priority_counts.values
    )

    plt.title("Data Enrichment Priority Distribution")
    plt.xlabel("Enrichment Priority")
    plt.ylabel("Number of Contacts")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig(
        CHARTS_DIR / "enrichment_priority_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()
