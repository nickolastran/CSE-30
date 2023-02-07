def make_dict (dict_file):
    dictionary = {}
    for x in dict_file:
        if len(x) <= 10:
            word_size = len(x)
        else:
            word_size = 10
        try:
            dictionary[word_size].append(x)
        except:
            dictionary[word_size] = [x]
    return dictionary

if __name__ == '__main__':

    d = {2: ['at', 'to', 'no'], 3: ['add', 'sun'], 10: ['Hello! How are you?']}
    dictionary = make_dict(['at', 'add', 'sun', 'to', 'no', 'Hello! How are you?'])
    print(dictionary)
    assert dictionary == d
    print('Everything works correctly!')
