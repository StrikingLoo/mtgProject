A set of Spiders for crawling mtgtop8, a Website dedicated to compiling and documenting the state of Meta in Magic: The Gathering.

The first spider compiles all 'Archetypes' an internal division of decks done by the site (though typical of the game).
The second one crawls archetypes for a list of 'events' where different decks are played.
The third and last one, finally, crawls the list of decks used in each event and saves the cards' names in a text file, making analysis possible.

The scripts I made for the processing and analysis of the collected dataset, and the small recommender system (based in simple Bayesian models, nothing too fancy), helped me realize how stale and static the MtG Meta is, and how useless a recommender system would be on encouraging creativity, since most of the combos and synergies are already discovered and explored.

Generating a dataset of casual decks, or budget ones, will be an interesting project for the future, if I ever come back to it.

