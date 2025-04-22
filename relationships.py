import streamlit as st
import streamlit.components.v1 as components


def show_relationships():
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
        Relationships
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        But what about just good, old fashioned politics? 
        It turns out, in Eurovision, some competitors start with an advantage just because of where they’re from. </p>
        Using each year’s votes, we wanted to see if we could find a pattern between which countries vote for which other countries. 
        After all, if some countries are just more likely to give their votes to others, 
        then that could be an important factor in who wins. 
        </p>
        To find out, 
        we wanted to know how many points any given country 
        (e.g., Germany) gave to another given country 
        (e.g., France) each year in years that both competed. 
        This amount was then divided by the total maximum number of points* that a country could have awarded that year. 
        So, for example, if Germany gave France 6 points one year, 
        when the maximum number of points was 12, then its relationship for that year would be 0.5. 
        </p>
        Then, 
        we calculated the mean of that voting point ratio across a given amount of years 
        to show the relative likelihood that one country would cast their votes for another during that time span. 
        To use our same example, 
        if Germany’s mean voting ratio with France from 1980-2015 was 0.20, 
        then that indicates that, regardless of France’s entry in a given year, 
        Germany would award France roughly 2 points (2.4) in an average year.
        </p>
        Using these mean voting scores, 
        it is then possible to calculate a country’s popularity across all countries by taking a mean of all mean voting ratios for a given country. 
        So, for example, using France again, 
        between the years 1980 and 2015, 
        it has a mean voting ratio of 0.18 across all countries, 
        meaning that between those years, countries, on average, 
        gave France 2 points (2.2) in an average year. 
        That might sound good, until you see that Russia (score of 0.32), 
        during that same time period 
        (though Russia joined Eurovision much later) was receiving nearly 4 points 
        (3.8) on average from each country in an average year! 
        In other words, some countries, statistically, are just more likely to get points from their peers.
        </p>
        You can also invert an individual country’s mean voting ratios to see which countries are more (or less) popular with other countries, 
        or what we call a popularity ratio. 
        France during this same time period, for example, has its highest popularity ratios from Monaco, Andorra, and Armenia.
        </p>
        In summary: </p>
        1) Calculate the percentage of points awarded out of the amount possible awardable points by Country 1 to Country 2. </p>
        2) Calculate the mean of that ratio for all years Country 1 and Country 2 participated to see which countries Country 1 is most likely to vote for. </p>
        3) Compare countries' popularity by seeing which ratios are higher/lower for Country 2 (by Country 1, 3, 4, etc). </p>
        </div>""", unsafe_allow_html=True
    )

#Relationship Dashboard Here

    path_to_html = "./htmls/relationship_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)

#empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")

    st.markdown(
        """
        <div style="text-align: justify; font-size: 20px;">
        </p>
        *Eurovision has changed its scoring system several times. 
        Prior to 1980, juries appointed by each country awarded points to their favorite songs 
        (the number of points awarded depended on the year, 
        as the competition tried numerous scoring systems in its early years, 
        ranging from the highest possible scores of 3-10). 
        In 1980, the competition implemented its now famous 1-8, 10, and 12 point system, 
        and, starting in 1997, combinations of juries and tele-audience votes were used. 
        In 2016, the competition once again switched voting systems, 
        now having a national jury and the tele-audience each awarding 1-8, 10, and 12 points, 
        for a possible high score of 24. And in 2023, the system was once again changed, 
        using only the audience vote for the semi-finals, but a combined jury and audience vote for the finals. 
        And even this is still an oversimplified version!
        </div>""", unsafe_allow_html=True
    )
