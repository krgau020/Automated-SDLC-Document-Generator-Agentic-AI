


import os
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    #model="gemini-2.0-pro",
    temperature=0.2,
    verbose=True,
    memory=True,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

requirement_analyst_Agent = Agent(
    role="Requirement Intake Agent",
    goal="Refine vague input for {topic} into detailed, structured requirements",
    backstory="An AI analyst that communicates with stakeholders to clarify vague or ambiguous requirements.",
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=True
)

document_reviewer_agent = Agent(
    role="Technical Reviewer",
    goal="Technically review documents based on {topic} and suggest improvements",
    backstory="Reviews technical documents for structure, completeness, and feasibility in the context of {topic}.",
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)

document_updater_agent = Agent(
    role="Final Reviewer",
    goal="Evaluate review quality and apply necessary updates for {topic} if required",
    backstory="A senior reviewer who ensures correctness and clarity of {topic}-related documents.",
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)

user_story_agent = Agent(
    role="Business Analyst",
    goal="Understand the requirement from {topic} and generate clear, concise user stories for agile environment",
    backstory="An experienced business analyst who translates business needs into actionable user stories.",
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=True
)

pdd_agent = Agent(
    role="PDD Specialist",
    goal="Create a Project Design Document from the user story and {topic}",
    backstory="A technical architect responsible for planning and system structure.",
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=True
)

sdd_agent = Agent(
    role="SDD Specialist",
    goal="Generate a detailed System Design Document based on the PDD",
    backstory="A system designer focused on translating designs into technical documents.",
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=True
)

component_mapper_agent = Agent(
    role="Component Mapper",
    goal="Map suitable technologies to components of {topic}",
    backstory="Identifies and selects technologies aligned with system modules for {topic}  based on PDD and SDD.",
    llm=llm,
    memory=True,
    verbose=True,
    allow_delegation=False
)

risk_analysis_agent = Agent(
    role="Risk Analyst",
    goal="Identify technical risks in the system for {topic} and propose mitigations",
    backstory="Helps ensure project success by anticipating and managing risks in {topic}-related systems.",
    llm=llm,
    memory=True,
    verbose=False
)

# flowchart_agent = Agent(
#     role="Flowchart Designer",
#     goal="Generate system flowcharts in Mermaid format to represent {topic}",
#     backstory="Creates clean and accurate visual flow representations of the {topic} system.",
#     llm=llm,
#     memory=True,
#     verbose=True,
#     allow_delegation=False
# )


flowchart_agent = Agent(
    role="Flowchart Designer",
    goal="Generate a clean and minimal Mermaid flowchart representing the {topic} system architecture.",
    backstory=(
        "Expert in designing clean system flowcharts using Mermaid syntax, focusing only on key modules, "
        "simple relationships, and high-level interactions. Avoids long labels and overly complex flows."
    ),
    llm=llm,
    memory=True,
    verbose=True,
    allow_delegation=False
)

final_writer_agent = Agent(
    role="Final Writer Agent",
    goal="Combine the User Story, PDD, and SDD into a final comprehensive output document",
    backstory="An experienced technical writer skilled at compiling and formatting technical documentation into a cohesive format.",
    verbose=False,
    memory=True,
    llm=llm,
    allow_delegation=False
)

# researcher_agent = Agent(
#     role="Researcher",
#     goal="Research and gather relevant data to enrich the design",
#     backstory="A researcher collecting technical and domain-specific references.",
#     verbose=True,
#     memory=True,
#     llm=llm
# )













word_doc_full_agent = Agent(
    role="Full Word Report Generator",
    goal="Generate complete, detailed Word report text content from system documents",
    backstory=(
        "You're a skilled technical writer responsible for compiling all finalized technical documentation "
        "into a single, well-structured Word report. Your goal is to preserve depth and clarity using proper sectioning."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)






word_doc_summary_agent = Agent(
    role="Summary Report Generator",
    goal="Generate a summary of the system documents for a Word report",
    backstory=(
        "You're a communication expert who summarizes technical documentation into readable overviews "
        "for non-technical persons. Your summary includes key points, system rationale, and high-level insights, "
        "but avoids implementation-level details."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False
)






evaluation_agent = Agent(
    role="Evaluation Agent",
    goal="Evaluate the overall effectiveness of the script and visuals",
    backstory="A creative director giving feedback on final assets.",
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=True
)
