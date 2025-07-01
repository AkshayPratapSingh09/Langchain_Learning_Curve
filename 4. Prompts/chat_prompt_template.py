from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage

# Traditional Way
# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert"),
#     HumanMessage(content="Explain in simple terms, what is {topic}")
# ])

# Modern Way
chat_template = ChatPromptTemplate([
    ('system',"You are a helpful {domain} expert"),
    ('human',"Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({'domain':'fintech','topic':'Rise in startups'})

print(prompt)