from crewai import Task
from agents import researcher, profiler

# Task for Researcher Agent: Extract Company Details
research_task = Task(
    description=(
        "Search and analyze the official website of {company} "
        "({company_website}), along with the following sites "
        "({sources}), and extract key information, names, "
        "and financials. Use the tools to gather content and "
        "identify and categorize the requirements. "
        "Make sure to include the following: {additional_info}"
    ),
    expected_output=(
        "A structured list of company details, including basic info "
        "key individuals, company overview, market and industry "
        "analysis, financial information, operational details, "
        "business strategy, innovation and R&D, environmental, "
        "social, and governance (ESG) information, and customer "
        "insights."
    ),
    agent=researcher,
    async_execution=True
)

# Task for Company Profiler Agent: Create a document to accurately summarize company details
profile_task = Task(
    description=(
        "Using the company details obtained from previous "
        "tasks, craft a strutured document to highlight the most "
        "relevant information. Employ tools to adjust and enhance the "
        "content. Make sure this is the best company profile ever but "
        "don't make up any information. Update every section—"
        "inlcuding the basic information, leadership, company overview, "
        "market and industry analysis, financial information, operational "
        "details, business strategy, innovation and R&D, environmental, "
        "social, and governance (ESG) information, and customer insights—"
        "to best reflect the company's true identity."
        "Additional info to include in the profile: {additional_info}"
    ),
    expected_output=(
        "A structured document that effectively highlights the company's "
        "key information to be used by senior executives for market analysis."
    ),
    output_file="profile.md",
    context=[research_task],
    agent=profiler
)