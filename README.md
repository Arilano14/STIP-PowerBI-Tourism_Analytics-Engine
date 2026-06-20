# Smart Tourism Intelligence Platform (STIP)

**A Research-Oriented Business Intelligence Architecture for Tourism Performance Monitoring, Competitiveness Benchmarking, and Policy-Oriented Decision Support.**

## 📌 Project Overview

Smart Tourism Intelligence Platform (STIP) is a research-oriented Business Intelligence project developed using Power BI to support tourism performance monitoring, demand forecasting, competitiveness benchmarking, and policy-oriented decision support across ASEAN countries.

This project was designed as an academic and professional portfolio demonstrating end-to-end Business Intelligence capabilities, including data modeling, semantic layer development, KPI engineering, forecasting integration, metadata governance, and dashboard deployment.

---

## Objectives

The project aims to:

* Monitor tourism performance across ASEAN countries.
* Analyze economic and environmental drivers affecting tourism demand.
* Evaluate tourism recovery after COVID-19.
* Compare tourism competitiveness among countries.
* Provide decision-support recommendations through data-driven insights.
* Demonstrate Business Intelligence architecture and governance best practices.

---

## Geographic Scope

Countries included:

* Indonesia
* Thailand
* Malaysia
* Singapore
* Vietnam

Period:

* 2015–2025
* Monthly granularity

---

## Business Intelligence Architecture

Data Sources
→ Power Query (ETL)
→ Data Quality Framework
→ Star Schema
→ Semantic Layer (DAX)
→ Analytics Mart
→ Research Layer
→ Power BI Service
→ Embedded Dashboard

---

## Core Components

### Data Model

Dimension Tables

* dim_country
* dim_date

Fact Tables

* fact_tourism
* fact_economy
* fact_weather
* fact_exchange
* forecast_results

---

### Semantic Layer

Core KPIs:

* Total Arrivals
* Total Revenue
* Revenue Per Tourist
* Tourism Contribution to GDP
* Arrival Growth Rate
* Revenue Growth Rate
* Recovery Index
* Tourism Competitiveness Score (TCS)

---

### Analytics Marts

#### mart_tourism_country_month

Integrated analytical dataset for dashboard consumption.

#### mart_insight

Automatically generated analytical insights.

#### mart_research_findings

Research-oriented findings and evidence metrics.

---

## Dashboard Structure

### Page 1 – Executive Overview

Answers:

"What happened?"

Features:

* KPI Cards
* Monthly Trends
* ASEAN Map
* Top and Bottom Country Rankings

---

### Page 2 – Tourism Demand Analysis

Answers:

"Where and how is demand changing?"

Features:

* Trend Analysis
* Seasonality Analysis
* Growth Ranking
* Country Comparison

---

### Page 3 – Economic & Weather Drivers

Answers:

"Why did it happen?"

Features:

* GDP Analysis
* Inflation Analysis
* Exchange Rate Analysis
* Weather Impact Analysis
* Correlation Matrix

---

### Page 4 – Forecasting

Answers:

"What will happen?"

Features:

* Actual vs Forecast
* Forecast Growth
* Model Comparison
* MAPE Evaluation

---

### Page 5 – Competitiveness & Recommendations

Answers:

"What should we do?"

Features:

* Tourism Competitiveness Score
* Radar Analysis
* Opportunity Assessment
* Strategic Recommendations

---

## Metadata & Web Integration Layer

To support future web integration, the project includes:

* metadata_kpi_catalog
* metadata_data_source
* metadata_web_config
* metadata_embed
* metadata_navigation
* metadata_access_control
* metadata_research_question
* metadata_expected_findings

These metadata tables enable frontend developers to consume dashboard outputs without accessing internal Power BI logic.

---

## Technology Stack

* Power BI Desktop
* Power Query
* DAX
* Power BI Service
* CSV Datasets
* Star Schema Data Modeling

---



