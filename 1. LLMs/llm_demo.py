from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()


llm = GoogleGenerativeAI(model="gemini-2.0-flash")

# Simple text invocation
result = llm.invoke("List the latest progress of indiaAI mission in last 1 Month")
print(result)

# Multimodal invocation with gemini-pro-vision
# message = HumanMessage(
#     content=[
#         {
#             "type": "text",
#             "text": "What's in this image?",
#         },
#         {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
#     ]
# )
# result = llm.invoke([message])
# print(result.content)