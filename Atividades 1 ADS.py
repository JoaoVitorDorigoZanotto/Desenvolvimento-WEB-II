# Crie um algoritmo que receba a idade do usuário, se o usuário tiver 18 anos
# ou mais ele pode fazer a carteira de motorista AB, caso sua idade for maior
# ou igual a 21 anos mostre que ele pode fazer a carteira AB e D, senão ele
# ainda não tem idade suficiente
'''
idade_usuario = int(input("Digite sua idade"))

if idade_usuario == 18 or idade_usuario < 21 and idade_usuario > 18:
                    
    print("Habilitado a fazer a carteira AB")

elif idade_usuario >=21:
    print("habilitado a fazer carteira AB e D")
'''
'''
#OUTRA FORMA DE FAZER
idade_usuario = int(input("informe a idade de usuário"))
if idade_usuario >= 21 and idade_usuario < 100:
    print("você está habilitado a fazer a carteira AB e D")
elif idade >= 18:
    print("Você está apto a fazer somente a CNH AB")
else:
    print("VocÊ não tem idade")
'''

#Atividade 8
#Faça um algoritmo que receba o preço de um item, e a forma
#de pagamento. Calcule o valor final do item seguindo as
#condições abaixo:

# Pagamento A vista – 12% de desconto
# Em até 3x – Preço normal S/juros
# Mais de 3x – 15% de Juros

'''
preco = float(input("Digite o preço:"))
pagamento = int(input("Digite o número de parcelas:"))

if pagamento == 1:
    preco = preco * 0.88
elif pagamento > 3:
    preco = preco * 1.15
    
print("Valor final: R$", preco)

'''


'''
#Faça um algoritmo que calcule o
#IMC (índice de massa corportal) de uma pessoa e mostre
#a sua classificação de acordo com a tabela abaixo:

altura = float(input("Digite sua altura: "))
peso = float(input("digite seu peso, será que é imenso: "))

imc = peso / altura**2
print(imc)

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc > 18.6 and imc < 24.9:
    print(" Parabéns, você está na tropa do saudável")
elif imc > 25 and imc< 29.9:
    print(" Opa, pera ai meu querido , larga esse pão, só o café")
elif imc > 30 and imc< 34.9:
    print("Perigo, está com obesidade meu querido, calma no churrasco")
elif imc > 35 and imc< 39.9:
    print("Bem vindo a tropa do gordão, ruim")
elif imc >= 40:
    print("Compra um caixão aí, logo vai")


'''

'''
Frete grátis:
valor da compra ≥ 200
OU(or)
cliente tiver CUPOM
Caso não tenha frete grátis:
Região sul ou sudeste - R$10
Outras regiões - R$20

'''

'''Atividade 4
Um sistema possui 3 níveis:
admin - acesso total
professor - acesso intermediário
aluno - acesso básico
A senha deve ser "123"
Caso usuário ou senha estejam errados - acesso negado'''

usuario = input("Digite seu usuário (Aluno/Professor/Admin")
senha = input("Digite sua senha numérica")

if usuario == admin and senha == 123:
    print("Acesso total liberado com sucesso")
elif usuario == aluno and senha == 123:
    print("Acesso básico liberado com sucesso")
elif usuario == Professor and senha 123:
    print("Acesso intermediário liberado com sucesso")
    
else:
    print("Não há cadastro")
    











''' Atividade 5 
valor_compra = float(input("Valor da compra: "))
regiao = input("Região (Sul/Sudeste/Norte/Nordeste/Centro-oeste):")
cupom = input("Cupom? (sim/não):")
retirada = input("Retirada na loja? (sim/não): ")

if retirada == "sim":
    frete = 0
elif valor_compra >= 200 or cupom == "sim":
    frete = 0
elif regiao == "sul" or regiao == "sudeste":
    frete = 10
else:
    frete = 20

print("Valor total do frete:", frete)
'''



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
