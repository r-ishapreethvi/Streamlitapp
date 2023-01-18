import streamlit as st
import pandas as pd


source = st.file_uploader("Upload Source Database containing 100 sourcesites ", type="xlsx")
gis = st.file_uploader("Upload GIS Database", type="xlsx")
if st.button('go!'):
   df0 = pd.read_excel(source)
   df2 = pd.read_excel(gis)

   st.dataframe(df0)
   st.dataframe(df2)

   # st.write(df1)
   df3 = pd.DataFrame()

   df3['source_name'] = df0['       name']
   dfslat = dict(zip(df2['cell'], df2['latitude']))
   df3['source_latitude'] = df3['source_name'].map(dfslat)

   st.write(df3)

else:
   st.warning("you need to upload an excel of format xlsx!")