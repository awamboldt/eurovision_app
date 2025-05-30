import streamlit as st
import streamlit.components.v1 as components



def show_references():
    # image
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('./data/image.png')

    with col3:
        st.write(' ')
    
    # Title for the references section
    st.title("References")

    # give some empty spaces in between
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Key References:")

    # reference 1
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        2023 John Ashley Burgoyne and Janne Spijkervet and David John Baker,
       'Measuring the {Eurovision Song Contest}: A Living Dataset for Real-World {MIR}.' "
        "Proceedings of the 24th International Society for Music Information Retrieval Conference, Milan, Italy.
        </p>
        </div>""", unsafe_allow_html=True
    )
    st.link_button(url='https://archives.ismir.net/ismir2023/paper/000097.pdf', label = 'Paper Link')
    st.link_button(url='https://github.com/Spijkervet/eurovision-dataset', label = 'Repository Link')

#empty spaces
    st.markdown("<br>", unsafe_allow_html=True)

# reference 2
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        2023 diamondsnake, 'Eurovision Song Contest Data.'
        </p>
        </div>""", unsafe_allow_html=True
    )
    st.link_button(url='https://www.kaggle.com/datasets/diamondsnake/eurovision-song-contest-data', label = 'Repository Link')

#empty spaces
    st.markdown("<br>", unsafe_allow_html=True)

# reference 3
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        2025 Wikipedia, 'List of countries in the Eurovision Song Contest.'
        </p>
        </div>""", unsafe_allow_html=True
    )

    st.link_button(url='https://en.wikipedia.org/wiki/List_of_countries_in_the_Eurovision_Song_Contest', label = 'Page Link')

#empty spaces
    st.markdown("<br>", unsafe_allow_html=True)

# reference 4
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        2025 Wikipedia, 'List of LGBTQ participants in the Eurovision Song Contest.'
        </p>
        </div>""", unsafe_allow_html=True
    )
    st.link_button(url='https://en.wikipedia.org/wiki/List_of_LGBTQ_participants_in_the_Eurovision_Song_Contest', label = 'Page Link')

#empty spaces
    st.markdown("<br>", unsafe_allow_html=True)

# tech stack
    st.subheader("This app was made using:")
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;"> 
        **AWS** 🎾: For cloud storage.</p>
        **dbt** 🪄: For data transformation and analysis.</p> 
        **matplotlib** 🗺️: For word cloud visualizations.</p> 
        **nltk** 🧮: For word cloud visualizations.</p>
        **Pandas** 🐼: For data processing.</p>
        **Python** 🐍: For the backend and for data manipulation.</p>
        **Streamlit** 🌐: For the interactive app interface.</p>
        **Tableau** 📈: For interactive data visualizations.</p>
        **wordcloud** 🌩️: For word cloud visualizations.
        </p>
        </div>""", unsafe_allow_html=True
    )
    st.subheader("Our somewhat sinister self-portrait was AI-generated by Ayla Abdullah.")

#empty spaces
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write("------")
