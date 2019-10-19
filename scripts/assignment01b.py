import re
"""
Assignment 1-B (optional)
=========================

This assignment is similar to 1-A except that the poem is in Russian now.

>>> print(poem())

"""

actors = ('пшеница',
            'весёлая птица-синица,',
            'кот,', 'пёс без хвоста,',
            'корова безрогая,',
            'старушка, седая и строгая,',
            'ленивый и толстый пастух,',
            'два петуха,')

actions = ('в тёмном чулане хранится',
            'часто ворует пшеницу,',
            'пугает и ловит синицу,',
            'за шиворот треплет кота,',
            'Лягнувшая старого пса без хвоста,',
            'доит корову безрогую,',
            'бранится с коровницей строгою,',
            'будят того пастуха,')

def manage_end(actor, action):
    if re.match('/[уая],$/g', actor):
        return 'Которая ' + action + '\n'
    else:
        return 'Который ' + action + '\n'

print(manage_end('весёлая птица-синица,', 'часто ворует пшеницу,'))
def poem():
    poem = ''
    poem += 'Вот дом, который построил Джек.\n\n'
    for i, actor in enumerate(actors):
        poem += 'А это ' + actor + '\n'
        poem += manage_end(actor, actions[i])
        for j, a in enumerate(reversed(actors[:i])):
            poem += manage_end(a, actions[j])
        poem += '\n'
    return poem

# print(poem())
# if __name__ == '__main__':
#     # import doctest
#     # doctest.testmod()
#     print(poem())