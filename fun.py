import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
import nltk

def show_fun():
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
        Fun Facts
        </h1>
        """, unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        What's Eurovision without some weird trivia? Here are some of our favorite odd, strange, or just funny findings.
        </div>""", unsafe_allow_html=True
    )

#word cloud title

    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Let, Love, Know: The 100 Most Sung Words in Eurovision History (1956–2023)
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
# text about word cloud
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        First up, what does every Eurovision song have in common? 
        Well, maybe not all of them, but a whole lot certainly use these words.
        Here are the top 100 words used in Eurovision lyrics.
        </div>""", unsafe_allow_html=True
    )

    # Download NLTK data (only needed first time)
    nltk.download('stopwords')

    df = pd.read_csv('./data/contestants.csv')

    def create_lyrics_wordcloud(df, lyrics_col='lyrics', max_words=100):
    
        # Combine all lyrics into one text
        all_lyrics = ' '.join(df[lyrics_col].dropna().astype(str))
        
        # Custom stopwords (excludes from wordcloud)
        custom_stopwords = set(stopwords.words('english')).union({
            'oh', 'ohh', 'yeah', 'yo', 'hey', 'ya', 'uh', 'hmm', 'mmm',
            'la', 'da', 'na', 'chorus', 'verse', 'intro', 'outro', 'repeat',
            'ooh', 'ah', 'ay', 'ha', 'hoo', 'est', 'que'
        })
        
        # Text cleaning
        def clean_lyrics(text):
            # Remove text in brackets (like [Verse 1])
            text = re.sub(r'\[.*?\]', '', text)
            # Remove punctuation and special characters
            text = re.sub(r'[^\w\s]', ' ', text.lower())
            # Remove numbers
            text = re.sub(r'\d+', '', text)
            # Remove extra whitespace
            text = re.sub(r'\s+', ' ', text).strip()
            return text
        
        # Clean the lyrics using the clean_lyrics function
        cleaned_text = clean_lyrics(all_lyrics)
        words = [word for word in cleaned_text.split() 
                if word not in custom_stopwords and len(word) > 2]
        
        # Calculate word frequencies
        word_freq = Counter(words)
        
        # Create word cloud
        wc = WordCloud(
            width=2000,
            height=1000,
            background_color='white',
            colormap='inferno', 
            max_words=max_words,
            stopwords=custom_stopwords,
            contour_width=1,
            contour_color='steelblue'
        ).generate_from_frequencies(word_freq)
        
        # Display
        plt.figure(figsize=(25, 12))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)  

        return wc

    # Generate the word cloud
    wordcloud = create_lyrics_wordcloud(df)

# reciprocity title
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Reciprocity (or Lack Thereof) in Eurovision Voting
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
# text about reciprocity

    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
       We already told you something about how voting in Eurovision is impacted by national politics 
        (don't remember that? Check out Relationships!). But what if we looked at how fair those relationships are? 
        Do countries vote for one another equally? Of course not. Check out the reciprocity in Eurovision voting by country below, 
        as well as the top 10 most uneven relationships since 2016. 
        (Shoutout to the Czech Republic, whose loyalty in voting is never reciprocated).
        </div>""", unsafe_allow_html=True
    )

# reciprocity Dashboard Here

    path_to_html = "./htmls/reciprocity_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=900, width = 1600)
    
# key and country title
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Country by Key
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
    # text about key and country
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        Ever wondered what a country sounds like? 
        Well, it turns out Slovakia loves the key of A Major, 
        because every entry they've sent since 2009 has been in that key. 
        Azerbaijan and Norway, in the meanwhile, really like to mix it up, 
        changing the key of their song almost every year.
        </div>""", unsafe_allow_html=True
    )

    #Key_country Here

    path_to_html = "./htmls/key_country_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=500, width = 1000)

    # winning by year title
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Winning-est Year Ever
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
    # text about first place by year
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        We've already told you about which countries have won the most, but what about which years? 
        1969 blew the competition out of the water, 
        as France, the Netherlands, Spain, and the United Kingdom all took first that year. 
        Sometimes even a competition can be collaborative. 
        </div>""", unsafe_allow_html=True
    )

#first_year Here

    path_to_html = "./htmls/first_year_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=500, width = 1000)

 # gender and lgbtqia+ title
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Musical Choices by Gender and LGBTQIA+ Identity
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
 # text about gender and lgbtqia+ status
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        How does gender and LGBTQIA+ identity impact song choices? See what percentages of all-men, 
        all-women, 
        and mix-gender groups, 
        as well as LGBTQIA+ performers and cisgender, heterosexual performers chose specific musical genres and keys from 2009-2023.
        </div>""", unsafe_allow_html=True
    )

#first_year Here

    path_to_html = "./htmls/gender_dash_html.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)

 # Gender trend across subresions
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 26px;">
        Spotlight on Gender: Who Takes the Stage Where?
        </h1>
        <p style="text-align: center; font-size: 12px; margin-top: -10px;">
        </p>
        """, unsafe_allow_html=True
    )
 # text about gender trends across subregions
    st.markdown(
        """
        <div style="text-align: justify; font-size: 22px;">
        Here you will find 7 subregions that we have created. Why? To see who's sending the boys, the girls, or a diplomatic mix - 
        because nothing says unity like gender trends in a glitter-fueled song contest!
        </div>""", unsafe_allow_html=True
    )

# the line graph Here

    path_to_html = "./htmls/gender_trends_subregions.html" 

    with open(path_to_html,'r') as f: 
        html_data = f.read()

    st.components.v1.html(html_data, scrolling=True, height=1000, width = 1600)

