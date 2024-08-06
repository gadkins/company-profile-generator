from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_template = FileReadTool(file_path='./company-profile-template.md')
semantic_search_profile = MDXSearchTool(mdx='./company-profile-template.md')