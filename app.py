import streamlit as st

import story_engine as se

### defines card set names for csv files
card_sets = {
    'Horror' : 'horror_cards',
    'Politics' : 'politics_cards',
    'Sci-Fi' : 'sci-fi_cards'
}

st.set_page_config(page_title="Story Engine", page_icon="", layout='wide')
st.title('Story Engine Generator')
st.markdown('Use this to convert a simple csv file to the format needed for the Story Engine Web app')


col1, col2 = st.columns([1,1])

with col1:
    card_set_choice = st.selectbox(
        'Select a Card Set',
        ('Horror','Politics','Sci-Fi'))

    card_set = card_sets[card_set_choice]
with col2:
    n_stacks = st.number_input('How many stacks do you want?', min_value=1, max_value=10, value=3)

st.write('Your batch will include ', n_stacks, ' stacks from the ', card_set_choice, 'card set')

filename = 'story_generator'
engine_type = 'story' ## Only option for now

se.generate_card_batch_file(card_set, n_stacks, filename, engine_type)

st.text(open('story_generator.txt', 'r+').read())

with open('story_generator.txt', 'r+') as file:
     btn = st.download_button(
             label='Download Output as Text File',
             data=file,
             file_name='story_generator',
             mime='text/'
           )