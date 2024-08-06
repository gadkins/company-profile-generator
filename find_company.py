# findCompany.py
import streamlit as st
import logging
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables from .env file
load_dotenv()

def find_company_websites(company_name, serper_api_key):
    search_query = f"{company_name} official site"
    search_results = SerperDevTool(api_key=serper_api_key)._run(search_query)
    logging.info(f"Raw Search Results: {search_results}")

    search_results_list = search_results.strip().split('---')
    parsed_results = []

    for result in search_results_list:
        lines = result.strip().split('\n')
        if len(lines) >= 3:
            title = lines[0].replace('Title: ', '').strip()
            link = lines[1].replace('Link: ', '').strip()
            snippet = lines[2].replace('Snippet: ', '').strip()
            parsed_results.append({'title': title, 'link': link, 'snippet': snippet})

    return parsed_results

def get_confirmed_company_details(serper_api_key):
    st.title("Customer Profile Creator")

    if 'stage' not in st.session_state:
        st.session_state.stage = 0
    if 'company_name' not in st.session_state:
        st.session_state.company_name = ""
    if 'company_website' not in st.session_state:
        st.session_state.company_website = ""
    if 'additional_info' not in st.session_state:
        st.session_state.additional_info = ""

    if st.session_state.stage == 0:
        st.session_state.company_name = st.text_input("What Company would you like to Research?")
        if st.button("Find Company"):
            st.session_state.stage = 1

    if st.session_state.stage == 1:
        st.write(f"Searching for {st.session_state.company_name}...")

        try:
            parsed_results = find_company_websites(st.session_state.company_name, serper_api_key)
        except Exception as e:
            logging.error(f"Error finding company websites: {e}")
            st.error("An error occurred while searching for company websites.")
            st.stop()

        website = None

        with st.form(key='website_selection'):
            for result in parsed_results:
                st.markdown(f"<div style='font-size:12px;'>Title: {result['title']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div style='font-size:12px;'>Link: <a href='{result['link']}'>{result['link']}</a></div>", unsafe_allow_html=True)
                st.markdown(f"<div style='font-size:12px;'>Snippet: {result['snippet']}</div>", unsafe_allow_html=True)
                user_confirmation = st.radio("Is this the correct company website?", ['Y', 'N'], key=result['link'])
                if user_confirmation == 'Y':
                    website = result['link']
                    break

            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not website:
                st.error("Could not find a valid company website. Please try again later.")
                st.stop()

            st.session_state.company_website = website
            st.session_state.stage = 2

    if st.session_state.stage == 2:
        st.session_state.additional_info = st.text_area("Do you have any additional information about this company you want to include in the profile?")
        if st.button("Finish"):
            st.session_state.stage = 3

    if st.session_state.stage == 3:
        # Clear inputs by not rendering them
        st.write("Thank you for providing the information. The company profile will be generated shortly.")

        # Return the dictionary with all the information
        return {
            'company_name': st.session_state.company_name,
            'company_website': st.session_state.company_website,
            'additional_info': st.session_state.additional_info
        }
            
    return None
