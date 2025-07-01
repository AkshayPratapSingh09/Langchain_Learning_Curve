from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents = {
    "First is first never last",
    "India is in the South of the World",
    "Dont try to me very creative"

}
result = embedding.embed_documents(documents)

print(str(result))



