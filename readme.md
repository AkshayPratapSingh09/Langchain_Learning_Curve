# ## **What is GenAI**?
- Type of AI that creates New Content ***eg. Image, Text, Videos, code etc*** by learning patterns and mimicking human creativity
<br>

<div align="center">
  <img width="300px" src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f5y9ezDXqQ5uS6QRZPwSuQ.png" />
</div>

### 💡Note :: Whenever you are trying to solve a GenAI problem always consider which section it Falls in
<div align="center">
  <img width="600px" src="https://i.ibb.co/nH35r3P/image.png" alt="image" border="0">
</div>

## #Langchain

***Open Source Framework that helps in building LLM based applications. It provides modular components and end-to-end tools that help developers build complex AI applications, such as chatbots,question- answering systems, retrieval-augmented generation(RAG), autonoumous agents, and more.***

  1. Supports all the major LLMs
  2. Simplifies developing LLM based applications
  3. Integrations available for all major tools
  4. Open Source/Free/Actively Developed
  5. Supports all major GenAI use cases



- ## What we can Build
1. Conversational Chatbot
1. AI Knowledge Assistants
1. AI Agents
1. Workflow Automation
1. Summarization/Research Helpers


### 💡Langchain Identified the problem of Standardization(Different packages and code for different offerings) of the Code to access Remote Model Deployment💡

## #Components of Langchain
1. ### Models
2. ### Prompt
3. ### Chains
4. ### Indexes
5. ### Memory
6. ### Agents

<img src="https://i.ibb.co/q3FwjHbv/image.png" alt="image" border="0">

Two types of models are there in Langchain 
- **Language Models** - Generative AI model to generate data
- **Embedding Models** - Vectorization models to vecotorized and query/semantic search for RAG like systems(*Different embedding vectors for every model*)

- Doc Link (Language Models Available) - https://python.langchain.com/docs/integrations/providers/
- Doc Link (Embedding Models Available) - https://python.langchain.com/docs/integrations/text_embedding/


## Chains

- Used to build pipelines
- These pipelines can facilitate other pipelines
- For eg. One chain output can be another chains input

<img src="https://i.ibb.co/B0XZC5W/image.png" alt="image" border="0">

## Indexes

- It connects your application to external knowledge-such as PDF,websites or databases
- eg.( *Doc Loader, Text splitter, vector storage, retrivers*)

## Memory

- LLM API calls are bydefault stateless(*They dont have previous or past messages*)

### Types of Memory

**1. ConversationalBufferMemory**  
---
*Store a transcript of recent messages. Great for short chats but can grow large quickly.*

**2. ConversationalBufferWindowMemory**  
---
*Only Keeps the last N interactions to avoid excessive token usage.*

**3. Summary Based Memory**  
---
*Periodically summarizes older chat segments to keep a condensed memory footprint.*

**4. Custom Memory**  
---
*For advanced use cases, you can store specialized state (e.g. the user's preferences or key facts about them in a custom memory class).*

## Agents
- Have access to tools and have reasoning capabilties


