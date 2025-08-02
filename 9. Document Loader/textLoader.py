from langchain_community.document_loaders import TextLoader


from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1, max_output_tokens=150)

prompt = PromptTemplate(
    template='Write a summary within 50-60 words for the following part of the big harry potter story book - \n {storyChunk}',
    input_variables=['storyChunk']
)

parser = StrOutputParser()

loader = TextLoader('9. Document Loader/testingDocuments/harryPotter.txt',encoding='utf-8')

docs = loader.load()

# print(type(docs))

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'storyChunk':docs[0].page_content}))
