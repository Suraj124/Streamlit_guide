import streamlit as st

st.title("Widget Guide")

################################# st.button() #######     https://docs.streamlit.io/library/api-reference/widgets/st.button
st.write(" ### 1.Working with buttons :")


if st.button(label="Click"):
	st.write("Hello")
else:
	st.write("Bye")


################################# st.text_input() ##### https://docs.streamlit.io/library/api-reference/widgets/st.text_input

st.write("## 2.Working with text input :")

name=st.text_input(label="Name",placeholder="Enter your Name")
st.write(name)
password=st.text_input(label="Password",type='password',placeholder="Enter your Password")
st.write(password)


################################# st.text_area() ###### https://docs.streamlit.io/library/api-reference/widgets/st.text_area

st.write("## 3.Working with text area :")

address=st.text_area(label="Address",placeholder="Enter you Adress here ... ")
st.write(address)

################################ st.date_input(),st.time_input() #### https://docs.streamlit.io/library/api-reference/widgets/st.date_input
import datetime
st.write("## 4.Working with date and time :")


dob = st.date_input(label="When is your birthday ?",value=datetime.date(1990,6,20))  # Retuns datetime.date object
st.write(f"Your Birthday is : {dob:%B-%m, %Y}")

alarm_time=st.time_input(label="Set an Alarm",value=datetime.time(5,0))  # Returns datetime.time object
st.write(f"Alarm is set for : {alarm_time}")

############################### st.checkbox() ##### https://docs.streamlit.io/library/api-reference/widgets/st.checkbox

st.write("## 5.Working with Checkbox :")

agree=st.checkbox(label="I agree")

if agree:
	st.write("Great!!!, Let's dive in")

tea=st.checkbox("Tea",value=True)   # Checkbox by default is selcted if value is True
coffee=st.checkbox("Coffee",False)

############################### st.radio() ### https://docs.streamlit.io/library/api-reference/widgets/st.radio

st.write("## 6.Working with Radio buttons :")

opt=["Tea",'Coffee','Milk']
drink=st.radio(label="What would you like to have ?",options=opt,index=1) # Returns the selected option

if drink==opt[0]:
	st.write(f"Thank you for purchasing : {drink}")
elif drink==opt[1]:
	st.write(f"Thank you for purchasing : {drink}")
else:
	st.write(f"Thank you for purchasing : {drink}")

############################## st.selectbox() ##### https://docs.streamlit.io/library/api-reference/widgets/st.selectbox

st.write("## 7.Working with select box :")

contact=st.selectbox(

	label="How would you like to be contacted ?",				# Returns the selected option
	options=["Email","Mobile Phone","Home Phone"],
	index=1

	)

st.write(f"You selected : {contact}")

############################## st.multiselect() ##### https://docs.streamlit.io/library/api-reference/widgets/st.multiselect

st.write("## 8.Working with Multi select options :")

colors=st.multiselect(    							# Retuns list with selcted options

	label="What are your favorite colors ?",
	options=["Green",'Yellow',"Red",'Blue','Yellow','Red','Black','Pink','Brwon','Gray'],
	default=['Blue','Black']

	)
st.write(f"You select the following color : {colors}")

############################ st.slider() #### 	https://docs.streamlit.io/library/api-reference/widgets/st.slider

st.write("## 9.Working with Slider :")

st.write("### Exaple - 1")
#Ex-1

age=st.slider(

	label="How old are you ?",
	min_value=0,
	max_value=130,
	value=18

	)
st.write(f"I'm {age} years old")

st.write("### Exaple - 2")
#Ex-2

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.write("### Exaple - 3")
#Ex-3

appointment=st.slider(

		"Schedule your appointment !!! ",
		value=(datetime.time(11,30),datetime.time(12,45))

	)

st.write(f"You are Schedule for : {appointment}")

st.write("### Exaple - 4")
# Ex-4

start_time=st.slider(

		"When do you start ?",
		value=datetime.datetime(2022,4,10,12,30),
		format="MM/DD/YY - hh:mm"

	)
st.write(f"Start time : {start_time}")

############################### st.number_input() ###https://docs.streamlit.io/library/api-reference/widgets/st.number_input

st.write("## 10.Working with Number input :")

age2=st.number_input(
		label="Enter you age",
		min_value=18,
		max_value=130,
		value=20
	)
st.write(f"Your age is  :  {age2}")

########################## st.file_uploader() #### https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader

st.write("## 11.Working with File Uploader:")

img=st.file_uploader(
		label="Upload you profile picture : ",
		type=None,   								# None -> all extenstions allowed
		accept_multiple_files=False
	)

if img is not None:
	st.image(img)