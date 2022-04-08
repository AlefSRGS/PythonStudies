lista_a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
lista_b = [1, 2, 3]

#max min sum da lista_a
print("lista_a" + str(lista_a))
print("max {} min {}, sum {} \n".format(max(lista_a), min(lista_a), sum(lista_a)))

#dos 5 primeiros numeros da lista_a
print("dos 5 primeiros "+str(lista_a[:5]))
print("max {} min {} sum {} \n".format(max(lista_a[:5]), min(lista_a[:5]), sum(lista_a[:5])))

#do 3° ate o 6° numero da lista_a
print("dos 5 primeiros "+str(lista_a[2:6]))
print("max {}, min {}, sum {} \n".format(max(lista_a[2:6]), min(lista_a[2:6]), sum(lista_a[2:6])))

#dos 5 ultimos numeros da lista_a
print("dos 5 ultimos "+str(lista_a))
print("print(max {}, min {}, sum {} \n".format(max(lista_a[-5:]), min(lista_a[-5:]), sum(lista_a[-5:])))

#da concatenação da lista_a com a lista_b
print("Da concatenação "+str(lista_a + lista_b))
print("print(max {}, min {}, sum {} \n".format(max(lista_a + lista_b), min(lista_a + lista_b), sum(lista_a + lista_b)))

#da multiplicação da lista_b por 2
print("Da multiplicação da lista_b "+str(lista_b * 2))
print("print(max {}, min {}, sum {} \n".format(max(lista_b * 2), min(lista_b * 2), sum(lista_b * 2)))