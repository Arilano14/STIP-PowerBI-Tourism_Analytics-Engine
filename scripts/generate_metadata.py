import csv
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

print("Generating metadata_kpi_catalog.csv...")
with open(os.path.join(DATA_DIR, 'metadata_kpi_catalog.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["kpi_id", "kpi_name", "category", "description", "format"])
    writer.writerows([
        [1, "Total Arrivals", "Demand", "Total number of international tourist arrivals", "#,##0"],
        [2, "Total Revenue", "Economy", "Total tourism receipts in USD", "$#,##0.00"],
        [3, "Recovery Index", "Resilience", "Current arrivals vs 2019 baseline", "0.0%"],
        [4, "Occupancy Rate", "Capacity", "Average hotel occupancy rate", "0.0%"],
        [5, "Avg Length of Stay", "Behavior", "Average days spent per tourist", "0.0"],
        [6, "Arrival Growth", "Growth", "YoY arrival growth percentage", "0.0%"],
        [7, "Forecast Accuracy", "Predictive", "MAPE of the forecasting model", "0.0%"],
        [8, "GDP Contribution", "Economy", "Tourism revenue as % of GDP", "0.00%"]
    ])

print("Generating metadata_data_source.csv...")
with open(os.path.join(DATA_DIR, 'metadata_data_source.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["source_id", "source_name", "connection_type", "status", "refresh_frequency", "future_api_endpoint"])
    writer.writerows([
        [1, "Dummy Generator", "Local CSV", "Active", "Manual", "N/A"],
        [2, "World Bank", "REST API", "Planned", "Monthly", "api.worldbank.org/v2/country/all/indicator"],
        [3, "Open Meteo", "REST API", "Planned", "Daily", "api.open-meteo.com/v1/historical"],
        [4, "Frankfurter", "REST API", "Planned", "Daily", "api.frankfurter.app/latest"]
    ])

print("Generating metadata_navigation.csv...")
with open(os.path.join(DATA_DIR, 'metadata_navigation.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["page_id", "page_name", "icon", "sort_order", "is_active"])
    writer.writerows([
        [1, "Executive Summary", "Home", 1, "Yes"],
        [2, "Demand Analysis", "BarChart", 2, "Yes"],
        [3, "Economic Drivers", "LineChart", 3, "Yes"],
        [4, "Forecasting", "TrendingUp", 4, "Yes"],
        [5, "Recommendations", "Lightbulb", 5, "Yes"]
    ])

print("Generating metadata_embed.csv...")
with open(os.path.join(DATA_DIR, 'metadata_embed.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["embed_id", "embed_type", "token_type", "role_required", "status"])
    writer.writerows([
        [1, "Report", "EmbedToken", "Viewer", "Ready"],
        [2, "Dashboard", "EmbedToken", "Viewer", "Ready"],
        [3, "QnA", "EmbedToken", "Pro", "Planned"]
    ])

print("Generating metadata_access_control.csv...")
with open(os.path.join(DATA_DIR, 'metadata_access_control.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["role_id", "role_name", "access_level", "rls_filter"])
    writer.writerows([
        [1, "Admin", "Full Access", "None"],
        [2, "Regional Manager", "Restricted", "dim_country[region] = USERPRINCIPALNAME()"],
        [3, "Country Analyst", "Restricted", "dim_country[country_id] = USERPRINCIPALNAME()"],
        [4, "Public Viewer", "Aggregated Only", "None"]
    ])

print("Generating metadata_research_question.csv...")
with open(os.path.join(DATA_DIR, 'metadata_research_question.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["rq_id", "question", "category", "mapped_page"])
    writer.writerows([
        ["RQ1", "How do tourism trends recover post-COVID?", "Trend", "Demand Analysis"],
        ["RQ2", "What are the key drivers of tourism demand?", "Driver", "Economic Drivers"],
        ["RQ3", "Which forecasting model performs best?", "Predictive", "Forecasting"],
        ["RQ4", "How does weather impact tourist arrivals?", "External", "Demand Analysis"],
        ["RQ5", "What is the correlation between exchange rates and arrivals?", "Economic", "Economic Drivers"]
    ])

print("Generating metadata_expected_findings.csv...")
with open(os.path.join(DATA_DIR, 'metadata_expected_findings.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["finding_id", "rq_id", "hypothesis", "validation_status"])
    writer.writerows([
        [1, "RQ1", "Recovery reaches 2019 levels by 2024", "Pending"],
        [2, "RQ2", "GDP growth strongly correlates with tourism receipts", "Pending"],
        [3, "RQ3", "SARIMAX outperforms Baseline due to external regressors", "Pending"],
        [4, "RQ4", "High rainfall negatively impacts short-term arrivals", "Pending"],
        [5, "RQ5", "Weaker local currency boosts international arrivals", "Pending"]
    ])

print("Metadata generation completed successfully.")
