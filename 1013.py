linha = list(map(int, input().split()))

linha.sort()

maior = linha.pop()

print(f"{maior} eh o maior")
