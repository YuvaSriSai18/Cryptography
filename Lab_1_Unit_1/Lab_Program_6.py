import string
def generate_matrix(key):
    key = key.lower().replace('j', 'i') 
    key = ''.join(dict.fromkeys(key))  

    playfair_matrix = []
    used_characters = set(key)  

    for char in key:
        playfair_matrix.append(char)

    for char in string.ascii_lowercase:
        if char not in used_characters and char != 'j':
            playfair_matrix.append(char)

    playfair_matrix = [playfair_matrix[i:i+5] for i in range(0, 25, 5)]

    return playfair_matrix

# matrix = generate_matrix('monarchy')
# for row in matrix:
#     print(' '.join(row))
"""
    m o n a r
    c h y b d
    e f g i k
    l p q s t
    u v w x z
"""