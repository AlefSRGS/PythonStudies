dict={}
text = input()
for i in text:
    qnt_words = text.count(i)
    dict[i]=qnt_words
x=sorted(dict.items(),reverse=True)
for i in x:
    print(i[0],i[1])