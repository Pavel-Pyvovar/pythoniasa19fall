chars = ['malt', 'rat', 'cat',
         'dog', 'cow with the crumpled horn',
         'maiden all forlorn',
         'priest all shaven and shorn',
         "cock that crow'd in the morn",
         'farmer sowing his corn']

actions = ['Jack built,', 'lay in the house that Jack built.',
           'ate the malt,', "kill'd the rat,", 'worried the cat,',
           "tossed the dog,", "milk'd the cow with the crumpled horn,",
           "kissed the maiden all forlorn,",
            "married the man all tatter'd and torn,",
           "waked the priest all shaven and shorn,",
           "kept the cock that crow'd in the morn,"]

print("This is the house that Jack built.\n")
for i, char in enumerate(chars, 1):
    print(f'This is the {char},')
    for action in reversed(actions[1:i+1]):    
        print(f"That {action}")
    print()