import os

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists


filename = "files/teste.txt"

if (os.path.exists(filename)):
  os.remove(filename) # Remove o arquivos


file = open(filename, "w") # w de write/escrever
file.writelines("Escrita com w de write\n")

file.close()

file = open(filename, "r") # r de read/leitura
conteudo = file.read()
print(conteudo)
file.close()


file = open(filename, "a") # a de append/adicionar
file.writelines("Segunda linha com append\n")
file.close()

file = open(filename, "r") # r de read/leitura
conteudo = file.read()
print(conteudo)
file.close()

os.remove(filename)

#file = open(filename, "x")        # Cria arquivo se não existir
#print(file)








