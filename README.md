# 📊 Superstore Sales & Profit Dashboard — Streamlit

An interactive **Streamlit dashboard** for analyzing Superstore sales, profit, customers, products, regions, categories, discounts, and returns.

The application loads the Superstore Excel workbook, combines the **Orders, People, and Returns** sheets, applies interactive filters, calculates KPIs, and presents the analysis through interactive Plotly visualizations.

## 🛠️ Tools Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)

## 🎯 Project Objective

The goal of this project is to build a practical, interactive analytics application that makes Superstore business data easier to explore.

The dashboard can be used to investigate:

- Sales and profit performance
- Profit margin
- Order volume
- Return rate
- Monthly sales and profit trends
- Sales by category
- Regional performance
- Profit by sub-category
- Top customers by sales
- Discount versus profit relationships

## 📸 Dashboard Preview

![Superstore Streamlit Dashboard](Screenshot%202026-09-21%20150711.png)

## 🔎 Dashboard Features

### Interactive Filters

The sidebar provides filters for:

- Order date range
- Region
- Category
- Segment

All charts and KPIs update according to the selected filters.

### KPI Cards

The dashboard displays:

- **Total Sales**
- **Total Profit**
- **Profit Margin**
- **Orders**
- **Return Rate**

### Visual Analysis

The application includes interactive Plotly charts for:

- Monthly Sales & Profit Trend
- Sales by Category
- Sales & Profit by Region
- Profit by Sub-Category
- Top 10 Customers by Sales
- Discount vs Profit

### Filtered Data Export

Users can expand the raw-data section to:

- View the filtered dataset
- Download the filtered data as a CSV file

## 📂 Project Structure

```text
Streamlit-Dashboard/
│
├── app.py
├── requirements.txt
├── sample_-_superstore.xls
├── Screenshot 2026-09-21 150711.png
└── README.md
```

### Files

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit application |
| `sample_-_superstore.xls` | Superstore source dataset |
| `requirements.txt` | Python dependencies |
| `Screenshot 2026-09-21 150711.png` | Dashboard preview |
| `README.md` | Project documentation |

## ⚙️ Data Processing

The application:

1. Loads the **Orders**, **People**, and **Returns** sheets from the Excel workbook.
2. Converts order and ship dates to datetime format.
3. Merges regional manager information from the People sheet.
4. Merges return information from the Returns sheet.
5. Creates a `Returned` flag for orders without a return record.
6. Applies the selected dashboard filters.
7. Calculates KPIs and generates interactive visualizations.

## ▶️ Run the Project Locally

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 📊 Skills Demonstrated

- Python data analysis
- Pandas data transformation
- Excel data handling
- Data merging
- KPI calculation
- Interactive dashboard development
- Plotly data visualization
- Streamlit application development
- Business-oriented data analysis
- CSV data export

## 👨‍💻 Author

**Yash Sharma**

BCA Graduate | Aspiring Data Analyst

**Skills:** Python | SQL | Excel | Power BI | Tableau | Data Analysis

