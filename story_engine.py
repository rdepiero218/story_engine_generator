import pandas as pd
import numpy as np



def create_card_database(card_set_name, engine_type):
    ### create dict of cardtypes for given cardset
    df = pd.read_csv(f'./data/{card_set_name}.csv')
    if engine_type =='world':
        df = df[['region','landmark','origin', 'namesake', 'attribute', 'advent']]
    else:
        df = df[['aspect','agent','engine', 'anchor', 'conflict']]
        
    card_set = {}
    card_types = df.columns.to_list()
    for card_type in card_types:
        card_set[card_type] = df[card_type].dropna(how = 'any')
    return card_set

def get_card_stack(card_set, printer=False):
    card_stack = {}
    for card_type in card_set:
        card_stack[card_type] = card_set[card_type].sample().to_string(index=False)
    if printer:
        for card_type in card_stack:
            print('Your %s:  %s'%(card_type, card_stack[card_type]))
    return card_stack

def get_batch_cards(n, card_set, printer=False):
    card_batch = []
    for card_stack in range(0,n):
        card_batch.append(get_card_stack(card_set))
        
    if printer:
        for card_stack in range(0,len(card_batch)):
            print('---------------')
            print('Card Stack %d'%(card_stack+1))
            print('---------------')
            for key in card_batch[card_stack].keys():
                print('Your %s: %s'%(key, card_batch[card_stack][key]))
    return card_batch

def card_set_tofile(card_batch, filename):
    card_set = open(fr'./{filename}.txt','w')
    
    for card_stack in range(0,len(card_batch)):
            card_set.write('---------------\n')
            card_set.write('Card Stack %d\n'%(card_stack+1))
            card_set.write('---------------\n')
            for key in card_batch[card_stack].keys():
                card_set.write('Your %s: %s\n'%(key, card_batch[card_stack][key]))
    card_set.close()

    return

def generate_card_batch_file(choice, n_stacks, filename, engine_type):
    ## create card set database
    card_set = create_card_database(choice, engine_type)
    ## generate a batch of card stacks
    card_batch = get_batch_cards(n_stacks, card_set)
    ## write card batch to text file
    card_set_tofile(card_batch, filename)
    return