TOTAL_DECKS_QTY = 778


def load_deck_as_dict(number):
    with open('processed_decks/processed_deck_'+str(number),'r') as d:
        cont = d.read()
        cont = cont.split('\n')
        card_names = [' '.join(c.split(' ')[1:]) for c in cont[1:]]
        card_numbers = [int(c.split(' ')[0]) for c in cont[1:]]
        return {card_names[i] : card_numbers[i] for i in range(len(card_names)) }

def has_card(deck, card):
    return card in deck.keys()

def qty(deck, card):
    try:
        return deck[card]
    except:
        return 0
def get_all_decks(all_decks=[]):
    if all_decks == []:
        all_decks = [load_deck_as_dict(i) for i in range(1,TOTAL_DECKS_QTY)]
    return all_decks

def card_frequency(card):
    return 1.0*len(decks_that_have_card(card))/TOTAL_DECKS_QTY

def combined_frequency(card1,card2,all_decks=[]):
    return 1.0*qty_decks_have_cards(card1,card2,all_decks)/TOTAL_DECKS_QTY

def decks_that_have_card(card,all_decks=[]):
    return [d for d in get_all_decks(all_decks) if has_card(d,card)]

def qty_decks_have_cards(card1,card2,all_decks=[]):
    tot = 0
    decks = decks_that_have_card(card1,all_decks)
    for d in decks:
        if has_card(d,card2):
            tot+=1
    return tot
def decks_that_have_cards(card1,card2,all_decks=[]):
    return [d for d in decks_that_have_card(card1,all_decks) if has_card(d,card2) ]

def get_all_cards():
    keys = [d.keys() for d in get_all_decks()]
    cards = {}
    for k in keys:
        for j in k:
            cards[j]=1
    return cards.keys()

def probability_card1_given_card2(card1,card2,freq,all_decks=[]):
    try:
        fr = freq[card1]
    except:
        freq[card1] = card_frequency(card1)
    return 1.0*combined_frequency(card1,card2,all_decks)/freq[card1]

def generate_all_probs():
    probs = []
    all_decks = get_all_decks()
    cards = get_all_cards()
    freq = {}
    count = 0
    for i in cards:
        count += 1
        for j in cards:
            if i!=j:
                probs.append([i,j,probability_card1_given_card2(i,j,freq,all_decks)])
        print(count)
    return probs

def generate_all_probabilities(card_name):
    probs = []
    freq = {}
    all_decks = get_all_decks()
    cards = get_all_cards()
    for i in cards:
        if i!=card_name:
            probs.append([i,card_name,probability_card1_given_card2(i,card_name,freq,all_decks)])
    return probs

all_probs = generate_all_probs()
with open('final_results','w') as final:
    results = ''
    for a,b,c in all_probs:
        results+= a+'---'+b+'---'+str(c)+'\n'
    final.write(results)
























