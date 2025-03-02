import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

st.title("Coursera QA")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(49, 49, 240);
}
</style>""", unsafe_allow_html=True)

btn = st.button("Create Knowledgebase")
if btn:
   pass

b = st.markdown("""
<style>
div.stButton > button:first-child {
    margin-color: rgb(49, 49, 240);
}
</style>""", unsafe_allow_html=True)

question = st.text_input("Question: ")

if question:
    qa_chain = get_qa_chain()
    response = qa_chain.invoke({"input":question})

    st.header("Answer: ")
    st.write(response["answer"])
