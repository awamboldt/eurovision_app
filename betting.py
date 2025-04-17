import streamlit as st
import streamlit.components.v1 as components

def show_betting():
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
        Betting on Eurovision: A Culture of Predictions and Surprises
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        Each year, as the Eurovision Song Contest draws near, fans across Europe - and beyond - start placing their bets. Eurovision has become more than just a musical competition;
        it's a spectacle of culture, performance and passionate predictions. Betting companies have capitalized on this excitement, offering odds on potential winners, finalists,
        and even who might come in last. While some companies consistently cover the event, others dip in and out, and not all ofer bets on every country or every year.
        </p>
        </div>""", unsafe_allow_html=True
    )

# Intro table

    st.markdown(
    """
    <div style="text-align: justify; font-size: 22px;">
        In this section, we’ll take a closer look at how the betting landscape has evolved over the years. 
        Specifically, we’ll explore:</p>
            1) Which countries placed in the top 3 each year?</p>
            2) How did various betting companies position their odds for those years?</p>
            3) How closely did those predictions align with the actual results?</p>
        Let’s explore whether the bookies saw it coming—or if Eurovision did what it does best: deliver the unexpected.</p>
    </div>
    """, unsafe_allow_html=True
)

# INSERT BETTING TABLE WITH ODDS

    path_to_html = "./htmls/betting_table.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)

    # give some empty spaces in between
    st.markdown("<br><br>", unsafe_allow_html=True)

# INSERT POWER REGRESSIONS 
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Regression Royale: Betting Odds vs. Final Glory
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        To dive deeper, we've used <strong>power regression models</strong> to analyze the relationship between betting odds and final placements—helping us understand just how predictive (or not) the odds really were.
        </p>
        </div>""", unsafe_allow_html=True
    )

    path_to_html = "./htmls/betting_dashboard.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1400)

    # give some empty spaces in between
    st.markdown("<br><br>", unsafe_allow_html=True)
    
