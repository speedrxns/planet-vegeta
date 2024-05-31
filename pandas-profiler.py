import streamlit as st
import pandas as pd
import snowflake.connector
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Streamlit page configuration
st.set_page_config(page_title='Snowflake Data Explorer', layout='wide')

# UI for username and password
st.sidebar.title("Snowflake Credentials")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Function to connect to Snowflake
def get_snowflake_connection(user, passwd):
    return snowflake.connector.connect(
        user=user,
        password=passwd,
        account='YOUR_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )

# Function to fetch data and handle datatype conversions
def fetch_data(query, user, passwd):
    conn = get_snowflake_connection(user, passwd)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        df = cursor.fetch_pandas_all()
        
        # Display data types before conversion
        with st.expander("Data Types Before Conversion"):
            st.dataframe(df.dtypes.astype(str))
        
        # Dynamic conversion of date columns if pandas does not recognize 'date'
        conversion_summary = {}
        for column in df.columns:
            if pd.api.types.is_object_dtype(df[column]):
                try:
                    converted = pd.to_datetime(df[column], errors='coerce')
                    if not pd.isnull(converted).all():  # Successful conversion of at least some entries
                        df[column] = converted
                        conversion_summary[column] = "Converted to datetime 🟢"
                except Exception as e:
                    conversion_summary[column] = f"Failed to convert: {str(e)} 🔴"

        # Convert decimal/numeric columns to float for better handling in pandas
        for column in df.select_dtypes(include=['number']).columns:
            df[column] = df[column].astype(float)
            conversion_summary[column] = f"Converted to float 🟢"
        
        if conversion_summary:
            with st.expander("Conversion Summary"):
                st.json(conversion_summary)

    finally:
        cursor.close()
        conn.close()
    
    return df

# Streamlit UI for query input
st.title('Snowflake Data Explorer')
query = st.text_area("Enter your SQL query here:", height=150)
if st.button('Run Query'):
    if not username or not password:
        st.error("Please enter both username and password.")
    else:
        with st.spinner('Fetching data from Snowflake...'):
            try:
                df = fetch_data(query, username, password)
                if not df.empty:
                    st.success('Data fetched successfully! 🎉')
                    with st.expander("View Data"):
                        st.dataframe(df)
                    # Generating the profile report
                    with st.spinner('Generating profile report...'):
                        profile = ProfileReport(df, explorative=True)
                        st_profile_report(profile)
                else:
                    st.warning('No data returned from the query.')
            except Exception as e:
                st.error(f'Failed to fetch data: {str(e)}')
