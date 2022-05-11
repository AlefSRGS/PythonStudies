import numpy as np

#criação de matrizes com array em numpy
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print('-'*50)
#verificar as dimensões da matriz
print(a.shape)
print('-'*50)

#criação de matrizes aleatorias
random = np.random.rand(3,3)
print(random)
print('-'*50)

#outro modo de declarar matrizes ou vetores se tiver sem o .reshape
vetorA = np.arange(12).reshape(6,2)
print(vetorA)
print('-'*50)

#criação de matrizes compostas apenas por 0
zeros = np.zeros((3,3))
print(zeros)
print('-'*50)

#criação de matrizes compostas apenas por 1
ones = np.ones((3,3))
print(ones)
print('-'*50)

#se quiser mudar os numeros da matriz
nNumber = np.ones(3)*5
print(nNumber)
print('-'*50)

#formatação de matrizes de compostas por zeros mas com a diagonal diferente de zero
matrizDiagonal = np.diag([1,2,3,4,5,6])
print(matrizDiagonal)
print('-'*50)

#criação de matrizes identidade
identidade = np.identity(3)
print(identidade)
print('-'*50)

#buscar elementos numa matriz
print(a[1,0])
print(a[1][0])
print(a[-1,0])
print(a[-1][0])
print('-'*50)

#buscar uma coluna especifica 
print(a[:,1])
##buscar uma coluna especifica menos o ultimo numero
print(a[:2,1])
##buscar uma coluna especifica menos o ultimo e o primeiro numero
print(a[1:2,1])
print('-'*50)

#calculando a inversa de uma matriz 
inversaA = np.linalg.inv(a)
print(inversaA)
#calculando a determinante de uma matriz 
determinanteA = np.linalg.det(a)
print(determinanteA)
#calculando a matriz transposta
print(a.transpose())
#ou
print(a.T)
print('-'*50)

#operações básicas
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.array([[11,12,13],[14,15,16],[17,18,19]])
#adição e subtração 
print(x+y)
print(x-y)
#multiplicação
print(np.dot(x,y))
#divisão 
print(np.dot(x,np.linalg.inv(y)))