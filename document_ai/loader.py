from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import Docx2txtLoader

import os

class Loader:

    def __init__(self) -> None:
        pass

    def doc_loader(self,path):
        document=[]
        for file in os.listdir(path):
            if file.endswith(".pdf"):
                pdf_path="./docs/"+file
                loader=PyPDFLoader(pdf_path)
                document.extend(loader.load())
            elif file.endswith('.docx') or file.endswith('.doc'):
                doc_path="./docs/"+file
                loader=Docx2txtLoader(doc_path)
                document.extend(loader.load())
            elif file.endswith('.txt'):
                text_path="./docs/"+file
                loader=TextLoader(text_path)
                document.extend(loader.load())
        