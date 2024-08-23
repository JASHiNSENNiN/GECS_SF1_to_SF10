import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

st.set_page_config(page_title="Guimba East Central School", layout="wide")

df = pd.read_excel("SF1.xls")

lrn_search = st.text_input("Search by LRN")

name_search = st.text_input("Search by Name (Last, First, Middle)")


AgGrid(df)