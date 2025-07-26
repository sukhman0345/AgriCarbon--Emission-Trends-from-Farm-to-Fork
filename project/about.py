import streamlit as st

def show_about():
    # Project Title
    st.markdown("""
        <div style='text-align: center'>
            <h1>About Project</h1>       
        </div>
        
    """, unsafe_allow_html=True)
    st.markdown("---")
    # Introduction Section
    st.markdown("""
        <div style='text-align: justify; font-size: 16px; line-height: 1.6'>
            <h2 style='text-align: center;'>Introduction</h2>
            <p>
                This project is built on the 
                <a href="https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml" target="_blank">
                Agri-Food CO₂ Emission Dataset on Kaggle</a>, compiled by merging and refining over a dozen individual sources from the 
                Food and Agriculture Organization (FAO) and Intergovernmental Panel on Climate Change (IPCC).
            </p>
            <p>
                The dataset provides a detailed view of agricultural emission activities across multiple sectors and years. 
                It contains 7,000 rows and 31 columns, capturing variables such as savanna and forest fires, crop residue management, 
                fertilizer production, rural and urban population statistics, and temperature variations.
            </p>
            <p>
                Each entry represents emission data recorded in kilotonnes (kt) and covers the period from 1990 to 2020 
                for various global regions. This dataset enables in-depth exploratory analysis, helping us understand 
                the intersection between agricultural activities and climate change.
            </p>
            <p>
                It lays the groundwork for future integration of regression and forecasting models while currently driving awareness 
                through interactive visualization and correlation-based insights.
            </p>
        </div>
        
    """, unsafe_allow_html=True)
    st.markdown("---")
    # Dataset Features Section Title
    st.markdown("""
        <div style='text-align: center'>
            <h2>Dataset Features</h2>       
        </div>
    """, unsafe_allow_html=True)
    
    # Dataset Feature List
    st.markdown("""
    - **Savanna Fires**  CO₂ emissions from fires in savanna regions  
    - **Forest Fires**  Emissions from forest fire activity  
    - **Crop Residues**  Emissions from burning or decomposition of leftover crop matter  
    - **Rice Cultivation**  Methane emissions produced during rice farming  
    - **Drained Organic Soils (CO₂)** CO₂ released due to drainage of organic soils  
    - **Pesticides Manufacturing**  Emissions from producing chemical pesticides  
    - **Food Transport**  Emissions from shipping and moving food products  
    - **Forestland**  Forest area acting as a carbon sink (negative emissions)  
    - **Net Forest Conversion**  Change in forest area due to land use shifts  
    - **Food Household Consumption**  Emissions from food consumed in homes  
    - **Food Retail**  Operational emissions of food retail businesses  
    - **On-Farm Electricity Use**  Energy consumed directly on agricultural farms  
    - **Food Packaging**  Emissions from creation and disposal of packaging materials  
    - **Agrifood Systems Waste Disposal**  Emissions from waste generated in agrifood systems  
    - **Food Processing**  Emissions from industrial food production and treatment  
    - **Fertilizers Manufacturing**  CO₂ released during fertilizer production  
    - **IPPU**  Emissions from industrial processes and product use  
    - **Manure Applied to Soils**  Emissions from animal manure spread on farmland  
    - **Manure Left on Pasture**  Emissions from grazing livestock manure  
    - **Manure Management**  Emissions from handling and storage of animal waste  
    - **Fires in Organic Soils**  Emissions caused by combustion of organic-rich soils  
    - **Fires in Humid Tropical Forests**  CO₂ from wildfires in tropical forest ecosystems  
    - **On-Farm Energy Use**  Broader energy footprint of farm operations  
    - **Rural Population**  Demographic count of people in rural zones  
    - **Urban Population**  Population in urbanized regions  
    - **Total Population - Male**  Total male population  
    - **Total Population - Female**  Total female population  
    - **Total Emission**  Sum of all recorded emissions across features  
    - **Average Temperature °C**  Annual temperature increase in degrees Celsius  
    """)

    st.markdown("---")

    #Data Scope
    st.markdown("""
        <div style='text-align: center'>
            <h2>Data analysis scope</h2>       
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
      <p>
        This project focuses on exploratory data analysis of agricultural CO₂ emissions across 
        regions. It utilizes visual techniques like heatmaps, sunburst charts, and scatter
        plots to reveal emission patterns, population dynamics, and their interconnections
        with climate trends. The goal is to translate raw environmental data into policy-relevant 
        insights.
                
       </p>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    #Geographical and Temporal Coverage
    st.markdown("""
        <div style='text-align: center'>
            <h2>Geographic and Temporal Coverag</h2>       
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
      <p>
        The dataset spans data from over 150 countries or territories between 1990 and 2020, 
        focusing particularly on agricultural activity, energy consumption, and food systems.
        Each row represents a snapshot of CO₂ emissions from multiple sources recorded yearly,
        allowing for trend analysis and historical comparison.
     </p>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    #Future Development
    st.markdown("""
        <div style='text-align: center'>
            <h2>Future Enhancements</h2>       
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
      <p>
        Planned extensions include integrating machine learning models for temperature variation prediction and anomaly detection. Additional features will allow dynamic filtering and country-level reporting, making the dashboard more interactive and responsive to user needs.
     </p>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.markdown("""

<p style="text-align: center; color: gray;">
    © 2025 sukhman.singh.codes
</p>
""", unsafe_allow_html=True)

