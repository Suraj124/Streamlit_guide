import streamlit as st  # Import streamlit library

st.title("Hello STramlit")

st.header("header")

st.subheader("Sub header")

st.text("This is a text !!! ")

st.markdown("""
	# h1 tag
	## h2 tag
	### h3 tag

	:heart:
	:moon:<br>
	:sunglasses: <br>

	**This is bold**
	_This is Italic_

	""",True)

st.latex(r'''

			\frac{1}{n} \sum \limits _{i=1} ^{n} x_{i}   # https://katex.org/docs/supported.html

	''')