# 📊 Superstore Data Cleaning & Transformation Project

## 📌 Project Overview
This project focuses on data immersion, cleaning, and transformation of the Superstore Retail Sales dataset using Python. 

The objective was to convert raw transactional retail data into a clean, structured, and analysis-ready dataset suitable for exploratory data analysis (EDA), visualization, and business intelligence reporting.

The final cleaned dataset is saved as:
cleaned_superstore.csv

---

## 📂 Dataset Summary
- 9,800+ transaction records
- 18 original features
- Transaction-level retail sales data
- Geographic coverage: United States
- Entities: Customers, Orders, Products, Regions, Sales

Each row represents a product within an order. A single Order ID may contain multiple products.

---

## 🔎 Data Cleaning Process

### 1. Data Exploration
- Reviewed dataset structure and dimensions
- Checked column names and data types
- Generated descriptive statistics
- Analyzed unique values across categorical columns

### 2. Data Quality Assessment
- Handled missing values in Postal Code
- Checked and verified duplicate records
- Converted Order Date and Ship Date to proper datetime format
- Standardized text formatting for City and State columns
- Validated high-value sales as legitimate transactions (no incorrect outliers removed)

---

## 🔄 Data Transformation & Feature Engineering

### Removed Column
- Row ID (non-analytical identifier)

### Standardization
- Rounded Sales values to two decimal places

### New Features Created
- Shipping Days → Calculated delivery time (Ship Date - Order Date)
- Order Year → Extracted from Order Date for yearly trend analysis
- Order Month → Extracted for seasonal analysis
- Sales Category:
  - LOW (Sales < 50)
  - MEDIUM (50 ≤ Sales < 200)
  - HIGH (Sales ≥ 200)

---

## 📈 Business Use Cases
The cleaned dataset enables:
- Revenue trend analysis
- Regional performance comparison
- Customer segmentation
- Shipping efficiency evaluation
- Business dashboard development

---

## 🛠 Tools & Technologies
- Python
- Pandas
- NumPy
- Jupyter Notebook

---

## ✅ Final Output
A fully cleaned and transformed dataset ready for advanced analysis and reporting.
