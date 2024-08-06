import streamlit as st
import os
import json
from dotenv import load_dotenv
from find_company import get_confirmed_company_details
from agents import researcher, profiler
from tasks import research_task, profile_task
from crewai import Crew, Process
from utils import convert_md_to_docx

# Warning control
import warnings
warnings.filterwarnings('ignore')

# Load environment variables from .env file
load_dotenv()

def main():
    serper_api_key = os.getenv('SERPER_API_KEY')
    
    # Get company details from user input and confirm the main website
    company_details = get_confirmed_company_details(serper_api_key)
    
    if company_details:
        company_name = company_details['company_name']
        company_website = company_details['company_website']
        additional_info = company_details['additional_info']
        
        st.write(f"Company Name: {company_name}")
        st.write(f"Company Website: {company_website}")
        st.write(f"Additional Info: {additional_info}")
        
        # Define sources to scrape and enhance the profile
        sources = [
            {"name": "Company Main Website", "url": company_website},
            {"name": "LinkedIn", "url": "https://www.linkedin.com/company/"},
            {"name": "Crunchbase", "url": "https://www.crunchbase.com"},
            {"name": "D&B Hoovers", "url": "https://www.dnb.com"},
            {"name": "ZoomInfo", "url": "https://www.zoominfo.com"},
            {"name": "Glassdoor", "url": "https://www.glassdoor.com"},
            {"name": "Yelp Business Listing", "url": "https://www.yelp.com"},
            {"name": "Google My Business", "url": "https://www.google.com/business"},
            {"name": "Better Business Bureau Profile", "url": "https://www.bbb.org"},
            {"name": "TrustPilot", "url": "https://www.trustpilot.com"},
            {"name": "G2 Crowd", "url": "https://www.g2.com"},
            {"name": "Local Business Directories and Chambers of Commerce", "url": "https://www.uschamber.com"},
            {"name": "IBISWorld", "url": "https://www.ibisworld.com"},
            {"name": "Statista", "url": "https://www.statista.com"},
            {"name": "Facebook Business Page", "url": "https://www.facebook.com"},
            {"name": "Top 2 results from Google News", "url": "https://news.google.com"},
            {"name": "Top 3 Google results", "url": "https://google.com"},
            {"name": "Industry Trade Publications and Directories", "url": "https://www.exampletradepublication.com"},  # Replace with actual trade publication URL
        ]
        
        # Create the crew
        company_profile_crew = Crew(
            agents=[researcher,
            profiler],

            tasks=[research_task,
            profile_task],

            verbose=True
        )

        # Configure the inputs (used by the research task)
        company_profile_inputs = {
            "company": f"{company_name}",
            "company_website": f"{company_website}",
            "sources": f"{sources}",
            "additional_info": f"{additional_info}"
        }

        # Run the crew
        result = company_profile_crew.kickoff(inputs=company_profile_inputs)

        # Display the results
        st.write("Finished building company profile")
        st.write(f"(These results were also saved to a file: {formatted_company_name}_profile.docx)")
        st.write(result)

        # Convert markdown to Word doc (for local use)
        # If running this app in the cloud, you may want to export the file to a cloud storage service
        formatted_company_name = company_name.replace(" ", "_").lower()
        convert_md_to_docx("profile.md", f"{formatted_company_name}_profile.docx")

if __name__ == "__main__":
    main()
