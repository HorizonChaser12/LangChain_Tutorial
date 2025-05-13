from langchain_core.prompts import PromptTemplate

#template that would be passed upon to generate the Prompt template as a JSON format which can be used in multiple places.

template = PromptTemplate(
    template="""
     Please summarize the research paper titled "{paper_input}" with the following specifications: 
     Explanation Style: {style_input}
     Explanation length: {length_input} 
     1. Mathematical Details:
        - Include relevant mathematical equations if present in the paper. 
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable. 
     2. Analogies: 
        - Use relatable analogies to simplify complex ideas. 
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing. 
    Ensure the summary is clear, accurate, and aligned with the provided style and length.                   
""",
input_variables=['paper_input','style_input','length_input'],
# This is to ensure that all the input variables are given which are mentioned in the Template and has their specific placeholders.
validate_template=True)

template.save('4.Prompts/Template.json')