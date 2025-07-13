import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px

st.set_page_config(page_title="SEBI Orders Dashboard", layout="wide")

# Load data from Snowflake
@st.cache_data(ttl=600)
def load_data():
    conn = snowflake.connector.connect(
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"],
        role=st.secrets["snowflake"]["role"]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM WCC_SEBI_ORDERS_SENTIMENT")
    df = cursor.fetch_pandas_all()
    cursor.close()
    conn.close()
    return df

df = load_data()

# Title and summary
st.title("📄 SEBI Enforcement Orders Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", len(df))
col2.metric("Negative", df[df["SENTIMENT"] == "NEGATIVE"].shape[0])
col3.metric("Neutral", df[df["SENTIMENT"] == "NEUTRAL"].shape[0])
col4.metric("General", df[df["SENTIMENT"] == "GENERAL"].shape[0])

# 🧠 Sentiment Distribution Pie Chart
st.subheader("🧠 Sentiment Distribution")
sentiment_counts = df["SENTIMENT"].value_counts().reset_index()
sentiment_counts.columns = ["SENTIMENT", "COUNT"]
fig = px.pie(sentiment_counts, values="COUNT", names="SENTIMENT", title="Sentiment Distribution", hole=0.4)
st.plotly_chart(fig, use_container_width=True)

# Sentiment selector
sentiment_choice = st.radio("📊 Filter by Sentiment", ["NEGATIVE", "NEUTRAL", "GENERAL", "UNKNOWN"])
filtered_df = df[df["SENTIMENT"] == sentiment_choice]

st.write(f"### Showing {len(filtered_df)} orders labeled as **{sentiment_choice}**")

# Show orders table
st.dataframe(
    filtered_df[["ORDER_DATE", "TITLE", "CATEGORY", "PDF_LINK"]],
    use_container_width=True,
)

# Add PDF download links
for idx, row in filtered_df.iterrows():
    st.markdown(f"🔗 [{row['TITLE']}]({row['PDF_LINK']})")

# CSV Export
csv = filtered_df.to_csv(index=False)
st.download_button("📥 Download Filtered Orders as CSV", csv, file_name="filtered_orders.csv")
