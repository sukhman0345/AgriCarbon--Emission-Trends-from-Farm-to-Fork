import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Updated CSS
page_bg_image = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://plus.unsplash.com/premium_vector-1719110245001-e40424da8477?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8b24lMjBjbzJ8ZW58MHx8MHx8fDA%3D");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}

[data-testid="stToolbar"]{
right: 2rem;
}

[data-testid="stSidebar"]{
background-image: url("")

</style>
'''
st.markdown(page_bg_image, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;'>🌾 Agri-food CO₂ Emission</h1>", unsafe_allow_html=True)

# About Dataset
st.subheader("About DataSet")

st.markdown("""
    <div style='color:rgb(64, 64, 64); font-size:17px; padding-bottom:20px;'>
    ➤ Total Columns: The dataset contains 31 columns, each representing a unique variable related to agricultural activities, food systems, fire events, climate indicators, or population demographics.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='color:rgb(64, 64, 64); font-size:17px; padding-bottom:12px;'>
    ➤ Total Rows: There are 6,965 rows, covering multiple countries or regions across several years — giving a rich temporal and geographic perspective.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='color:rgb(64, 64, 64); font-size:17px; padding-bottom:12px;'>
    ➤ Dataset Focus: It centers on analyzing CO₂ emissions generated from the agri-food sector, including activities like crop residue burning, rice cultivation, fertilizer production, food transport, and energy use.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='color:rgb(64, 64, 64); font-size:17px; padding-bottom:12px;'>
    ➤ Source Composition: This dataset is a merged and cleaned composite of over a dozen datasets from the FAO and IPCC, designed for in-depth climate and sustainability analysis.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='color:rgb(64, 64, 64); font-size:17px; padding-bottom:12px;'>
    ➤ Environmental Relevance: It highlights that agri-food systems contribute approximately 62% of global annual emissions, underlining their major role in climate change discourse.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='color:rgb(64, 64, 64); font-size:17px; padding-bottom:12px;'>
    ➤ Use Case: Ideal for descriptive analysis, emission trend visualization, and policy-relevant insight generation in agriculture and environmental planning. A regression model is also included to examine temperature variation dynamics.
    </div>
""", unsafe_allow_html=True)

# load file
file = st.file_uploader("Upload your csv file", type=["csv"])

if file:
  df = pd.read_csv(file)
  st.subheader("Data preview")
  st.dataframe(df)

if file:
  st.subheader("Summary Status") 
  st.write(df.describe())

if file:
  st.subheader("Head Data")
  st.write(df.head())
  st.subheader("Tail Data")
  st.write(df.tail())

# Visualization of graphs
if file is not None:
    st.subheader("Choropleth: Total emissions by Area")

    fig = px.choropleth(
        df,
        locations="Area",
        locationmode="country names",
        color="total_emission",
        hover_name="Area",
        animation_frame="Year",
        title="Area-wise Total Emissions"
    )

    fig.update_layout(
        title_x=0.5,
        width=800,
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please upload a valid file to visualize emissions data.")

# 2nd chart
if file is not None:
    st.subheader("Line Chart: Year Trend of Rice Cultivation Emission")

    # Create line chart using Plotly Express
    fig = px.line(
        df,
        x="Year",
        y="Rice Cultivation",
        color="Area",
        title="Rice Cultivation Emissions over Time"
    )

    # Customize layout
    fig.update_layout(
        width=1200,
        height=500,
        title_x=0.2
    )

    # Display chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Please upload a valid file to visualize emissions data.")

#3rd graph
if file is not None:
    st.subheader("Bar Chart: Top 10 Areas by Fire-Based Emissions")

    # Group and calculate average emissions by fire type
    fire_df = df[[
        "Area", 
        "Forest fires", 
        "Savanna fires", 
        "Fires in humid tropical forests"
    ]].groupby("Area").mean().reset_index()

    # Calculate total fire emissions per area
    fire_df["Total Emissions"] = fire_df[[
        "Forest fires", 
        "Savanna fires", 
        "Fires in humid tropical forests"
    ]].sum(axis=1)

    # Sort and keep top 10 highest emitting areas
    top_fire_df = fire_df.sort_values("Total Emissions", ascending=False).head(10)

    # Melt data for grouped bar plotting
    fire_melted = top_fire_df.drop(columns="Total Emissions").melt(
        id_vars="Area", 
        var_name="Fire Type", 
        value_name="Emissions"
    )

    # Create bar chart using Plotly Express
    fig = px.bar(
        fire_melted,
        x="Area",
        y="Emissions",
        color="Fire Type",
        title="Top 10 Areas by Fire-Based Emissions",
        labels={"Emissions": "Emissions (Kilotons)"}
    )

    # Customize layout
    fig.update_layout(
        xaxis_tickangle=-45,
        width=1100,
        height=600,
        title_x=0.5
    )

    # Display chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Please upload a valid file to visualize fire-based emissions data.")

#4 chart
if file is not None:
    st.subheader("Pie Chart: Industrial Emission Composition")

    # Filter data for the latest year
    year_df = df[df["Year"] == df["Year"].max()]

    # Sum relevant industrial emission sources
    ind_emissions = year_df[[
        "IPPU", 
        "On-farm Electricity Use", 
        "Food Processing"
    ]].sum()

    # Create pie chart using Plotly Express
    fig = px.pie(
        values=ind_emissions.values,
        names=ind_emissions.index,
        title=f"Industrial Emission Proportion in {year_df['Year'].max()}"
    )

    # Customize layout
    fig.update_layout(
        title_x=0.3,
        width=1000,
        height=500
    )

    # Display chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Please upload a valid file to visualize industrial emissions.")

# side bar
st.sidebar.header("Filteration")
