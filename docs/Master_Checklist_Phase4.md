# STIP - Master Checklist (Phase 4: Power Query & ETL)

This document outlines the strict exit criteria and requirements for Phase 4 (ETL Layer) of the Smart Tourism Intelligence Platform (STIP), establishing it as a 9.8/10 Master's level Business Intelligence Portfolio.

---

## Tujuan Phase
Membangun **ETL Layer** yang:
* bersih (clean)
* konsisten (consistent)
* dapat direproduksi (reproducible)
* siap untuk Semantic Layer (Phase 5)
* siap untuk Power BI Service (Phase 9)
* siap diganti dari Dummy CSV menjadi API/Database pada masa depan.

**Alur Data:**
CSV/API ➔ Power Query ➔ Clean Dataset ➔ Star Schema ➔ Ready for DAX

---

## OUTPUT PHASE 4
- [ ] Power Query Documentation
- [ ] Data Quality Report
- [ ] ETL Flow Diagram
- [ ] Clean Fact Tables
- [ ] Clean Dimension Tables
- [ ] Parameter Tables
- [ ] Data Validation Rules
- [ ] Refresh Ready Dataset
- [ ] Publish Ready PBIX

---

## A. DATA INGESTION
**Goal:** Mengimpor seluruh dataset tanpa error.

### Source Folder
- `C:\Users\Arilano\Downloads\Project ARICE\Project Tourism\data\`

### Import Dataset
- **Dimensions:** `dim_country.csv`, `dim_date.csv`, `dim_year.csv`, `dim_model.csv`
- **Facts:** `fact_tourism_monthly.csv`, `fact_weather_monthly.csv`, `fact_exchange_rate_monthly.csv`, `fact_economy_yearly.csv`, `fact_forecast_monthly.csv`
- **Metadata Tables:** `metadata_kpi_catalog.csv`, `metadata_data_source.csv`, `metadata_navigation.csv`, `metadata_embed.csv`, `metadata_access_control.csv`, `metadata_research_question.csv`, `metadata_expected_findings.csv`

### Power Query Naming Convention
- `pq_dim_country`, `pq_dim_date`, `pq_dim_year`, `pq_dim_model`
- `pq_fact_tourism`, `pq_fact_weather`, `pq_fact_exchange`, `pq_fact_economy`, `pq_fact_forecast`

**Exit Criteria:** 0 import errors

---

## B. DATA TYPE STANDARDIZATION
**Goal:** Memastikan tipe data presisi (Whole Number, Decimal, Text, Date).
**Exit Criteria:** 100% datatype correct across all imported files.

---

## C. DATA QUALITY FRAMEWORK
**Goal:** Dataset memenuhi standar kualitas enterprise.

- [ ] **Completeness:** >95% (Null/Missing values report, Column profiling enabled)
- [ ] **Validity:** `tourist_arrivals >=0`, `gdp_usd >=0`, `rainfall_mm >=0`, `population >=0`
- [ ] **Consistency:** Standardized Country names, Date format, Currency code.
- [ ] **Duplicate:** 0 (No duplicate PK, No duplicate Country-Month combination, No duplicate Forecast rows).
- [ ] **Freshness:** Dataset version & last refresh documented.

**Exit Criteria:** 0 critical data quality issues.

---

## D. DATA CLEANING
**Goal:** Menghasilkan clean dataset.
- [ ] Trim whitespace
- [ ] Remove empty rows
- [ ] Remove duplicates
- [ ] Remove invalid records
- [ ] Replace null values
- [ ] Standardize text casing, date format, decimal separator

**Exit Criteria:** 100% clean tables.

---

## E. BUSINESS RULE VALIDATION
- **Tourism:** arrivals cannot be negative, occupancy between 0 and 100, average stay >0
- **Economy:** inflation >-100%, population >0
- **Weather:** humidity between 0 and 100, rainfall >=0
- **Forecast:** MAPE between 0 and 100, growth between -100% and 500%

**Exit Criteria:** 0 business rule violations.

---

## F. POWER QUERY PARAMETERS
**Goal:** Membuat ETL reusable.
- **Current Parameters:** `pDataFolder`, `pRefreshDate`, `pEnvironment` (Values: DEV, TEST, PROD)
- **Future Parameters:** `pAPIWorldBank`, `pAPIOpenMeteo`, `pAPIFrankfurter`

**Exit Criteria:** 100% parameterized source path.

---

## G. POWER QUERY FUNCTION
**Goal:** Reusable ETL logic.
- Functions to create: `fnCleanText`, `fnRemoveDuplicates`, `fnValidateCountry`, `fnValidateDate`, `fnDataQualityScore`

**Exit Criteria:** Minimum 5 reusable functions.

---

## H. QUERY DEPENDENCY DOCUMENTATION
- [ ] Query Dependency View created.
- [ ] ETL Flow Diagram exported to `docs/ETL_Flow.png`

---

## I. PERFORMANCE OPTIMIZATION
- [ ] Remove unnecessary columns
- [ ] Disable load staging queries
- [ ] Remove intermediate queries
- [ ] Use correct datatypes
- [ ] Avoid duplicate transformations

**Performance Target:** Dataset refresh <30 seconds. PBIX size <25 MB.

---

## J. REFRESH STRATEGY
- **MVP:** Manual Refresh
- **Future:** Scheduled Refresh
- **Documentation:** Refresh Plan, Data Source Mapping

---

## K. FUTURE CONNECTIVITY (PORTFOLIO VALUE)
- **Database Ready:** PostgreSQL schema, SQL migration, Connection string template documented.
- **Odoo Ready:** Odoo connector architecture, REST API endpoints, PostgreSQL mapping, ERP integration roadmap documented.
- **API Ready:** World Bank, Open Meteo, Frankfurter mapping.

---

## L. CODING STANDARDS
- **Naming:** `pq_`, `stg_`, `fn_`, `dim_`, `fact_`, `metadata_`
- **Folder Structure:** `queries/` ➔ `staging`, `dimensions`, `facts`, `metadata`, `functions`, `marts`

---

## M. DELIVERABLES
- [ ] PowerQueryDocumentation.pdf
- [ ] DataQualityReport.pdf
- [ ] ETL_Flow.png
- [ ] QueryDependency.png
- [ ] RefreshPlan.pdf
- [ ] SourceMapping.xlsx

---

**PHASE 4 EXIT CRITERIA MET WHEN:**
Semua CSV berhasil di-load, semua datatype benar, tidak ada duplicate/null critical, business rule valid, ETL terdokumentasi, dataset refresh <30 detik, PBIX <25 MB, parameterized source path, Future API/Database/Odoo roadmap ready, dan publish ready.
