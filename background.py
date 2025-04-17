import streamlit as st
import streamlit.components.v1 as components


def show_background():
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
        Background
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        Over time, the competitors in Eurovision have looked very different. 
        Below, you can find visualizations of the first and most recent years that different countries have competed in Eurovision, 
        along with a link to their entry for that year.
        </p>
        </div>""", unsafe_allow_html=True
    )

#Youtube Map Dashboard Here

    path_to_html = "./htmls/background_maps.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)
    
    # top 3 and winners title
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Best in Show
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
    # top 3 and winners text
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        So, who’s winning though? Well, certain countries are definitely doing much better than others at taking home the prize.
        However, when you look at who’s placed 1st, 2nd, and 3rd each year,
         you can see that although some countries aren’t winning,
         they are certainly consistent top finishers.
        </p>
        </div>""", unsafe_allow_html=True
    )

#Top3 Dashboard Here

    path_to_html = "./htmls/background_winners.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)
