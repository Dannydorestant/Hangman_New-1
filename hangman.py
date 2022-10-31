import random

def getword():
    word_list = ['air', 'apple', 'baby', 'birth', 'cheese', 'connection', 'distribution', 'electric', 'exchange',
                 'feather', 'flower', 'grain', 'gun', 'hanging', 'harbour', 'insurance', 'island', 'journey', 'kettle',
                 'learning', 'liquid', 'material']

    word_index = random.choice(word_list)
    return(word_index)



