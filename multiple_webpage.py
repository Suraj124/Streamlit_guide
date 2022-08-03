import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
st.set_option('deprecation.showPyplotGlobalUse', False)

plt.style.use('ggplot')

data={
	
	"nums":[x for x in range(1,100)],
	"square":[x**2 for x in range(1,100)],
	"twice":[x*2 for x in range(1,100)],
	"thrice":[x*3 for x in range(1,100)]
}
df=pd.DataFrame(data=data)

rad = st.sidebar.radio(label="Navigation",options=['Home','About Us'])

if rad=="Home":

	col=st.sidebar.multiselect(label="Select a Number",options=df.columns)

	plt.plot(df['nums'],df[col])

	st.pyplot()
if rad=="About Us":
	st.write("This is About us page !!! :smile:")

	my_progress_bar=st.progress(0)

	for percentage in range(100):
		time.sleep(0.1)
		my_progress_bar.progress(percentage+1)

	st.balloons()

	st.error("This is an Error")
	st.success("This is sucess message")
	st.info("This is purely information box")
	st.exception(RuntimeError("This is an exception of type : RUntimeError !!!"))
	st.warning("This is warning !!!")