from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat Template
chat_template = ChatPromptTemplate([
    ('system',"Your are a helpful customer support agent"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human',"{query}")
])

chat_history = []
# Load Chat History
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history,"query":"What is the current progress of my refund"})

print(prompt)