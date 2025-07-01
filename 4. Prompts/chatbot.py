from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

# Initialize Gemini LLM
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=150)
chat_history = [SystemMessage(content="I am a helpful assistant")]

while True:
    user_input=input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if( user_input == "exit"):
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print(result.content)