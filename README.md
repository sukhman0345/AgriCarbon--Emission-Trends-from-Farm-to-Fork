# 📊 AgriCarbon: Emission Trends from Farm to Fork
This repository contains the preprocessed dataset derived from FAO and IPCC sources, tracking CO₂ emissions across the agri-food sector.

# 🌍 Key Features of the Dataset
Crop Residue Burning

Fertilizer Application

Food Processing & Transport across regions and years

Fact: Agri-food activities contribute to ~62% of global annual CO₂ emissions.

# 📌 Use Cases
Climate impact analysis

Emission forecasting

Sustainability & policy research

# 🔗 Relation to the Streamlit Project – TheCarbonivore
This dataset serves as the foundation for the interactive Streamlit application, created in a separate repository:

TheCarbonivore Streamlit App Repository:

Project Structure:

AgriCarbon → Data preprocessing & cleaning

TheCarbonivore → Interactive Streamlit dashboard built using this dataset

Project Name: TheCarbonivore

# 🚀 Running the Streamlit Application
To explore the interactive dashboard for this dataset:

bash
Copy
Edit
# Clone the TheCarbonivore repository
git clone https://github.com/sukhman0345/theCarbonivore.git

# Navigate into the project folder
cd theCarbonivore

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
📌 Notes
This repository (AgriCarbon) only contains the processed dataset.

The UI code and dashboard logic are inside TheCarbonivore repository.

Ensure Python and Streamlit are installed before running the app.

