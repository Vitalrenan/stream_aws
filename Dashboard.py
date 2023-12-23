# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("streamlit-bkt-example/base_imoveis/batch_1_e2.parquet", input_format="parquet")

st.dataframe(df.head())

# Print results.
#for row in df.itertuples():
#    st.write(f"{row.Owner} has a :{row.Pet}:")