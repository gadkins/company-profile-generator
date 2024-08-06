from crewai import Agent
from tools import scrape_tool, search_tool

# Agent 1: Researcher
researcher = Agent(
    role="Company Researcher",
    goal="Make sure to do amazing analysis on "
         "the company, ensuring all important " 
         "information is collected.",
    tools = [scrape_tool, search_tool],
    verbose=True,
    backstory=(
        "Equipped with analytical prowess, you dissect "
        "and synthesize information "
        "from diverse sources to craft comprehensive "
        "company profiles, laying the foundation for "
        "detailed reports used by senior executives."
    )
)

# Agent 2: Company Profiler
profiler = Agent(
    role="Company Profile Creator",
    goal="Create a comprehensive company profile "
         "based on information found online about the company.",
    tools = [scrape_tool, search_tool],
    verbose=True,
    backstory=(
        "With a strategic mind and an eye for detail, you "
        "excel at crafting company profiles to highlight "
        "the most relevant information about the company, "
        "they align perfectly with the company's true information. "
        "Your profiles are concise, yet complete, with a strong "
        "preference towards bulleted lists."
    )
)