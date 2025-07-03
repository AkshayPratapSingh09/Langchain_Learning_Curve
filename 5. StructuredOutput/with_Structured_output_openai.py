# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=150)
model = ChatOpenAI(model='gpt-4.1-mini', temperature=1.5, max_completion_tokens=100)

class Review(TypedDict):
    reason:str
    sentiment:str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
    Give me the sentiment of the sentence : ""The lazy dog was beaten by the police men""
 """)

print(result['sentiment'])
print(result['reason'])

