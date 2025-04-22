import streamlit as st
import streamlit.components.v1 as components

def show_home():
     # image
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('./data/image.png')

    with col3:
        st.write(' ')
    
    # Title of the page
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 32px;">
        What Makes a Winning Eurovision Entry:<p>
        <p style="text-align: center; font-size: 26px; margin-top: -10px;">
        What Data (if any) are a Good Predictor for Success in the Eurovision Song Contest? <p>
        <p style="text-align: center; font-size: 22px; margin-top: -10px;">
        Ayla Abdullah,  Neringa Šiožinytė, Alexander Wamboldt
        </p>
        """, unsafe_allow_html=True
        )

    # Introduction
    
    st.markdown(
        """
        <h2 style="text-align: center; font-size: 26px;">Introduction</h2>
        <div style="text-align: justify; font-size: 22px;">
       The Eurovision Song Contest is an annual competition organized by the European Broadcast Union among its members.
         Started in 1956, the contest features original songs that are performed by six or less people and broadcast live.
         Voters in each competing country can then award points to their favorite entries (excluding their own),
         though the voting method has changed over the years. But, what makes for a good Eurovision song?    
         </p>
         Well, that’s the question that these three nerds are going to try to answer.
         For this analysis, we used data on the competitors and country votes from 1956-2023,
         song-specific data from 2009-2023, betting organizations’ data from 2016-2023,
         and some country participation and contestant demographic data from Wikipedia.
         Full citations on data sources can be found in References.
         </p>
         To complete this project, song, vote, betting, and 
         contestant data from referenced sources and 
         data collected through Wikipedia web scraping 
         were extracted and cleaned 
         (e.g., to standardize performer and song names). 
         These data were then combined, as needed, 
         and uploaded to an AWS server and dbt for data 
         transformations into key metrics and collaborative analysis. 
         Visualizations were made using Tableau as well as 
         Matplotlib, nltk, and wordcloud, 
         and the app is powered by Streamlit.
        </p>
        </div>""", unsafe_allow_html=True
    )
 # image
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('./data/pipeline_image.png', width=1000)

    with col3:
        st.write(' ')

    # give some empty spaces in between
    st.markdown("<br><br>", unsafe_allow_html=True)
