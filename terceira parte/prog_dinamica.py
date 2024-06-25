def cof_bin(n, k):
  if k == 0 or k == n:
    return 1
  else:
    print(n, k)
    return (cof_bin(n-1, k-1) + cof_bin(n-1, k))

#print(cof_bin(5,2))

#print("-----------")

def coeficiente_bin(n, m):
    # Cria um array de tamanho n+1 inicializado com 0
    b = [0] * (n + 1)
    
    # Define o primeiro elemento como 1, que é o caso base
    b[0] = 1
    
    # Itera sobre os valores de 1 até n
    for i in range(1, n + 1):
        b[i] = 1
        # Atualiza o array de trás para frente
        for j in range(i - 1, 0, -1):
            b[j] = b[j] + b[j - 1]
            print(b[i], b[j])
    
    # Retorna o coeficiente binomial desejado
    return b[m]

n = 5
m = 2
#print(f"C({n}, {m}) = {coeficiente_bin(n, m)}") 
preco = [1,5,8,9,10,17,17,20]
def corte(a, b):
  for i in range(1, a + 1):
    for j in range(1, a +1):
      print(i + j)
      if(i + j == a):
        print(f"preço 1 {preco[i]}")
        print(f"preco 2 {preco[j]}")
        b = preco[i] + preco[j]
        break;
    #for j in range(i, a):
  print()
  return b
    
print(corte(4, 9))   