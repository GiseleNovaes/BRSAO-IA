

#verifica se a pessoa é maior de 18 anos

def verifica_idade(idade):
    if idade>=18:
        print('Você é maior de 18 anos')
    else:
        print('Você não é maior de 18 anos')
        return idade

idade = int(input('Digite a sua idade: '))
idade_usuario = (idade)

print(f'Você informou que tem {idade_usuario} anos.') 

verifica_idade(idade_usuario)


