#Task2
def count_words(sentence):
    new_str=''
    for i in sentence:
        if i.isalnum() or i ==' ':
            new_str+=i
        
    words = new_str.split()
    return len(words)

sentence = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."
result = count_words(sentence)
print(result)
