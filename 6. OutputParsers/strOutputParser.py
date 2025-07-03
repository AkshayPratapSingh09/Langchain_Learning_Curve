# from langchai_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# model = ChatOpenAI(model='gpt-4.1-mini', temperature=1)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=150)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variable=["topic"]
)
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text./n {text}",
    input_variable=["text"]
)

# Old Way 
    # prompt1 = template1.invoke({'topic':'black hole'})

    # result = model.invoke(prompt1)

    # prompt2 = template2.invoke({'text':result.content})

    # result2 = model.invoke(prompt2)
    # print(result.content)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)