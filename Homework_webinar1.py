def count_words(sentence):
    words = sentence.split()
    words.remove('—')
    return len(words)

sentence = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."
result = count_words(sentence)
print(result)