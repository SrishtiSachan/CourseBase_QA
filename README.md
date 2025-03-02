# CourseBase_QA
<img width="830" alt="Screenshot 2025-03-02 at 3 14 17 PM" src="https://github.com/user-attachments/assets/9dbc637f-7fa1-4390-82b6-149545276389" />


```CourseBase_QA``` is a Python-based project that provides a question-answering system related to course details using the LangChain library. It allows users to query a set of FAQs related to courses in a structured and efficient manner.

## Features

- Answering course-related queries.
- Uses LangChain to process and answer questions based on a dataset of FAQs (coursebase_faqs.csv).
- Using streamlit to test the code.
- Using RAG to provide more specific outputs , in context to our vector database. 
- Supports indexing and querying via FAISS for fast retrieval.
- Create Knowledgebase to update vector db, we already have index for our current data in ```faiss_db_index```.

## Requirements

To run the project, you'll need the following dependencies:

- Python 3.x
- langchain
- faiss
- streamlit

## Files

```CourseBase.ipynb:``` Jupyter notebook for exploring the functionality and testing the question-answering system.<br />

```coursebase_faqs.csv:``` CSV file containing frequently asked questions related to courses.<br />

```langchain_helper.py:``` Helper functions to integrate LangChain with the FAISS index.<br />

```main.py:``` Main script for running the question-answering system. This file contains code to integrate our code with UI using streamlit.<br />

```faiss_db_index:``` Directory containing the FAISS index vector database. This index is created and stored locally so that we don't need to create it again unless we have an updated csv file.<br />

## Usage

To use the question-answering system, run the main.py script. It loads the dataset of FAQs, indexes the data with FAISS, and answers course-related questions.

```
streamlit run main.py
```
