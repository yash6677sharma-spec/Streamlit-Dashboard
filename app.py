import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="Superstore Dashboard", layout="wide")

# ---------------------------------------------------------
# DATA LOADING (cached so it doesn't reload on every interaction)
# ---------------------------------------------------------
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "sample_-_superstore.xls")

@st.cache_data
def load_data():
    orders = pd.read_excel(DATA_PATH, sheet_name="Orders")
    people = pd.read_excel(DATA_PATH, sheet_name="People")
    returns = pd.read_excel(DATA_PATH, sheet_name="Returns")

    orders["Order Date"] = pd.to_datetime(orders["Order Date"])
    orders["Ship Date"] = pd.to_datetime(orders["Ship Date"])

    # Merge regional manager + returned flag onto orders
    df = orders.merge(people, on="Region", how="left")
    df = df.merge(returns, on="Order ID", how="left")
    df["Returned"] = df["Returned"].fillna("No")

    return df

df = load_data()

# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------
st.sidebar.header("Filters")

min_date, max_date = df["Order Date"].min(), df["Order Date"].max()
date_range = st.sidebar.date_input(
    "Order Date range", value=(min_date, max_date),
    min_value=min_date, max_value=max_date
)

region = st.sidebar.multiselect(
    "Region", options=sorted(df["Region"].unique()), default=None
)
category = st.sidebar.multiselect(
    "Category", options=sorted(df["Category"].unique()), default=None
)
segment = st.sidebar.multiselect(
    "Segment", options=sorted(df["Segment"].unique()), default=None
)

# Apply filters
f = df.copy()
if len(date_range) == 2:
    f = f[(f["Order Date"] >= pd.to_datetime(date_range[0])) &
          (f["Order Date"] <= pd.to_datetime(date_range[1]))]
if region:
    f = f[f["Region"].isin(region)]
if category:
    f = f[f["Category"].isin(category)]
if segment:
    f = f[f["Segment"].isin(segment)]

# ---------------------------------------------------------
# TITLE + KPIs
# ---------------------------------------------------------
st.title("📊 Superstore Sales & Profit Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Sales", f"${f['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${f['Profit'].sum():,.0f}")
margin = (f["Profit"].sum() / f["Sales"].sum() * 100) if f["Sales"].sum() else 0
col3.metric("Profit Margin", f"{margin:.1f}%")
col4.metric("Orders", f"{f['Order ID'].nunique():,}")
return_rate = (f["Returned"].eq("Yes").sum() / f["Order ID"].nunique() * 100) if f["Order ID"].nunique() else 0
col5.metric("Return Rate", f"{return_rate:.1f}%")

st.divider()

# ---------------------------------------------------------
# ROW 1: Sales trend + Category breakdown
# ---------------------------------------------------------
c1, c2 = st.columns((2, 1))

with c1:
    monthly = f.set_index("Order Date").resample("ME")[["Sales", "Profit"]].sum().reset_index()
    fig = px.line(monthly, x="Order Date", y=["Sales", "Profit"],
                  title="Monthly Sales & Profit Trend", markers=True)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    cat = f.groupby("Category")[["Sales"]].sum().reset_index()
    fig = px.pie(cat, names="Category", values="Sales", title="Sales by Category", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# ROW 2: Region performance + Sub-category profit
# ---------------------------------------------------------
c3, c4 = st.columns(2)

with c3:
    reg = f.groupby("Region")[["Sales", "Profit"]].sum().reset_index()
    fig = px.bar(reg, x="Region", y=["Sales", "Profit"], barmode="group",
                 title="Sales & Profit by Region")
    st.plotly_chart(fig, use_container_width=True)

with c4:
    sub = f.groupby("Sub-Category")[["Profit"]].sum().reset_index().sort_values("Profit")
    fig = px.bar(sub, x="Profit", y="Sub-Category", orientation="h",
                 title="Profit by Sub-Category",
                 color="Profit", color_continuous_scale=["red", "green"])
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# ROW 3: Top customers + Discount vs Profit
# ---------------------------------------------------------
c5, c6 = st.columns(2)

with c5:
    top_cust = f.groupby("Customer Name")[["Sales"]].sum().nlargest(10, "Sales").reset_index()
    fig = px.bar(top_cust, x="Sales", y="Customer Name", orientation="h",
                 title="Top 10 Customers by Sales")
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

with c6:
    fig = px.scatter(f, x="Discount", y="Profit", color="Category",
                      title="Discount vs Profit", opacity=0.6,
                      hover_data=["Product Name"])
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# RAW DATA TABLE
# ---------------------------------------------------------
st.divider()
with st.expander("🔍 View filtered raw data"):
    st.dataframe(f, use_container_width=True)
    st.download_button(
        "Download filtered data as CSV",
        f.to_csv(index=False).encode("utf-8"),
        "filtered_superstore_data.csv",
        "text/csv"
    )
