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

def convert_str_to_list(string):
    a = []
    for i in range(0, len(string), 2):
        if i + 1 < len(string): 
            a.append(string[i] + string[i + 1]) 
        else:
            a.append(string[i] + 'z')
    return a


def find_index(matrix, element):
    for row_index, row in enumerate(matrix):
        if element in row:
            col_index = row.index(element)
            return row_index, col_index
    return None 

# matrix  = generate_matrix('Monarchy')
# str_list = convert_str_to_list('instruments')

# for row in matrix:
#     print(' '.join(row))

def diagonalRule(matrix , row_1 , col_1,row_2 , col_2):
    a = matrix[row_1][col_2]
    b = matrix[row_2][col_1]
    return a + b

# print(diagonalRule(matrix , 2 , 3 , 0 , 2))

def rowRule_Encrypt(matrix, row_1, col_1, row_2, col_2):
    if col_1 == 4:
        col_1 = 0
    else:
        col_1 += 1 

    if col_2 == 4:
        col_2 = 0
    else:
        col_2 += 1 

    a = matrix[row_1][col_1]
    b = matrix[row_2][col_2]

    return a + b

# print(rowRule_Encrypt(matrix , 1 , 0 , 1 , 4))

def colRule_Encrypt(matrix, row_1, col_1, row_2, col_2):
    if row_1 == 4:
        row_1 = 0
    else:
        row_1 += 1
    
    if row_2 == 4:
        row_2 = 0
    else:
        row_2 += 1
    a = matrix[row_1][col_1]
    b = matrix[row_2][col_1]
    
    return a + b

# print(colRule_Encrypt(matrix , 1 , 1 , 3 , 1))

def rowRule_Decrypt(matrix, row_1, col_1, row_2, col_2):
    if col_1 == 0:
        col_1 = 4
    else:
        col_1 -= 1 

    if col_2 == 0:
        col_2 = 4
    else:
        col_2 -= 1 

    a = matrix[row_1][col_1]
    b = matrix[row_2][col_2]

    return a + b

def colRule_Decrypt(matrix, row_1, col_1, row_2, col_2):
    if row_1 == 0:
        row_1 = 4
    else:
        row_1 -= 1
    
    if row_2 == 0:
        row_2 = 4
    else:
        row_2 -= 1
    a = matrix[row_1][col_1]
    b = matrix[row_2][col_1]
    
    return a + b

def encrypt(plain_text , key):
    matrix = generate_matrix(key)
    for row in matrix:
        print(' '.join(row))
    text_list = convert_str_to_list(plain_text)
    cipher_text = ''
    for word in text_list:
        row_1 , col_1 = find_index(matrix , word[0])
        row_2 , col_2 = find_index(matrix , word[1])
        
        if row_1 != row_2 and col_1 != col_2:
            cipher_text += diagonalRule(matrix , row_1 , col_1 , row_2 , col_2)
        if row_1 == row_2 and col_1 != col_2:
            cipher_text += rowRule_Encrypt(matrix , row_1 , col_1 , row_2 , col_2 )
        if row_1 != row_2 and col_1 == col_2:
            cipher_text += colRule_Encrypt(matrix , row_1 , col_1 , row_2 , col_2)
    return cipher_text

def Decrypt(cipher_text , key):
    matrix = generate_matrix(key)
    for row in matrix:
        print(' '.join(row))
    text_list = convert_str_to_list(cipher_text)
    plain_text = ''
    for word in text_list:
        row_1 , col_1 = find_index(matrix , word[0])
        row_2 , col_2 = find_index(matrix , word[1])
        
        if row_1 != row_2 and col_1 != col_2:
            plain_text += diagonalRule(matrix , row_1 , col_1 , row_2 , col_2)
        if row_1 == row_2 and col_1 != col_2:
            plain_text += rowRule_Decrypt(matrix , row_1 , col_1 , row_2 , col_2 )
        if row_1 != row_2 and col_1 == col_2:
            plain_text += colRule_Decrypt(matrix , row_1 , col_1 , row_2 , col_2)
    return plain_text

# print(encrypt('instruments' , 'monarchy'))
# print('Decrypted Message : ')
# print(Decrypt('gatlmzclrqtx' , 'monarchy'))