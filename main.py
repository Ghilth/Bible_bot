import os, dotenv
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain






#API keys loading
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')




#LLM loading. Here we use gemini
llm= ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5)



#Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", temperature=0.5)




#BDV loading
bible_bdv_path="bible_bdv"
data_store=Chroma(persist_directory=bible_bdv_path, embedding_function=embeddings)





#Then, we will retriever a vectorial database. If you want how to xreate a database, you'll find it in notebook
retriever = data_store.as_retriever(search_type="similarity", search_kwargs={"k": 15})



#PrompTemplate
#Here I create a template to use to query the model
template = """You are a bot expert in theology and mastering the history of the Bible, you are responsible for responding clearly and in detail
 questions relating to the Bible.


 In addition to the information provided in the document, add your knowledge as a gemini pro
 to answer the questions.

 You can freely copy part of the Bible and rephrase it if necessary.

 Be tolerant of any words or expressions, and always return a response.

 Answer in input language. If the question is in french, answer in french; if it is is english, answer in english.

 If you don't have enough information, respond with: "I don't have enough information to answer this question."



 Here is the question: {input}

  context: {context}
  input: {input}
  answer:
 """


prompt = PromptTemplate(
        template=template,
    input_variables=['input']
)



#Chain LLM, prompt and retriever
combine_docs_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)





#Let's write a function to retrieve with llm
def ask(question : str):
    response=retrieval_chain.invoke({"input": question})

    if response:
        return response['answer']
    else :
        "Please, ask another question"



print(ask("luc 20 v45 47"))