





import os
from crewai import Task
from agents import (
    requirement_analyst_Agent,
    user_story_agent,
    pdd_agent,
    sdd_agent,
    component_mapper_agent,
    risk_analysis_agent,
    flowchart_agent,
    document_reviewer_agent,
    document_updater_agent,
    final_writer_agent
)

output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# ========== 1. Requirement Intake ==========

requirement_analyst_task = Task(
    description=(
        "Take the vague problem statement from {topic} and generate detailed, clear, and structured "
        "functional requirements. Your response must include two sections:\n\n"
        "1. **Original Client Requirements**: Paste the full deatiled original  {topic}.\n"
        "2. **Refined Functional Requirements**: Your rewritten version, organized and clarified for {topic}."
    ),
    expected_output=(
        "A markdown-formatted document with two sections:\n\n"
        "**Original Client Requirements**: (copy of the {topic})\n\n"
        "**Refined Functional Requirements**: (structured breakdown of clear, detailed requirements based on the {topic})"
    ),
    agent=requirement_analyst_Agent,
    output_file=os.path.join(output_dir, "01_requirements.txt")
)

requirement_analyst_review_task = Task(
    description=(
        "Review the requirement analyst document related to {topic} for the following:\n"
        "- Technical clarity and feasibility\n"
        "- Logical structure and testability of each requirement\n"
        "- Completeness of the functional requirements based on the original client statement\n\n"
        "Provide a markdown-formatted review report with suggestions for improvement if needed."
    ),
    expected_output="Review report with suggestions to improve clarity, feasibility, or completeness.",
    agent=document_reviewer_agent,
    context=[requirement_analyst_task],
    output_file=os.path.join(output_dir, "01a_requirements_review.txt")
)

requirement_update_task = Task(
    description=(
        "Update the requirement analyst document based on the review for {topic}. Ensure the following:\n"
        "- Keep the original client problem statement in a section titled '## Original Client Requirements'\n"
        "- Address all technical review feedback in the '## Refined Functional Requirements' section\n"
        "- Maintain formatting and IDs for each requirement\n"
        "- Ensure the requirements are implementable and testable"
    ),
    expected_output=(
        "A markdown-formatted document with two sections:\n\n"
        "**Original Client Requirements**: (copy of the {topic})\n\n"
        "** Refined Functional Requirements**: (updated requirement analyst document based on review)"
    ),
    agent=document_updater_agent,
    context=[requirement_analyst_task, requirement_analyst_review_task],
    output_file=os.path.join(output_dir, "01b_requirements_updated.txt")
)

# ========== 2. User Story ==========

user_story_task = Task(
    description=(
        "For the given {topic}, write a fully detailed enterprise-grade user story in agile format.\n\n"
        "The output must be in the following markdown order:\n"
        "- **Title**\n"
        "- **Epic**\n"
        "- **Feature**\n"
        "- **Priority**\n"
        "- **Story Points**\n"
        "- **User Story** (As a [role], I want to [goal], so that [benefit])\n"
        "- **🎯 Acceptance Criteria** (Grouped by themes such as Account Creation, Privacy, Security, etc.)\n"
        "- **📘 Functional Requirements Mapping** (List of FR codes used in the AC section with short definitions)\n"
        "- **✅ Definition of Done** (Checklist of conditions that must be met for the story to be considered complete)"
    ),
    expected_output=(
        "A markdown-formatted user story that includes all sections above and uses technical clarity, "
        "realistic testable conditions, and strong alignment with enterprise development standards."
    ),
    agent=user_story_agent,
    context=[requirement_update_task],
    output_file=os.path.join(output_dir, "02_user_story.txt")
)

user_story_review_task = Task(
    description=(
        "Review the user story for {topic} to ensure it:\n"
        "- Meets agile formatting and structure\n"
        "- Uses realistic and feasible acceptance criteria\n"
        "- Covers edge cases (errors, security, opt-outs)\n"
        "- Clearly maps acceptance criteria to functional requirements (FRs)\n"
        "- Has a comprehensive Definition of Done\n\n"
        "Suggest improvements or mark it as approved."
    ),
    expected_output="Review report with clear comments and improvement suggestions if needed.",
    agent=document_reviewer_agent,
    context=[user_story_task],
    output_file=os.path.join(output_dir, "02a_user_story_review.txt")
)

user_story_update_task = Task(
    description=(
        "Update the user story based on the review feedback for {topic}.\n"
        "Ensure all required changes are applied clearly.\n"
        "Keep the structure, FR mapping section, and DoD intact.\n"
        "If the review found no issues, simply confirm the document is good."
    ),
    expected_output="An updated and final markdown-formatted user story document.",
    agent=document_updater_agent,
    context=[user_story_task, user_story_review_task],
    output_file=os.path.join(output_dir, "02b_user_story_updated.txt")
)


# ========== 3. Project Design Document ==========
# ========== 3. Project Design Document (PDD) ==========

# pdd_task = Task(
#     description=(
#         "Based on the updated user story and {topic}, generate a concise, enterprise-grade Project Design Document (PDD) in markdown. "
#         "The PDD must include the following clearly defined sections:\n"
#         "1. Executive Summary\n"
#         "2. Problem Statement\n"
#         "3. Objectives & Success Metrics\n"
#         # "4. Scope (In-Scope / Out-of-Scope)\n"
#         "5. Features Overview (with priority levels)\n"
#         # "6. User Flows or Sample Interactions\n"
#         "7. Technical Architecture Overview\n"
#         # "8. Risks & Assumptions\n"
#         # "9. Appendices (if applicable)\n\n"
#         "Use clear section headers, bullet points where applicable, and maintain a formal, professional tone. Avoid unnecessary verbosity."
#     ),
#     expected_output="A clean, structured, enterprise-grade PDD in markdown format.",
#     agent=pdd_agent,
#     context=[user_story_update_task],
#     output_file=os.path.join(output_dir, "03_pdd.txt")
# )

# pdd_review_task = Task(
#     description=(
#         "Review the generated PDD document for:\n"
#         "- Structural completeness based on standard enterprise PDD format\n"
#         "- Professional tone and clarity\n"
#         "- Alignment with the updated user story and {topic}\n"
#         "- Redundancy or unnecessary content\n\n"
#         "Suggest any improvements in structure, accuracy, or brevity."
#     ),
#     expected_output="Detailed but concise review with suggested edits to align with enterprise-level standards.",
#     agent=document_updater_agent,
#     context=[pdd_task],
#     output_file=os.path.join(output_dir, "03a_pdd_review.txt")
# )

# pdd_update_task = Task(
#     description=(
#         "Revise the PDD document using the reviewer feedback for {topic}. "
#         "Ensure the final version is clean, enterprise-grade, and reflects all suggested improvements in structure and tone. "
#         "Preserve markdown formatting and maintain clarity."
#     ),
#     expected_output="Final updated PDD document with improved enterprise formatting and precision and it should be complete.",
#     agent=document_updater_agent,
#     context=[pdd_task, pdd_review_task],
#     output_file=os.path.join(output_dir, "03b_pdd_updated.txt")
# )




pdd_task = Task(
    description=(
        "Based on the updated user story and {topic}, generate a **complete and professional Project Design Document (PDD)** in markdown format. "
        "The PDD **must contain** the following clearly defined sections:\n\n"
        "1. Executive Summary\n"
        "2. Problem Statement\n"
        "3. Objectives & Success Metrics\n"
      
        "5. Features Overview \n"
      
        "7. Technical Architecture Overview (diagram explained in text form)\n\n"

        "Use proper section headers, bullet points, and markdown formatting. Use tables where appropriate (e.g., for features overview). "
        "**Ensure all sections are included and sufficiently elaborated.** Avoid verbosity but do not skip any section."
    ),
    expected_output="A complete, well-structured, markdown-based PDD document with all sections and table formatting where needed.",
    agent=pdd_agent,
    context=[user_story_update_task],
    output_file=os.path.join(output_dir, "03_pdd.txt")
)




pdd_review_task = Task(
    description=(
        "Carefully review the generated PDD document for {topic} for:\n"
        "- Presence and completeness of **all 9 required sections**\n"
        "- Correct use of markdown formatting (headers, lists, tables)\n"
        "- Clarity, accuracy, and formal tone\n"
        "- Missing or shallow sections (e.g., incomplete tables, skipped assumptions, vague architecture)\n"
        "- Redundancy or filler content\n\n"
        "**Highlight incomplete or missing sections explicitly.** Suggest precise edits or additions needed to bring the document up to enterprise standards."
    ),
    expected_output="A clear and detailed review listing missing content, weak sections, and markdown improvements (including any table/structure issues).",
    agent=document_reviewer_agent,
    context=[pdd_task],
    output_file=os.path.join(output_dir, "03a_pdd_review.txt")
)



pdd_update_task = Task(
    description=(
        "Revise and improve the PDD document for {topic} using the review feedback. Ensure the following:\n"
        "- **All required sections are present and complete**\n"
        "- Features Overview includes a **properly formatted table** (if missing or malformed)\n"
        "- All sections are elaborated with clarity and depth appropriate for an enterprise audience\n"
        "- Markdown formatting (headers, bullets, tables) is clean and consistent\n\n"
        "The final version must be clear, complete, professional, and publication-ready."
    ),
    expected_output="Final updated and complete PDD document with all improvements applied, formatted cleanly in markdown.",
    agent=document_updater_agent,
    context=[pdd_task, pdd_review_task],
    output_file=os.path.join(output_dir, "03b_pdd_updated.txt")
)










component_map_task = Task(
    description="Break the system for {topic} down into components and map suitable technologies based on SDD.",
    expected_output="Component list with matching technologies.",
    agent=component_mapper_agent,
    context=[pdd_update_task],
    output_file=os.path.join(output_dir, "05_component_mapping.txt")
)




# ========== 4. System Design Document ==========
# sdd_task = Task(
#     description=(
#         "Based on the updated PDD, write a System Design Document (SDD) including:\n"
#         "- Technical Architecture\n- Data Flow\n- Database Schema\n- API Specs based on the requirements"
#     ),
#     expected_output="A complete SDD in markdown.",
#     agent=sdd_agent,
#     context=[pdd_update_task, component_map_task],
#     output_file=os.path.join(output_dir, "04_sdd.txt")
# )

# sdd_review_task = Task(
#     description="Review the SDD document for completeness and correctness for {topic}.",
#     expected_output="Review report with suggestions.",
#     agent=document_reviewer_agent,
#     context=[sdd_task],
#     output_file=os.path.join(output_dir, "04a_sdd_review.txt")
# )

# sdd_update_task = Task(
#     description="Update the SDD based on the review for {topic}.",
#     expected_output="Update SDD document if required, based on review and it should be complete.",
#     agent=document_updater_agent,
#     context=[sdd_task, sdd_review_task],
#     output_file=os.path.join(output_dir, "04b_sdd_updated.txt")
# )




sdd_task = Task(
    description=(
        "Based on the updated PDD and component mapping for {topic}, generate a **complete and detailed System Design Document (SDD)** in markdown format. "
        "The SDD must include the following sections, clearly separated:\n\n"
        "1. **Technical Architecture** – Describe architecture layers, technologies, and responsibilities (e.g., frontend/backend/services).\n"
        "2. **Data Flow** – Describe how data moves through the system; use sequential bullet points or markdown flow representation.\n"
        "3. **Database Schema** – Provide an entity-relationship overview. Use markdown tables for entities with fields, types, and relations.\n"
        "4. **API Specifications** – Document at least 3-5 key APIs with:\n"
        "   - Endpoint (e.g., POST /predict)\n"
        "   - Description\n"
        "   - Request format (JSON with fields)\n"
        "   - Response format\n"
        "   - Status codes\n\n"
        "**All sections are mandatory.** Use proper markdown formatting, avoid placeholders, and ensure technical depth appropriate for a system architect or senior engineer."
    ),
    expected_output="A complete, clear, and technically sound SDD in markdown with all required sections and formatting.",
    agent=sdd_agent,
    context=[pdd_update_task, component_map_task],
    output_file=os.path.join(output_dir, "04_sdd.txt")
)



sdd_review_task = Task(
    description=(
        "Review the generated System Design Document (SDD) for {topic}. Specifically check:\n"
        "- **Presence and completeness of all four key sections** (Architecture, Data Flow, Database Schema, API Specs)\n"
        "- Markdown formatting (headers, code blocks, tables)\n"
        "- Technical accuracy and consistency with the PDD\n"
        "- Level of detail – ensure APIs have example payloads and status codes, DB schema has at least 3 tables\n"
        "- Missing content or vague sections (e.g., generic architecture, incomplete APIs, missing data flow)\n\n"
        "Highlight any missing or weak areas and suggest clear, specific improvements to elevate it to enterprise standard."
    ),
    expected_output="Detailed SDD review with clear notes on missing sections, vague content, or markdown issues.",
    agent=document_reviewer_agent,
    context=[sdd_task],
    output_file=os.path.join(output_dir, "04a_sdd_review.txt")
)





sdd_update_task = Task(
    description=(
        "Update and improve the SDD for {topic} using the review feedback. Ensure the final version includes:\n"
        "- All four required sections\n"
        "- **Fully detailed markdown-formatted API specs**, including endpoint, request/response, and status codes\n"
        "- **Clear database schema tables** with field names, types, and relationships\n"
        "- **Clean formatting**, clear section headers, bullet points, and tables where needed\n"
        "- Technical correctness and alignment with the PDD and requirements\n\n"
        "The updated SDD must be technically sound, markdown formatted, and ready for engineering implementation or architecture review."
    ),
    expected_output="Updated and complete SDD with all review points addressed and markdown correctly applied.",
    agent=document_updater_agent,
    context=[sdd_task, sdd_review_task],
    output_file=os.path.join(output_dir, "04b_sdd_updated.txt")
)











# ========== 5. Supporting Tasks ==========


risk_analysis_task = Task(
    description="List key risks and suggest mitigation strategies for the {topic} system.",
    expected_output="Risks and mitigation strategies.",
    agent=risk_analysis_agent,
    context=[sdd_update_task],
    output_file=os.path.join(output_dir, "06_risk_analysis.txt")
)


# flowchart_task = Task(
#     description=(
#         "Generate a system architecture flowchart in Mermaid format for {topic}, "
#         "showing main modules, data flows, and user interactions."
#     ),
#     expected_output="A Mermaid flowchart diagram.",
#     agent=flowchart_agent,
#     context=[sdd_update_task],
#     output_file=os.path.join(output_dir, "07_flowchart.txt")
# )


flowchart_task = Task(
    description=(
        "Generate a simple and clean system architecture flowchart in Mermaid format for {topic}. "
        "The diagram should include only high-level modules, main user interactions, and essential data flows. "
        "Avoid detailed descriptions, long edge labels, or nested flows. Limit to 10–15 nodes."
    ),
    expected_output="A simple and minimal Mermaid flowchart diagram with short node labels.",
    agent=flowchart_agent,
    context=[sdd_update_task ],
    output_file=os.path.join(output_dir, "07_flowchart.txt")
)






# ========== 6. Final Compilation ==========
final_writer_task = Task(
    description="Using the updated User Story, PDD, and SDD, create a final consolidated technical document for {topic}.",
    expected_output="A well-formatted combined document including the user story, PDD, and SDD.",
    agent=final_writer_agent,
    output_file=os.path.join(output_dir, "08_final_combined_output.txt"),
    context=[user_story_update_task, pdd_update_task, sdd_update_task],
    async_execution=False
)










from agents import word_doc_full_agent, word_doc_summary_agent, evaluation_agent

word_doc_full_task = Task(
    description=(
        "Generate formatted content for a full Word report for {topic}. It should include:\n"
        "- Updated Intake\n"
        "- Updated User Story\n"
        "- Updated PDD\n"
        "- Component Mapping\n"
        "- Updated SDD\n\n"
        "Use clear section headers, structured bullet points, and consistent layout in the text."
    ),
    expected_output="Formatted full report content as plain text for Word conversion.",
    agent=word_doc_full_agent,
    context=[final_writer_task],  # Ensure all updated documents are combined here
    output_file=os.path.join(output_dir, "docs_full.txt")
)




word_doc_summary_task = Task(
    description=(
        "Generate a Word summary report in plain text format for {topic}. "
        "The summary should highlight the main purpose, system overview, technical approach, and key components.\n\n"
        "Avoid deep implementation details but maintain sufficient context. "
        "Use clear section headings and bullet points where helpful."
    ),
    expected_output="Summarized report content in plain text for Word summary doc.",
    agent=word_doc_summary_agent,
    context=[final_writer_task],
    output_file=os.path.join(output_dir, "docs_summary.txt")
)










evaluation_task = Task(
    description=(
        "You will evaluate multiple documents generated for the topic: {topic}.\n\n"
        "For **each document**, provide the following scores:\n"
        "- Structural Completeness (out of 10)\n"
        "- Clarity & Tone (out of 10)\n"
        "- Technical Accuracy (out of 10)\n"
        "- Relevance to Topic (out of 10)\n"
        "- Overall Quality (out of 10)\n\n"
        "Also provide a short 2-3 lines paragraph with strengths, weaknesses, and improvement suggestions for each, format will be like first document name then score then paraggraph for each of documents.\n"
        "Documents to evaluate:\n"
        "- Requirements \n"
        "- User Story\n"
        "- Project Design Document (PDD)\n"
        "- System Design Document (SDD)\n"
    ),
    expected_output="An evaluation report with per-document scores and improvement suggestions.",
    agent=evaluation_agent,
    context=[
        requirement_update_task,
        user_story_update_task,
        pdd_update_task,
        sdd_update_task
    ],
    output_file=os.path.join(output_dir, "evaluation_report.txt")
)

