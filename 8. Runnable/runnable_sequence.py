from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=300)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variable=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':'AI'}))