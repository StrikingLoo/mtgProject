for k in range(1,778):
    with open('formatted_deck_'+str(k), 'r') as f:
        cnts = f.read()
        cnts = cnts.split('SIDEBOARD')[0]
    with open('formatted_deck_'+str(k), 'w') as f:        
        f.write(cnts)
