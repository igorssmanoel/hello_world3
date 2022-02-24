## Listas

# Exibir o primeiro valor da lista


lista = ["Igor", "Weyner", "Fabricio", "Ricardo", "Mariana"] #Declaração da lista
#           0       1           2          3          4

tamanhoLista = len(lista) # Tamanho da lista


print(f"O tamanho da lista é {tamanhoLista}")

primeiro = lista[0]     # Primeiro item da lista
print(primeiro)

ultimo = lista[tamanhoLista - 1]    # Ultimo item da lista
print(ultimo)


lista.append("Item adicionado")  # Adiciona item na lista

print("Imprimindo a lista")

print("Lista original: ",lista)

lista.pop() # Remove o ultimo item da lista

print("Lista semo ultimo item: ",lista)

del lista[0]  # Remove item pelo index

print("Lista com o item 0 removido: ",lista)

lista.reverse() # Inverte a ordem da lista

print("Lista ao contrario: ",lista)

lista.sort()  # Ordena a lista

print("Lista ordenada: ",lista)


#Imprimir a lista
for item in lista:
  print("Item da lista", item)
#Imprime a lista pelo index
for i in range(0, len(lista)):
  print(f"Item da lista pelo index {i}", lista[i])


