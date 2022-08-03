import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
st.set_option('deprecation.showPyplotGlobalUse', False)

data=pd.read_csv("Data/Salary_Data.csv") 

lr=LinearRegression()
x=np.array(data['YearsExperience']).reshape(-1,1)
y=np.array(data['Salary'])
lr.fit(x,y)



st.title("Salary Prediction")


nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])

if nav == "Home":
	st.image("Data/sal.jpg",width=800)

	if st.checkbox("Show Table"):
		st.table(data)

	graph = st.selectbox("What kind of Graph ?",["Non-Interactive","Interactive"])

	val=st.slider("Filter data using slider",0,20)
	data=data.loc[data['YearsExperience']>=val]

	if graph == "Non-Interactive":
		plt.figure(figsize=(10,5))
		plt.scatter(data['YearsExperience'],data['Salary'])
		plt.ylim(0)
		plt.xlabel("Years of Experience")
		plt.ylabel("Salary")
		plt.tight_layout()
		st.pyplot()
	if graph == "Interactive":
		layout=go.Layout(
				xaxis=dict(range=[0,16]),
				yaxis=dict(range=[0,210000])
			)
		fig=go.Figure(data=go.Scatter(x=data['YearsExperience'],y=data['Salary'],mode='markers'),
				layout=layout
			)
		st.plotly_chart(fig)


if nav == "Prediction":
	st.subheader("Know you Salary !!!")
	val=st.number_input("Enter your Experience : ",0.00,20.00,0.25)

	val=np.array(val).reshape(1,-1)
	pred=lr.predict(val)[0]

	if st.button("Predict"):
		st.success(f"Your predicted salary is :  {np.around(pred,2)}")


if nav == "Contribute":
	st.subheader("Contribute to our dataset : ")

	ex=st.number_input("Enter your Experience",0.0,20.0)
	sal=st.number_input("Enter your salary",0.00,1000000.00,step=1000.0)

	if st.button("Submit"):
		to_add={'YearsExperience':[ex],'Salary':[sal]}
		to_add=pd.DataFrame(to_add)

		to_add.to_csv("Data/Salary_Data.csv",mode='a',index=False,header=False)
		st.success("Information added successfully !!!")

