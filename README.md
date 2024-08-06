# Company Profile Generator

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
