import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

KNOWLEDGE_BASE = "knowledge_base"


def load_documents():

    documents = []

    for file in os.listdir(KNOWLEDGE_BASE):

        if file.endswith(".txt"):

            loader = TextLoader(
                os.path.join(KNOWLEDGE_BASE, file),
                encoding="utf-8"
            )

            documents.extend(loader.load())

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=50

    )

    return splitter.split_documents(documents)
def create_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore

def get_retriever():

    documents = load_documents()

    chunks = split_documents(documents)

    vectorstore = create_vectorstore(chunks)

    return vectorstore.as_retriever(
        search_kwargs={"k": 2}
    )

def retrieve_context(query):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    # ----------------------------------
    # Clean Markdown formatting
    # ----------------------------------

    context = (
        context
        .replace("# ", "")
        .replace("## ", "")
        .replace("### ", "")
        .replace("---", "")
        .replace("**", "")
    )

    # Remove extra blank lines
    while "\n\n\n" in context:
        context = context.replace("\n\n\n", "\n\n")

    return context.strip()