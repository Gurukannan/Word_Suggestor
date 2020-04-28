import streamlit as st 
import enchant

message = st.text_area("Enter Text","Type Here ..")
if st.button("Analyze"):
# Using 'en_US' dictionary 
	d = enchant.Dict("en_US") 
	word = message
	d.check(word)
	df=d.suggest(word)
	st.json(df)