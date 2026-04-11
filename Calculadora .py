
#Entrada de dados do Usuario
def usuario_entrada():
    entrada_1= float(input("Digite um numero: "))
    print()
    entrada_2= float(input("Digite outro numero: "))
    print()
    return entrada_1, entrada_2

#Escolha da opereção matematica 
def simbulos():
    print()
    escolha_sim= str(input("Escolha uma operação matematica:  [MAIS +] .  [MENOS -] . [DIVISÃO /] . [MULTIPLICAÇÃO *]   = " ))      
    return  escolha_sim

#Operações matematicas disponiveis
def operação_mais(valor_1, valor_2):
    soma= valor_1+valor_2
    return soma

def operação_menos(valor_1, valor_2):
    menos= valor_1+valor_2
    return menos

def operação_divisao(valor_1, valor_2):
    divisao= valor_1+valor_2
    return divisao

def operação_multiplicaçao(valor_1, valor_2):
    multiplicaçao= valor_1+valor_2
    return multiplicaçao


valor_1, valor_2= usuario_entrada ()
sim= simbulos()

if sim=="+":
    soma= valor_1+valor_2
    print (f"O resultado é {soma} ")

elif sim=="-":
      menos=valor_1-valor_2 
      print (f"O resultado é {menos}")

elif sim=="/":
      divi=valor_1/valor_2 
      print (f"O resultado é {divi}")

elif sim=="*":
      mult=valor_1*valor_2 
      print (f"O resultado é {mult}")            