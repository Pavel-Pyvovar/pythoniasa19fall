"""
Assignment 2-A
==============

merge assignment01 and assignment02

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('../data/poem-en.txt').read_text()
True
"""

def poem():
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

    story = "This is the house that Jack built.\n"

    for i, char in enumerate(chars):
        story += '\n'
        if char != 'malt':
            story += f'This is the {char},' + '\n'
        else:
            story += f'This is the {char}' + '\n'
        for action in reversed(actions[:i+1]):    
            story += f"That {action}" + '\n'
    return story


if __name__ == '__main__':
    # print(poem())
    # with open('mypoem.txt', 'w') as f:
    #     f.write(poem())
    import doctest
    doctest.testmod()
