from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI
#from langchain.chains import ChatVectorDBChain  ## biw: this has been depricated!!
from langchain.chains import ConversationalRetrievalChain

_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.
You can assume the question about the most recent state of the union address.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template = """You are an AI assistant for answering questions about the most recent state of the union address.
You are given the following extracted parts of a long document and a question. Provide a conversational answer.
If you don't know the answer, just say "Hmm, I'm not sure." Don't try to make up an answer.
If the question is not about the most recent state of the union, politely inform them that you are tuned to only answer questions about the most recent state of the union.
Question: {question}
=========
{context}
=========
Answer in Markdown:"""
QA_PROMPT = PromptTemplate(template=template, input_variables=["question", "context"])


def get_chai1n(vectorstore):
    llm = OpenAI(temperature=0)
    
    #qa_chain = ChatVectorDBChain.from_llm(
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        #vectorstore.as_retriever(),  # biw: was just vectorstore 
        retriever=vectorstore.as_retriever(),  
        qa_prompt=QA_PROMPT,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT
    )
    return qa_chain

def get_chain2(vectorstore):
    llm = OpenAI(temperature=0)
    
    #qa_chain = ChatVectorDBChain.from_llm(
    qa_chain = ConversationalRetrievalChain.from_llm(
        OpenAI(temperature= 0.0), 
        vectorstore.as_retriever(),  
        qa_prompt=QA_PROMPT,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
        verbose = True
    )
    return qa_chain

def get_chain(vectorstore):
    llm = OpenAI(temperature=0)
    
    #qa_chain = ChatVectorDBChain.from_llm(
    qa_chain = ConversationalRetrievalChain.from_llm(
        OpenAI(temperature= 0.0), 
        vectorstore.as_retriever(),  
        #qa_prompt=QA_PROMPT,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
        verbose = True
    )
    return qa_chain
