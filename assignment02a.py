"""
Assignment 2-A
==============

merge assignment01 and assignment02

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():

    chars = ['malt', 'rat,', 'cat,',
            'dog,', 'cow with the crumpled horn,',
            'maiden all forlorn,',
            'man all tattered and torn,',
            'priest all shaven and shorn,',
            "cock that crowed in the morn,",
            'farmer sowing his corn,']

    actions = ['lay in the house that Jack built.\n',
                'ate the malt', "killed the rat,", 'worried the cat,',
                "tossed the dog,", "milked the cow with the crumpled horn,",
                "kissed the maiden all forlorn,",
                "married the man all tattered and torn,",
                "waked the priest all shaven and shorn,",
                "kept the cock that crowed in the morn,"]


    res = "This is the house that Jack built.\n\n"
    for i, char in enumerate(chars):
        res += f'This is the {char}\n'
        for action in reversed(actions[:i+1]):    
            res += f"That {action}\n"
    return res[:-1]


# with open('res.txt', 'w') as file:
#     file.write(poem())
if __name__ == '__main__':
    import doctest
    doctest.testmod()
