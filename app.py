
import streamlit as st
import pandas as pd

st.title("🔍 Part Number Lookup App")

# Upload Excel file
uploaded_file = st.file_uploader("📤 Upload your Excel file", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.subheader("📑 Data Preview")
        st.dataframe(df.head())

        if 'Part Number' not in df.columns:
            st.error("❌ 'Part Number' column not found in the uploaded file.")
        else:
            part_number = st.text_input("🔎 Enter Part Number to Search")

            if part_number:
                filtered = df[df['Part Number'].astype(str).str.contains(part_number, case=False)]

                if not filtered.empty:
                    st.subheader("✅ Search Results")
                    st.dataframe(filtered)

                    csv = filtered.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="⬇️ Download results as CSV",
                        data=csv,
                        file_name='filtered_parts.csv',
                        mime='text/csv',
                    )
                else:
                    st.warning("⚠️ No matching part number found.")
    except Exception as e:
        st.error(f"❌ Error reading the Excel file: {e}")
else:
    st.info("📥 Please upload an Excel file to start.")
