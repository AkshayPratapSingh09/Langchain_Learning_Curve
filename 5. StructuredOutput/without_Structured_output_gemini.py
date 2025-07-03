from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=150)

result = model.invoke("""
    Give me the sentiment of the sentence : ""The lazy dog was beaten by the police men""
 """)

print(result.content)

