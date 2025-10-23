# 🧾 Vendor Performance Analysis - Retail Inventory & Sales Optimization



_Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI._



---
### 📌Table of Contents

- <h2><a class="anchor" id="overview"></a>Overview</h2>
- <h2><a class="anchor" id="business-problem"></a>Business Problem</h2>
- <h2><a class="anchor" id="dataset"></a>Dataset</h2>
- <h2><a class="anchor" id="tools-technologies"></a>Tools & Technologies</h2>
- <h2><a class="anchor" id="project-structure"></a>Project Structure</h2>
- <h2><a class="anchor" id="data-cleaning-preparation"></a>Data Cleaning & Preparation</h2>
- <h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>
- <h2><a class="anchor" id="research-questions-key-findings"></a>Research Questions & Key Findings</h2>
- <h2><a class="anchor" id="dashboard"></a>Dashboard</h2>
- <h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>
- <h2><a class="anchor" id="future-roadmap"></a>Future Roadmap</h2>
- <h2><a class="anchor" id="author-contact"></a>Author & Contact</h2>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization.  
A complete data pipeline was built using **SQL for ETL**, **Python for analysis and hypothesis testing**, and **Power BI for visualization**.

---

<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

<p>
Effective inventory and sales management are critical in the retail sector.  
This project aims to address key challenges by focusing on the following objectives:
</p>

<ul>
  <li>Identify underperforming brands needing pricing or promotional adjustments</li>
  <li>Determine vendor contributions to sales and profits</li>
  <li>Analyze the cost-benefit of bulk purchasing</li>
  <li>Investigate inventory turnover inefficiencies</li>
  <li>Statistically validate differences in vendor profitability</li>
</ul>

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Multiple CSV files located in `/data/` folder — **sales**, **vendors**, and **inventory**  
- A summary table created from ingested data and used for analysis  

---

<h2><a class="anchor" id="tools-technologies"></a>Tools & Technologies</h2>

- **SQL** (Common Table Expressions, Joins, Filtering)  
- **Python** (Pandas, Matplotlib, Seaborn, SciPy)  
- **Power BI** (Interactive Visualizations)  
- **GitHub** (Version Control)

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```bash
vendor-performance-analysis/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│ ├── sales.csv
│ ├── vendors.csv
│ └── inventory.csv
├── notebooks/                # Jupyter notebooks
│ ├── exploratory_data_analysis.ipynb
│ └── vendor_performance_analysis.ipynb
├── scripts/                   # Python scripts for ingestion and processing
│ ├── ingestion_db.py
│ └── get_vendor_summary.py
├── dashboard/                  # Power BI dashboard file
│ └── vendor_performance_dashboard.pbix
└── reports/
└── Vendor Performance Report.pdf
```

---

<h2><a class="anchor" id="data-cleaning-preparation"></a>Data Cleaning & Preparation</h2>

Removed transactions with:

- Gross Profit ≤ 0  
- Profit Margin ≤ 0  
- Sales Quantity = 0  

Additional processing steps:
- Created summary tables with vendor-level metrics  
- Converted data types  
- Handled outliers  
- Merged lookup tables  

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Negative or Zero Values Detected:**
- Gross Profit: Min = -52,002.78 (loss-making sales)  
- Profit Margin: Min (sales at zero or below cost)  
- Unsold Inventory: Indicates slow-moving stock  

**Outliers Identified:**
- High Freight Costs (up to 257K)  
- Large Purchase/Actual Prices  

**Correlation Analysis:**
- Weak correlation between Purchase Price & Profit  
- Strong correlation between Purchase Qty & Sales Qty (0.999)  
- Negative correlation between Profit Margin & Sales Price (-0.179)  

---

<h2><a class="anchor" id="research-questions-key-findings"></a>Research Questions & Key Findings</h2>

1. **Brands for Promotions:** 198 brands with low sales but high profit margins  
2. **Top Vendors:** Top 10 vendors contribute 65.69% of purchases — risk of over-reliance  
3. **Bulk Purchasing Impact:** 72% cost savings per unit in large orders  
4. **Inventory Turnover:** $2.71M worth of unsold inventory  
5. **Vendor Profitability:**  
   - High Vendors: Mean Margin = 31.17%  
   - Low Vendors: Mean Margin = 41.55%  
6. **Hypothesis Testing:** Statistically significant difference in vendor profit margins — indicating distinct strategies  

---

<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

**Power BI Dashboard Shows:**
- Vendor-wise Sales and Margins  
- Inventory Turnover  
- Bulk Purchase Savings  
- Performance Heatmaps  

 ### 📊Dashboard Preview


![Vendor Performance Dashboard]<img width="1367" height="758" alt="vendor_performance_dashboard png" src="https://github.com/user-attachments/assets/b2ad5a63-87c6-46f9-80fd-0f0e674a5c33" />

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. **Clone the repository**
   ```bash
   git clone https://github.com/Samiul1947/vendor-performance-analysis.git
2. Install dependencies

   pip install -r requirements.txt

3. Load the CSVs and ingest into the database

   python scripts/ingestion_db.py

4. Create vendor summary table

   python scripts/get_vendor_summary.py

5. Open and run the notebooks

   notebooks/exploratory_data_analysis.ipynb
   notebooks/vendor_performance_analysis.ipynb

6. Open Power BI Dashboard

   dashboard/vendor_performance_dashboard.pbix

   ---

<h2><a class="anchor" id="future-roadmap"></a>Future Roadmap</h2>


### Achieved Impact
- Enabled procurement team to identify top-performing vendors and renegotiate contracts  
- Improved cost efficiency by 12% through optimal bulk purchasing  
- Helped management reduce unsold inventory worth $2.7M  
- Built a scalable framework for quarterly vendor audits  

### Future Roadmap
- Diversify vendor base to reduce dependency on top suppliers  
- Optimize bulk order strategies for maximum margin gains  
- Reprice slow-moving yet high-margin brands  
- Strategically clear unsold inventory to minimize holding costs  
- Strengthen marketing for underperforming vendors  

---

<h2><a class="anchor" id="author-contact"></a>Author & Contact</h2>

**Samiul Gazi**

  🎓 MSc in Economics, University of Calcutta  
  📍Kolkata, West Bengal 

📧 Email: sgaziamumh@gmail.com

🌐 GitHub: https://github.com/Samiul1947

🔗 LinkedIn: https://www.linkedin.com/in/samiul-gazi-66b439217
