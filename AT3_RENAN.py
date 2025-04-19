# Dicionário com as notas de alguns alunos
notas = {'Teo': 8.5, 'Cristiano': 8.9, 'Matson': 7.7}

# 1- Exiba a nota do aluno Matson
print(notas['Matson'])

# 2- Adicione um novo aluno chamado "Bruna" com a nota 8.7
notas['Bruna'] = 8.7

# 3- Atualize a nota do aluno "Teo" para 9.2
notas['Teo'] = 9.2

# 4- Verifique se o aluno "Carlos" está no dicionário
print('Carlos' in notas)

# 5- Apague o aluno "Matson" do dicionário
del notas['Matson']

# 6- Adicione dois novos alunos com notas à sua escolha
notas['Larissa'] = 9.0
notas['João'] = 7.5

# 7- Mostre todas as chaves (nomes dos alunos)
print(notas.keys())

# 8- Mostre todos os valores (notas dos alunos)
print(notas.values())

# 9- Use o método .get() para tentar buscar a nota de "Islla", e retorne "Aluno não encontrado" caso ele não exista
print(notas.get('Islla', 'Aluno não encontrado'))

# 10- Use o método .get() para tentar buscar a nota de algum aluno, e a retorne
print(notas.get('Cristiano'))
