import csv
import random
import datetime
import os

# Configuration
START_YEAR = 2015
END_YEAR = 2025
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

COUNTRIES = [
    {"id": "ID", "name": "Indonesia", "iso": "IDN", "currency": "IDR", "lat": -0.789, "lon": 113.921, "profile": "mass", "base_arrivals": 1200000, "rev_per_tourist": 1100, "pop": 270000000, "gdp_base": 1000000000000},
    {"id": "TH", "name": "Thailand", "iso": "THA", "currency": "THB", "lat": 15.870, "lon": 100.992, "profile": "growth", "base_arrivals": 2500000, "rev_per_tourist": 1500, "pop": 70000000, "gdp_base": 500000000000},
    {"id": "MY", "name": "Malaysia", "iso": "MYS", "currency": "MYR", "lat": 4.210, "lon": 101.975, "profile": "balanced", "base_arrivals": 2000000, "rev_per_tourist": 800, "pop": 32000000, "gdp_base": 350000000000},
    {"id": "SG", "name": "Singapore", "iso": "SGP", "currency": "SGD", "lat": 1.352, "lon": 103.819, "profile": "premium", "base_arrivals": 1000000, "rev_per_tourist": 2500, "pop": 5700000, "gdp_base": 380000000000},
    {"id": "VN", "name": "Vietnam", "iso": "VNM", "currency": "VND", "lat": 14.058, "lon": 108.277, "profile": "aggressive", "base_arrivals": 800000, "rev_per_tourist": 700, "pop": 98000000, "gdp_base": 280000000000}
]

MODELS = [
    {"id": 1, "name": "Baseline", "type": "Moving Average", "desc": "Simple historical average"},
    {"id": 2, "name": "Prophet", "type": "Time Series", "desc": "Facebook Prophet model with seasonality"},
    {"id": 3, "name": "SARIMAX", "type": "Econometric", "desc": "SARIMAX with weather exogenous variables"}
]

METRICS = [
    {"id": 1, "name": "TCS", "category": "Competitiveness", "unit": "Score"},
    {"id": 2, "name": "Recovery Index", "category": "Resilience", "unit": "Index"},
    {"id": 3, "name": "Arrival Growth", "category": "Growth", "unit": "Percentage"}
]

def get_covid_factor(year, month):
    if year < 2020: return 1.0
    if year == 2020:
        if month <= 2: return 0.9
        if month == 3: return 0.5
        return random.uniform(0.05, 0.1)
    if year == 2021: return random.uniform(0.1, 0.15)
    if year == 2022: return random.uniform(0.2, 0.45)
    if year == 2023: return random.uniform(0.5, 0.75)
    if year == 2024: return random.uniform(0.75, 0.95)
    if year == 2025: return random.uniform(0.95, 1.1)

def get_seasonality(month):
    if month in [12, 7, 8]: return random.uniform(1.1, 1.25)
    if month in [2, 3]: return random.uniform(0.85, 0.95)
    return random.uniform(0.95, 1.05)

print("Generating dim_country.csv...")
with open(os.path.join(DATA_DIR, 'dim_country.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["country_id", "country_name", "iso_code", "region", "currency_code", "latitude", "longitude"])
    for c in COUNTRIES:
        writer.writerow([c["id"], c["name"], c["iso"], "ASEAN", c["currency"], c["lat"], c["lon"]])

print("Generating dim_date.csv...")
with open(os.path.join(DATA_DIR, 'dim_date.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["date_id", "date", "year", "quarter", "month", "month_name", "year_month"])
    for y in range(START_YEAR, END_YEAR + 1):
        for m in range(1, 13):
            d = datetime.date(y, m, 1)
            date_id = int(d.strftime("%Y%m%d"))
            writer.writerow([date_id, d.isoformat(), y, (m - 1) // 3 + 1, m, d.strftime("%B"), d.strftime("%Y-%m")])

print("Generating dim_year.csv...")
with open(os.path.join(DATA_DIR, 'dim_year.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["year_id", "year"])
    for y in range(START_YEAR, END_YEAR + 1):
        writer.writerow([y, y])

print("Generating dim_model.csv...")
with open(os.path.join(DATA_DIR, 'dim_model.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["model_id", "model_name", "model_type", "description"])
    for m in MODELS:
        writer.writerow([m["id"], m["name"], m["type"], m["desc"]])

print("Generating dim_metric.csv...")
with open(os.path.join(DATA_DIR, 'dim_metric.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["metric_id", "metric_name", "metric_category", "unit"])
    for m in METRICS:
        writer.writerow([m["id"], m["name"], m["category"], m["unit"]])

print("Generating fact_tourism_monthly.csv...")
with open(os.path.join(DATA_DIR, 'fact_tourism_monthly.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["tourism_id", "country_id", "date_id", "tourist_arrivals", "tourism_receipts_usd", "hotel_occupancy_rate", "average_length_of_stay"])
    tourism_id = 1
    for y in range(START_YEAR, END_YEAR + 1):
        for m in range(1, 13):
            date_id = int(datetime.date(y, m, 1).strftime("%Y%m%d"))
            covid = get_covid_factor(y, m)
            season = get_seasonality(m)
            for c in COUNTRIES:
                growth_factor = 1.0 + ((y - START_YEAR) * 0.05)
                if c["profile"] == "aggressive": growth_factor = 1.0 + ((y - START_YEAR) * 0.1)
                arrivals = int(c["base_arrivals"] * growth_factor * covid * season * random.uniform(0.95, 1.05))
                revenue = arrivals * c["rev_per_tourist"] * random.uniform(0.9, 1.1)
                occupancy = min(max(random.uniform(0.4, 0.6) * covid * season * 1.5, 0.1), 0.95)
                los = random.uniform(3.0, 7.0) * (1.2 if covid < 0.5 else 1.0)
                writer.writerow([tourism_id, c["id"], date_id, arrivals, round(revenue, 2), round(occupancy, 3), round(los, 1)])
                tourism_id += 1

print("Generating fact_economy_yearly.csv...")
with open(os.path.join(DATA_DIR, 'fact_economy_yearly.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["economy_id", "country_id", "year", "gdp_usd", "gdp_growth_rate", "inflation_rate", "population"])
    econ_id = 1
    for y in range(START_YEAR, END_YEAR + 1):
        for c in COUNTRIES:
            gdp_growth = random.uniform(0.03, 0.07)
            if y == 2020: gdp_growth = random.uniform(-0.06, -0.02)
            gdp = c["gdp_base"] * (1 + gdp_growth) ** (y - START_YEAR)
            inflation = random.uniform(0.01, 0.05) if y < 2022 else random.uniform(0.04, 0.08)
            pop = int(c["pop"] * (1 + 0.01) ** (y - START_YEAR))
            writer.writerow([econ_id, c["id"], y, round(gdp, 2), round(gdp_growth, 3), round(inflation, 3), pop])
            econ_id += 1

print("Generating fact_weather_monthly.csv...")
with open(os.path.join(DATA_DIR, 'fact_weather_monthly.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["weather_id", "country_id", "date_id", "temperature_avg", "rainfall_mm", "humidity_avg"])
    wid = 1
    for y in range(START_YEAR, END_YEAR + 1):
        for m in range(1, 13):
            date_id = int(datetime.date(y, m, 1).strftime("%Y%m%d"))
            for c in COUNTRIES:
                temp = random.uniform(25.0, 32.0)
                rain = random.uniform(50.0, 300.0)
                if m in [11, 12, 1]: rain *= 1.5
                humidity = random.uniform(70.0, 90.0)
                writer.writerow([wid, c["id"], date_id, round(temp, 1), round(rain, 1), round(humidity, 1)])
                wid += 1

print("Generating fact_exchange_rate_monthly.csv...")
with open(os.path.join(DATA_DIR, 'fact_exchange_rate_monthly.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["exchange_id", "country_id", "date_id", "exchange_rate_usd_local", "exchange_rate_change"])
    xid = 1
    base_rates = {"ID": 14000, "TH": 33, "MY": 4.1, "SG": 1.35, "VN": 23000}
    for y in range(START_YEAR, END_YEAR + 1):
        for m in range(1, 13):
            date_id = int(datetime.date(y, m, 1).strftime("%Y%m%d"))
            for c in COUNTRIES:
                rate = base_rates[c["id"]] * random.uniform(0.95, 1.05)
                if y >= 2022: rate *= 1.05
                change = random.uniform(-0.02, 0.02)
                writer.writerow([xid, c["id"], date_id, round(rate, 2), round(change, 4)])
                xid += 1

print("Generating fact_forecast_monthly.csv...")
with open(os.path.join(DATA_DIR, 'fact_forecast_monthly.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["forecast_id", "country_id", "date_id", "actual_arrivals", "forecast_arrivals", "forecast_growth", "model_id", "model_mape"])
    fid = 1
    mapes = {1: 0.22, 2: 0.15, 3: 0.13}
    for y in range(START_YEAR, END_YEAR + 1):
        for m in range(1, 13):
            date_id = int(datetime.date(y, m, 1).strftime("%Y%m%d"))
            covid = get_covid_factor(y, m)
            season = get_seasonality(m)
            for c in COUNTRIES:
                for model_id, mape in mapes.items():
                    growth_factor = 1.0 + ((y - START_YEAR) * 0.05)
                    if c["profile"] == "aggressive": growth_factor = 1.0 + ((y - START_YEAR) * 0.1)
                    actual_arrivals = int(c["base_arrivals"] * growth_factor * covid * season * random.uniform(0.95, 1.05))
                    forecast = int(actual_arrivals * random.uniform(1-mape, 1+mape))
                    growth = random.uniform(-0.05, 0.08)
                    writer.writerow([fid, c["id"], date_id, actual_arrivals, forecast, round(growth, 3), model_id, mape])
                    fid += 1

# Delete old forecast file if it exists
old_file = os.path.join(DATA_DIR, 'forecast_results.csv')
if os.path.exists(old_file):
    os.remove(old_file)
    print("Deleted old forecast_results.csv")

print("Data generation completed successfully.")
