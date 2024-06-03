'''
Crie um programa que o usuário possa escolher se deseja saber a área se um circulo, de um triangulo ou de um trapézio.
'''

# Formula do círculo
def formula_circulo():
    return 'Área do Círculo: A = π * r²'

# Fórmula da área de um triângulo
def formula_triangulo():
    return 'Área do Triângulo: A = (base * altura) / 2'

# Fórmula da área de um trapézio
def formula_trapezio():
    return 'Área do Trapézio: A = ((base maior + base menor) * altura) / 2'

# Menu para escolher a fórmula
def menu():
    while True:
        print('Escolha uma opção para exibir a fórmula da área: ')
        print('1. Círculo: ')
        print('2. Triângulo: ')
        print('3. Trapézio: ')
        print('4. Sair: ')

        opcao = input('Opção: ')
        
        if opcao == '1':
            print(formula_circulo() + '\n')
        elif opcao == '2':
            print(formula_triangulo() + '\n')
        elif opcao == '3':
            print(formula_trapezio() + '\n')
        elif opcao == '4':
            break
        else:
            print('Opção inválida!!! Tente novamente.\n')

# Executando o menu principal
menu()