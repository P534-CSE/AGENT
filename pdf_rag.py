import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA


load_dotenv()

# -----------------------------
# 1. Set OpenAI API Key
# -----------------------------
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable or add it to a .env file.")
os.environ["OPENAI_API_KEY"] = api_key


# -----------------------------
# 2. Load PDF
# -----------------------------
pdf_path = os.getenv("PDF_PATH", r"C:\Users\M.Pavitra\OneDrive\Desktop\CAT\document.pdf")

loader = PyPDFLoader(pdf_path)
documents = loader.load()


# -----------------------------
# 3. Create Embeddings
# -----------------------------
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


# -----------------------------
# 4. Create Vector Database
# -----------------------------
vectorstore = FAISS.from_documents(documents, embeddings)


# -----------------------------
# 5. Create Retriever
# -----------------------------
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


# -----------------------------
# 6. Create LLM
# -----------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# -----------------------------
# 7. Create RAG Chain
# -----------------------------
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
)


# -----------------------------
# 8. Ask Questions
# -----------------------------
while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    answer = rag_chain.invoke({"query": question})
    print("\nAnswer:")
    print(answer["result"])
