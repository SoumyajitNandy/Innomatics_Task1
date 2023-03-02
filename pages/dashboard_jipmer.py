import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "JIPMER.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "JIPMER.csv")

st.title("Dashboard - JIPMER Data")
st.header("This is Soumyajit's first :red[Innomatics] task")
st.subheader(":sunglasses: :sunglasses:")
img = image.imread(IMAGE_PATH)
st.image(img)

st.subheader("The dataframe of JIPMER is shown below:")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)



gen = st.selectbox("Select the gender:", df['sex'].unique())

col1= st.columns(1)

col1[0].subheader("Histogram of age based on gender")
fig_1 = px.histogram(df[df['sex'] == gen], x="age")
col1[0].plotly_chart(fig_1, use_container_width=True)

smoking = st.selectbox("Smoker or Non-smoker:", df['smoking'].unique())
alch= st.selectbox("alcoholic or Non-alcoholic:", df['alcoholic'].unique())

col2,col3= st.columns(2)

col2.subheader("Boxplot of BMI based on smoking and alcohol")
col3.subheader("Boxplot of SBP based on smoking and alcohol")
fig_2 = px.box(df[df['smoking']==smoking][df[df['smoking']==smoking]['alcoholic']==alch], y="BMI")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.box(df[df['smoking']==smoking][df[df['smoking']==smoking]['alcoholic']==alch], y="SBP")
col3.plotly_chart(fig_2, use_container_width=True)