import streamlit as st
import streamlit.components.v1 as components

def show_song():
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
        <h1 style="text-align: center; font-size: 30px;">
        Song Characteristics
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
    
# text about song data here
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        How do the musical qualities of songs impact their performance in Eurovision? 
        It turns out that some qualities of songs do influence their chances for success in Eurovision, 
        sadly by playing it safe. 
        Using the visualization below, 
        which utilizes song data from 2009-2023, 
        explore how winning, top 10, and not-top 10 songs vary across different musical variables. 
        Notably, check out how a songs' data distribution for beats per minute, 
        backing singers (i.e., how many people on stage are performing backup vocals), 
        and liveness (a Spotify metric for how present live performance elemtents are) all narrow between not-Top 10 and Top 10, 
        and then again between Top 10 and winners.
        This shows that songs that do better as their measurements for these variables fall within narrower and narrower ranges. 
        In other words, musical creativity, at least by some measures, isn't rewared at Eurovision.
        </div>""", unsafe_allow_html=True
    )

#Song box and whiskers here

    path_to_html = "./htmls/song_characteristics_box.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)
