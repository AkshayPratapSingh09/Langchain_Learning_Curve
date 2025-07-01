from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini LLM
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7,max_new_tokens=150)

messages = [
    SystemMessage(content="Your are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)