from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=300)

prompt = PromptTemplate(
    template=" Generate a detailed report {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template=" Generate a 5 pointer summary from the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()
chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'AI Startups in India'})

chain.get_graph().print_ascii()

print(result)