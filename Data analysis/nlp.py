import streamlit as st
from textblob import TextBlob

# streamlit run nlp.py
st.sidebar.title('NLP using TextBlob')
# streamlit run c:/Users/KumarCha05/Documents/GitHub/Python-Basic/Data analysis/nlp.py [ARGUMENTS]
msg=st.text_area('Enter something in English',height=300)
if st.button('Update'):
    st.sidebar.subheader('Your Content')
    st.sidebar.write(msg)
if msg:
    blob=TextBlob(msg)
    tags=blob.tags
    st.subheader('Part of speech tagging : Nouns')
    nouns=[]
    for tag in tags:
        if tag[1]=='NN'
        nouns.append(tag)