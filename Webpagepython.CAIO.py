import streamlit as st
import pandas as pd
import openml
from datetime import datetime

from sklearn.datasets import fetch_openml

from sklearn.datasets import fetch_openml

# dataset = openml.dataset.get_database('iris)
# df = dataset.get_frame()
# st.datafram(df)

dataset = fetch_openml('iris')
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

with st.sidebar:
    st.image('./logo.png')
    st.title("AutoML")
    choice = st.radio("Navigation", ["Data Preprocessing", "Data Profilling", "CASH", "Download"])
    st.info("You can navigate through each of the sections")

st.write("this is an automated machine learning project")

if choice == "Data Preprocessing":
    st.write("this section is under development please make sure that the data is  preprocessed accordingly")
    st.info("Only preprocessed data can make good results")

    options = ["Upload your data", "Default Test data"]
    input = st.selectbox("Select your Data loading methods", options)

    if input == "Upload your data":
        uploaded_file = st.file_uploader("Upload Data")

        if uploaded_file is not None:
            st.write ("Processing uploaded file")
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
    if input == "Default Test data":
        from sklearn.datasets import fetch_openml
        # dataset = openml.dataset.get_database('iris)
        # df = dataset.get_frame()
        #st.datafram(df)

        dataset = fetch_openml('iris')
        df = pd.DataFrame(data =dataset.data, columns=dataset.feature_names)
        df['target']=dataset.target
        st.dataframe(df)
        pass


if choice == "Data Profilling":
    import pandas_profiling
    from streamlit_pandas_profiling import st_profile_report
    st.title("Exploratory data analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)
    pass
if choice == "CASH":
    st.checkbox("Yes")
    st.checkbox("No")
    st.button("Submit")
    st.multiselect("Favorite food",["burguer","pizza","icecream"] )
    st.select_slider("rate the movie", ["good","average", "bad"])
    st.slider("choose a number", 0,50)

    st.number_input("enter your age", 0,120)
    st.text_input("enter your name")
    min_date=datetime(1920,1,1)
    max_date=datetime(2030,1,1)
    st.date_input("choose your DOB",min_value =min_date,max_value=max_date )
    st.time_input("when should we stop the class")
    st.text_area("how do you fell today")
    st.color_picker("choose your favorite color")
    pass
if choice == "Download":
    name = st.text_input("enter your name")
    food = st.selectbox("Chosse your Favorite food",["burguer","pizza","icecream"])

    if food== "burguer":
        st.write("Thank you for choosing burguer")
        st.image('https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/cf29c385555335.5d7fb3c164383.jpg')


    pass
