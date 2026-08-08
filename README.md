# Customer Segmentation Analytics Dashboard

## 📌 Project Overview
The **Customer Segmentation Analytics Dashboard** is an end-to-end Business Intelligence solution built in Power BI to analyze customer purchasing behavior. Utilizing the **RFM (Recency, Frequency, Monetary)** framework combined with machine learning clustering models, this dashboard segments customers into actionable behavioral groups such as **VIP / High-Value** and **Loyal / Regular** customers.

The primary goal of this analytics dashboard is to help marketing and sales teams track core business KPIs, identify top-contributing customer tiers, and implement targeted retention and cross-selling strategies.

---

## 🛠️ Tech Stack & Key Technologies
* **Business Intelligence Tool:** Microsoft Power BI Desktop
* **Data Modeling & Analytics:** DAX (Data Analysis Expressions)
* **Data Preprocessing & ETL:** Power Query Editor
* **Segmentation Methodology:** RFM Analysis & K-Means Clustering

---

## 📈 Dashboard Architecture & Features

### 1. Key Performance Indicator (KPI) Banner
Located at the top of the dashboard for instant executive insights:
* **Total Customers:** Unique count of active customers across all segments.
* **Total Revenue:** Aggregate monetary value generated from customer transactions.
* **VIP Customers:** Dynamic count of high-value, high-frequency customers.
* **Regular Customers:** Dynamic count of active, core repeat buyers.

### 2. Primary Segment Distribution
* **Customer Distribution by Segment:** A clear visual breakdown displaying the exact split between VIP/High-Value and Loyal/Regular customer groups.

### 3. RFM Behavioral Deep-Dive (2x2 Grid)
* **Avg Spending by Segment:** Measures average monetary spend per segment to evaluate profitability.
* **Avg Frequency by Segment:** Compares average order count to identify high-engagement segments.
* **Avg Recency by Segment:** Tracks average days since the last transaction to highlight potential churn risks.
* **Total Revenue by Cluster:** Visualizes revenue distribution across cluster segments to measure group performance.

---

## ⚙️ Core DAX Measures

```dax
// 1. Total Unique Customer Count
Total Customers = 
DISTINCTCOUNT('final_customer_segments'[CustomerID])

// 2. Total Business Revenue
Total Revenue = 
SUM('final_customer_segments'[Monetary])

// 3. Dynamic VIP Customer Segmentation
VIP = 
CALCULATE(
    [Total Customers], 
    SEARCH("VIP", 'final_customer_segments'[Segment], 1, 0) > 0
)

// 4. Dynamic Regular/Loyal Customer Segmentation
Regular = 
CALCULATE(
    [Total Customers], 
    SEARCH("Loyal", 'final_customer_segments'[Segment], 1, 0) > 0
)

// 5. Average Recency (Days Since Last Purchase)
Avg Recency = 
AVERAGE('final_customer_segments'[Recency])

// 6. Average Order Frequency
Avg Frequency = 
AVERAGE('final_customer_segments'[Frequency])

// 7. Average Customer Spend
Avg Monetary = 
AVERAGE('final_customer_segments'[Monetary])
