# Company Profile Generator

This app allows you to generate a company profile using OpenAI's GPT-4 model. You can input the company name and the app will search and scrape relevant websites and generate a company profile for you. The profile is based off a template that includes basic information, leadership, company overview, market and industry analysis, financial information, and operational details.

## Usage

### 1. Create a virtual environment and install the required packages:
``` bash
# Create a virtual environment
python3 -m venv myenv

# Activate a virtual environment
source myenv/bin/activate

# Install the required packages
pip3 install -r requirements.txt
```

### 2. Set `OPENAI_MODEL_NAME` in the `.env` file

You can change the OpenAI model used by setting `OPENAI_MODEL_NAME` to one of the following:
- `gpt-4o-mini`  
- `gpt-4o`

### 3. Run the streamlit app:
``` bash
streamlit run main.py
```# ai-report-generation
