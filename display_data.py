import streamlit as st
import numpy as np
import pandas as pd
import time

arr=np.arange(1,10)
mat=arr.reshape((3,3))

d={
	"Name":["Bob","Jasper"],
	"Age":[20,15],
	"Gender":["Male","Male"]
}


df=pd.read_csv("Data/employer-default-indicator.csv")

#Displaying data with st.dataframe()
st.write("#### Using st.dataframe()")

st.dataframe(arr)
st.dataframe(mat)
st.dataframe(d)
st.dataframe(df,width=300,height=600)

# Displaying data with st.table(): Use st.table if your table is small
st.write("#### Using st.table()")

st.table(df)
st.table(arr)
st.table(d)

# using json
st.write("#### Using st.json()")

st.json(d)

# Using write
st.write("#### Using st.write()")

st.write(arr)
st.write(d)
st.write(df)


####################### Caching #############################

@st.cache
def ret_time():
	time.sleep(5)
	return time.time()

if st.checkbox("1"):
	st.write(ret_time())
if st.checkbox("2"):
	st.write(ret_time())