

def parseHTMLDeck(deck):
    output = ''
    saving = True
    numbers = False
    for i in deck:
        if i=='<':
            saving = False
        if saving:
            if i in [str(j) for j in range(10) ]:
                if numbers==False:
                    output+='\n'
                numbers = True
            else:
                if numbers:
                    numbers = False
            output+=str(i)
        if i=='>':
	        saving = True
    return output

for k in range(1,778):
	with open('./decks/deck_table'+str(k)+'.html','r') as f:
		contents = f.read()
        newContents = parseHTMLDeck(contents)
        with open('formatted_deck_'+str(k),'w') as op:
            op.write(newContents) 

