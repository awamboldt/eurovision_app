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
        Each year, as the Eurovision Song Contest draws near, fans across Europe - and beyond - start placing their bets. 
        Betting companies have capitalized on this excitement, offering odds on potential winners, finalists,
        and even who might come in last. We have betting organisations' data for the years 2016 - 2023. 
        While some companies consistently cover the event, others dip in and out, and not all ofer bets on every country or every year. 
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
        To dive deeper, we've used <strong>power regression models</strong> to analyze the relationship between betting odds and final placements—helping us understand 
        just how predictive (or not) the odds really were. <strong>Power Regression</strong> is a type of nonlinear regression used when the relationship between two variables
        follows: <strong>y = a.x^b</strong> </p>
        This model is useful when the effect of x on y increases or decreases non-linearly i.e., <strong>how strongly betting odds predict outcomes but in a non-linear way.</strong></p>
        Here, the curve flattens out for higher odds (more underdog entries), showing that beyond a point, odds lose predictive power 
        (i.e., a song with odds of 300 doesn’t perform much worse than one with 400 — both are long shots).</p>
        <strong>R-squared = 0.717 means ~71.7% of the variation in final placements is explained by the betting odds using this power regression model.</strong> 
        That’s a very strong relationship — especially in social/cultural data like Eurovision, which has many unpredictable elements (public taste, juries, politics, performance quality).
        A p-value of < 0.0001 indicates the model’s fit is statistically significant — the probability that this result is due to random chance is less than 0.01%.
        </p>
        </div>""", unsafe_allow_html=True
    )

    path_to_html = "./htmls/betting_dashboard.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1400)

    # give some empty spaces in between
    st.markdown("<br><br>", unsafe_allow_html=True)
    
