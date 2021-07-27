import Scrape_text
import streamlit as st
import Clean
import transformers
from transformers import pipeline
from transformers.pipelines import base

nlp = pipeline("question-answering")

interview=Clean.interview(Scrape_text.contexts())

# Project Title
st.header("Welcome to Automated Q&A bot")

# To fetch the query that is the question  
#question=st.text_input('Ask a question here:') 

# To fetch the query that is the question  
question=st.text_input('Ask a question here:') 


answer = nlp(question=question, context=interview)
st.text(answer['answer'])

