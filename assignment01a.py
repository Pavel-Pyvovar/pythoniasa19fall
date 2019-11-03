chars = ['malt', 'rat', 'cat',
        'dog', 'cow with the crumpled horn',
        'maiden all forlorn',
        'man all tattered and torn',
        'priest all shaven and shorn',
        "cock that crowed in the morn",
        'farmer sowing his corn']

actions = ['lay in the house that Jack built.',
            'ate the malt', "killed the rat,", 'worried the cat,',
            "tossed the dog,", "milked the cow with the crumpled horn,",
            "kissed the maiden all forlorn,",
            "married the man all tattered and torn,",
            "waked the priest all shaven and shorn,",
            "kept the cock that crowed in the morn,"]

print("This is the house that Jack built.\n")
for i, char in enumerate(chars):
    print(f'This is the {char},')
    for action in reversed(actions[:i+1]):    
        print(f"That {action}")
    print()