from random import choices, choice
from string import digits, ascii_letters
from assignment03c import validate
from collections import Counter
"""
Create a function that would generate randomly
correct passwords
"""

def gen_password():
    """
    >>> validate(gen_password())
    True
    """
    return ''.join(choices(ascii_letters + digits + '@#$', k=choice([i for i in range(6, 13)])))

cnt = Counter()
for i in range(100):
    cnt[validate(gen_password())] += 1

print(cnt)
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()    
