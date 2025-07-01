from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.8)

# Simple text invocation
result = llm.invoke("write a hindi poem in 4 lines about students")
print(result.content)