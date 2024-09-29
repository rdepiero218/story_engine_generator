import streamlit as st

import story_engine as se

### defines card set names for csv files
card_sets = {
    'Horror' : 'horror_cards',
    'Politics' : 'politics_cards',
    'Sci-Fi' : 'sci-fi_cards',
    'World' : 'world_deck'
}

st.set_page_config(page_title="Story Engine", page_icon="", layout='wide')
st.title('Story Engine Generator')
st.markdown('A super basic digital version of the story engine card deck.')


col1, col2 = st.columns([1,1])

with col1:
    card_set_choice = st.selectbox(
        'Select a deck',
        ('Horror','Politics','Sci-Fi','World'))

    card_set = card_sets[card_set_choice]
with col2:
    n_stacks = st.number_input('How many stacks do you want?', min_value=1, max_value=10, value=3)

st.write('Your batch will have ', n_stacks, ' stacks from the ', card_set_choice, ' deck.')

filename = 'story_generator'

if card_set_choice == 'World':
    engine_type = 'world' ## Only option for now
else:
    engine_type = 'story' ## Only option for now

se.generate_card_batch_file(card_set, n_stacks, filename, engine_type)

if st.button('Generate!'):
    st.text(open('story_generator.txt', 'r+').read())

    with open('story_generator.txt', 'r+') as file:
        btn = st.download_button(
                label='Download Output as Text File',
                data=file,
                file_name='story_generator',
                mime='text/'
            )