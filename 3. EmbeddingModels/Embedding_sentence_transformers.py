from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

documents = {
    "First is first never last",
    "India is in the South of the World",
    "Dont try to me very creative"

}
vector = embeddings.embed_documents(documents)

print(vector)