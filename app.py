from flask import Flask, request, jsonify
from langchain_community.llms import Ollama
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader

app = Flask(__name__)

llm = Ollama(model='nemotron-mini', base_url='http://localhost:11434')

def create_embeddings_flask(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, 
        chunk_overlap=100, 
        length_function=len
    )

    join_chunks = text_splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    vectorial_data_base = FAISS.from_texts(join_chunks, embeddings)

    return vectorial_data_base

default_data_base = create_embeddings_flask("PDF/vikingos.pdf")

@app.route("/nemotron-mini", methods=["POST"])
def llama2():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "Debe proporcionar una pregunta en el formato {'question': 'texto de la pregunta'}"}), 400
    
    context = default_data_base.similarity_search(question)
    chain = load_qa_chain(llm, chain_type="stuff")

    answer = chain.run(input_documents=context, question=question)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(port=3333)