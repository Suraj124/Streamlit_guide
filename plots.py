import streamlit as st
import numpy as np
import pandas as pd

data=pd.DataFrame(
		data=np.random.randn(100,3),
		columns="a b c".split()
	)

st.dataframe(data)

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

################ Using Matplotlib ################
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


plt.scatter(data['a'],data['b'])
plt.title("scatter plot")
plt.xlabel("Price")
plt.ylabel("Product")

st.pyplot()

############ Using Altair ########
st.write(" #### Using altair")
import altair as alt

chart = alt.Chart(data).mark_circle().encode(

				x='a' , y='b' , tooltip=['a','b']
	)

st.altair_chart(chart,use_container_width = True)


######### Digraph #########

st.graphviz_chart("""

	digraph{

		Eat->Sleep
		Sleep->Code
		Code->Eat

	}

	""")

######## Map #########
st.write(" # Map ")

city=pd.DataFrame({

		'city':['Lucknow','Noida'],
		'lat':[26.8467,28.5355],
		'lon':[80.9462,77.3910]

	})

st.map(city)

######### Add Image #####  https://docs.streamlit.io/library/api-reference/media/st.image

st.write(" # Adding Image")

st.image(["img/python.png","img/Guido.jpg"],width=400,caption=['Python logo','Python developer'])

######## Add Audio #####   https://docs.streamlit.io/library/api-reference/media/st.audio

st.audio(data="Data/demo.wav", format="audio/wav", start_time=0) 

####### Add Video #####    https://docs.streamlit.io/library/api-reference/media/st.video

st.write(" # Adding Video")

st.video(data="Data/star.mp4", format="video/mp4", start_time=0)

# we can also embed you tube link

st.video("https://www.youtube.com/watch?v=jq0lKFb-P8k&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=4")



