from langchain_core.prompts import PromptTemplate


# Dynamic prompt construction
template = PromptTemplate(
    template = """
You are a helpful AI trained in summarizing research papers. 
Provide a summary of the following paper in the style of "{style}" and the length category "{length}".

Paper Title: "{title}"
Abstract: "{abstract}"

Ensure the summary is coherent, informative, and well-written.
""",

input_variables = ['style',"length","title","abstract"],
validate_template=True,
)


template.save("./template.json")