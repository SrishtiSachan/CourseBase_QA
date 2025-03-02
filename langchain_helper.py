from dotenv import load_dotenv
load_dotenv()
# The above module imports variables in .env file. It sets these as os env variables.

from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores.faiss import FAISS

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

import os
# from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import CSVLoader
# The below api key is just for experiment , if i can declare it as a var in .env


# Below code is to create vector embeddings from HuggingFace
model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

vector_db_filepath = "faiss_db_index"
# Using llama3.2 , tried ChatOpenAI,ChatVertexAI, gemini - all cost money
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

def create_vector_db():
    loader = CSVLoader(file_path='coursebase_faqs.csv', encoding='cp1252', source_column='prompt')
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=hf)
    vectordb.save_local(vector_db_filepath)

def get_qa_chain():
    # Load vector database from local folder
    vectordb = FAISS.load_local(vector_db_filepath, hf, allow_dangerous_deserialization=True)

    # Create retriever to query vectordb
    retriever = vectordb.as_retriever()
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain

if __name__=="__main__":
    # create_vector_db()
    chain = get_qa_chain()
    print(chain.invoke({"input": "Do you provide internship ? Do you provide EMI options ?"})["answer"])

