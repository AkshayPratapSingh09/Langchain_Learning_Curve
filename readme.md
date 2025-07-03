# ## **What is GenAI**?
- Type of AI that creates New Content ***eg. Image, Text, Videos, code etc*** by learning patterns and mimicking human creativity
<br>

<div align="center">
  <img width="300px" src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f5y9ezDXqQ5uS6QRZPwSuQ.png" />
</div>

### 💡Note :: Whenever you are trying to solve a GenAI problem always consider which section it Falls in
<div align="center">
  <a href="https://ibb.co/cKJCr5QP"><img src="https://i.ibb.co/1YZdmVT3/image.png" alt="image" border="0"></a>
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


# #Model

- This component is cruical in langchain to facilitate Interactions b/w **language models** and **embedding models**

<img src="https://i.ibb.co/9kTVBmnW/image.png" alt="image" border="0">

- There is LLM and there is ChatModel (Both are difference)

`temperature` is a parameter that **controls the randomness of a language model's output**. It affects how **creative or deterministic** the responses are.

- **Lower values (0.0 – 0.3)** → More **deterministic** and predictable.
- **Higher values (0.7 – 1.5)** → More **random, creative**, and diverse.

<img src="https://i.ibb.co/x88HwL8q/image.png" alt="image" border="0">


### When Using Langchain there will be 2 choices for using the Inference
1. **Normal LLM** - *It will simply return the answer in a string format*
2. **Chat** - *It will return the response in a proper object/JSON*

<div style="width: 100%">

### 🧾 API Response

```json
{
  "content": "Beneath the sky, the bat doth gleam,\nOn fields where heroes chase their dream.\nThe ball flies swift, the crowd’s loud cheer,\nEchoes of joy are ringing near.\nIn cricket's dance, hearts hold dear.",
  "additional_kwargs": {
    "refusal": null
  },
  "response_metadata": {
    "token_usage": {
      "completion_tokens": 53,
      "prompt_tokens": 15,
      "total_tokens": 68,
      "completion_tokens_details": {
        "accepted_prediction_tokenrobs": null
      }
    },
    "id": "run--96b2776f-05df-4bb1-980a-631f0d96f2fa-0",
    "usage_metadata": {
      "input_tokens": 15,
      "output_tokens": 53,
      "total_tokens": 68,
      "input_token_details": {
        "audio": 0,
        "cache_read": 0
      },
      "output_token_details": {
        "audio": 0,
        "reasoning": 0
      }
    }
  }
}
```
</div>

## #Prompts

**PromptTemplates** are structured ways to create dynamic prompts

**Why use PromptTemplate over f strings?**
  1. Default Validation(Production Tolerant)
  1. Reusable
  1. Langchain Ecosystem

  # #Messages

### 📬 Types of Messages in LangChain

| Message Type     | Description                                             | Common Use Case                        |
|------------------|---------------------------------------------------------|----------------------------------------|
| `SystemMessage`  | Sets the behavior of the AI assistant                   | "You are a helpful assistant."         |
| `HumanMessage`   | Represents input from the user                          | "Tell me about LangChain."             |
| `AIMessage`      | Represents the LLM’s response                           | "LangChain is a framework for..."      |
| `ToolMessage`    | Captures output from a tool used by an agent            | Tool-generated data or intermediate result |
| `FunctionMessage`| Holds the return value of a function/tool invocation    | Function call return (e.g., search API)|
| `ChatMessage`    | Generic message with custom `role` (e.g., "user", "assistant", "function") | Flexible custom messaging |

---

#### 📌 Examples: Message Flow Example

```python
[
  SystemMessage("You are a helpful assistant."),
  HumanMessage("Translate 'Namaste' to English."),
  AIMessage("Hello"),
]
```
# #Chat Prompt Templates

- We can send dynamic messages within *single message*
- But for a list of dynamic message we will have to use ***ChatPromptTemplate***

<a href="https://ibb.co/cKD7hdQc"><img src="https://i.ibb.co/GfcbQjRv/image.png" alt="image" border="0"></a>







