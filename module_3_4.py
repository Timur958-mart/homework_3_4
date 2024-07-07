def single_root_words (root_word, *other_words):
    same_words = []
    list_oter_words = list(other_words)


    for j in range(len(list_oter_words)):
        if root_word.lower() in list_oter_words[j].lower() or list_oter_words[j].lower() in root_word.lower():
            same_words.append(list_oter_words[j])
    return(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
