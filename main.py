import pandas as pd
import streamlit as st
from Review_Analyzer import *

st.header('Review Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        text = get_sentiment(text)
        st.write('Polarity: ', text[0])
        st.write('Subjectivity: ', text[1])
        st.write('Sentiment: ', text[2])

with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')
    if upl:
        file_format = st.selectbox('Select file format', ['csv', 'excel', 'parquet'])
        df = analyze_data(upl, file_format=file_format)
        st.write(df.head(10))

        @st.cache_data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        
        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )