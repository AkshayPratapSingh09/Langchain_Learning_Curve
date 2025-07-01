from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

startup_profiles = [
    "Nikhil Kamath is the co-founder of Zerodha, a fintech startup revolutionizing retail stock trading in India.",
    "Deepinder Goyal founded Zomato, a food delivery giant that transformed how India eats and explores restaurants.",
    "Bhavish Aggarwal co-founded Ola and Ola Electric, pushing India’s ride-sharing and electric vehicle sectors forward.",
    "Kunal Shah is the founder of CRED, a fintech platform redefining credit card payments and customer engagement.",
    "Ghazal Alagh co-founded Mamaearth, a D2C personal care brand known for its toxin-free and eco-conscious products."
]

query = "tell me about India top food delivery company"

doc_embeddings = embedding.embed_documents(startup_profiles)
query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

index, score = (sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])
print(query)
print(startup_profiles[index])
print("Similarity Score is ",score)
