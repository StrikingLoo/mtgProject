for k in range(1,778):
    with open('formatted_decks/formatted_deck_'+str(k),'r') as d:
        lines = d.read().split('\n')
        lines = [l for l in lines if (('LAND' not in l) and ('SPELL' not in l) and ('SORC' not in l) and ('CREATURE' not in l)) ]
        cont = '\n'.join(lines)
        with open('processed_decks/processed_deck_'+str(k),'w') as f:
            f.write(cont)

