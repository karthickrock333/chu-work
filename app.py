# Save this as app.py
import pandas as pd
import streamlit as st
from io import BytesIO

st.title("📊 Product Summary App")

uploaded_file = st.file_uploader("📁 Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    grouped = df.groupby('Product Name').agg({
        'Freequantity': 'sum',
        'Purchase Price': 'first'
    }).reset_index()
    grouped['Total'] = grouped['Freequantity'] * grouped['Purchase Price']

    output = BytesIO()
    grouped.to_excel(output, index=False)
    output.seek(0)

    st.success("✅ File processed successfully!")
    st.download_button(
        label="⬇️ Download Result File",
        data=output,
        file_name="grouped_product_summary.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
