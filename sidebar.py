import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

plt.style.use('ggplot')

data={
	
	"nums":[x for x in range(1,100)],
	"square":[x**2 for x in range(1,100)],
	"twice":[x*2 for x in range(1,100)],
	"thrice":[x*3 for x in range(1,100)]
}
x=np.arange(1,500)
data1={
	
	"nums":x,
	"square":np.power(x,2),
	"exp":np.exp(x),
	"log":np.log(x)
}

df=pd.DataFrame(data=data)

# col=st.sidebar.selectbox(label="Select a Number",options=df.columns)

# plt.plot(df['nums'],df[col])

# st.pyplot()


col=st.sidebar.multiselect(label="Select a Number",options=df.columns)

plt.plot(df['nums'],df[col])

st.pyplot()