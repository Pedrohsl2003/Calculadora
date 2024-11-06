import math
from collections import Counter
import sympy as sp
import cmath
import numpy as np

# Funções básicas de operações matemáticas
def soma(x: float, y: float) -> float: return x + y
def subtracao(x: float, y: float) -> float: return x - y
def multiplicacao(x: float, y: float) -> float: return x * y
def divisao(x: float, y: float) -> str: return "ERRO: Divisão por zero!" if y == 0 else x / y
def potencia(x: float, y: float) -> str: return "ERRO: Zero elevado a um número negativo não é definido!" if x == 0 and y < 0 else x ** y

# Funções trigonométricas e logaritmos
def raiz(x: float) -> str: return "ERRO: Raiz quadrada de número negativo não é definida!" if x < 0 else math.sqrt(x)
def seno(x:float) -> float: return math.sin(x)
def cosseno(x: float) -> float: return math.cos(x)
def tangente(x: float) -> float: return math.tan(x)
def arcoseno(x: float) -> str: return math.asin(x) if -1 <= x <= 1 else "ERRO: Valor fora do domínio de -1 a 1!"
def arcocoseno(x: float) -> str: return math.acos(x) if -1 <= x <= 1 else "ERRO: Valor fora do domínio de -1 a 1!"
def arcotangente(x: float) -> float: return math.atan(x)
def senohiperbolico(x:float) -> float: return math.sinh(x)
def cossenohiperbolico(x: float) -> float: return math.cosh(x)
def tangentehiperbolico(x: float) -> float: return math.tanh(x)
def logaritmonatural(x: float) -> str: return "ERRO: Logaritmo de número não positivo não é definido!" if x <= 0 else math.log(x)
def logaritmobase10(x: float) -> str: return "ERRO: Logaritmo de número não positivo não é definido!" if x <= 0 else math.log10(x)
def logaritmobaseb(x: float, b:float) -> str: return "ERRO: Valores inválidos!" if x <= 0 or b <= 0 or b == 1 else math.log(x) / math.log(b)
def fatorial(n: int) -> str: return "ERRO: Fatorial não é definido para números negativos!" if n < 0 else math.factorial(n)
def combinacao(n: int, r: int) -> str: return "ERRO: Valores inválidos!" if n < 0 or r < 0 or r > n else math.comb(n, r)
def permutacao(n: int, r: int) -> str: return "ERRO: Valores inválidos!" if n < 0 or r < 0 or r > n else math.perm(n, r)
def grausradianos(x:float) -> float: return x * math.pi / 180
def radianosgraus(x: float) -> float: return x * 180 / math.pi
def binario(x: int) -> str: return bin(x)[2:]
def octal(x: int) -> str: return oct(x)[2:]
def hexadecimal(x: int) -> str: return hex(x)[2:].upper()
def binariodecimal(b: str) -> int: return int(b, 2)
def octaldecimal(o: str) -> int: return int(o, 8)
def hexadecimaldecimal(h: str) -> int: return int(h, 16)

def media() -> float:
    numeros = obterNumerosInput()
    return sum(numeros) / len(numeros) if numeros else "ERRO: Lista de números vazia!"

def mediana() -> float:
    numeros = obterNumerosInput()
    if not numeros:
        return "ERRO: Lista de números vazia!"

    numeros.sort()
    n = len(numeros)
    return numeros [n // 2] if n % 2 == 1 else (numeros[n // 2 - 1] + numeros[n // 2]) / 2

def moda() -> str:
    numeros = obterNumerosInput()
    if not numeros: 
        return "ERRO: Lista de números vazia!"
    contador = Counter(numeros)
    frequenciaMax = max(contador.values())
    modas = [num for num, freq in contador.items() if freq == frequenciaMax]
    if len(modas) == len(numeros):
        return "ERRO: Todos os números são unicos; não há moda definida."
    return modas if len(modas) > 1 else modas[0]

def desvioPadrao() -> str:
    numeros = obterNumerosInput|()
    if not numeros:
        return "ERRO: Lista de números vazia!"
    media = sum(numeros) / len(numeros)
    variancia = sum((x - media) ** 2 for x in numeros) / len(numeros)
    return math.sqrt(variancia)

def integralIndefinida(expressao: str, variavel: str) -> str:
    try:
        x = sp.symbols(variavel)
        return sp.integrate(expressao, x)
    except Exception as e:
        return f"ERRO: {e}"
    
def integralDefinida(expressao: str, variavel: str, a:float, b:float) -> str:
    try:
        x = sp.symbols(variavel)
        return sp.integrate(expressao, (x, a, b))
    except Exception as e:
        return f"ERRO: {e}"
    
def derivada(expressao: str, variavel: str) -> str:
    try:
        x = sp.symbols(variavel)
        return sp.diff(expressao, x)
    except Exception as e:
        return f"ERRO: {e}"
    
def equacaoDiferencial(equacao: str, variavel: str, funcao: str) -> str:
    try:
        x = sp.symbols(variavel)
        y = sp.Function(funcao)(x)
        ode = sp.Eq(eval(equacao), y.diff(x))
        return sp.dsolve(ode, y)
    except Exception as e:
        return f"ERRO: {e}"
    
def somaComplexo(z1: complex, z2: complex) -> complex: return z1 + z2
def subtracaoComplexo(z1: complex, z2: complex) -> complex: return z1 - z2
def multiplicacaoComplexo(z1: complex, z2: complex) -> complex: return z1 * z2
def divisaoComplexo(z1: complex, z2: complex) -> str: return "ERRO: Divisão por zero!" if z2 == 0 else z1 / z2

def representacaoPolar(z: complex) -> str:
    r, theta = cmath.polar(z)
    return f"Magnitude: {r}, Ângulo (radianos): {theta}"

def transformadaFourier(dados: list) -> str:
    try:
        dados = [complex(d) for d in dados]
        return np.fft.fft(dados)
    except Exception as e:
        return f"ERRO: {e}"
    
def obterNumerosInput() -> list:
    numeros = []
    while True:
        entrada = input("Digite um número (ou 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            break

        try: 
            numeros.append(float(entrada))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

        return numeros
    
# Função para exibir o menu
def menu() -> None:
    print("\n--- Calculadora Multifuncional ---")
    print("1. Soma | 2. Subtração | 3. Multiplicação | 4. Divisão | 5. Potência")
    print("6. Raiz Quadrada | 7. Seno | 8. Cosseno | 9. Tangente | 10. Arcoseno")
    print("11. Arcocoseno | 12. Arcotangente | 13. Senohiperbólico | 14. Cossenohiperbólico | 15. Tangentehiperbólico")
    print("16. Logaritmo Natural | 17. Logaritmo de Base 10 | 18. Logaritmo de Base B | 19. Fatorial | 20. Combinatória")
    print("21. Permutação | 22. Conersão de Graus para Radianos | 23. Conversão de Radianos para Graus | 24. Conversão para Binário | 25. Conversão para Octal")
    print("26. Conversão para Hexadecimal | 27. Conversão de Binário para Decimal | 28. Conversão de Octal para Decimal | 29. Conversão de Hexadecimal para Decimal | 30. Média")
    print("31. Mediana | 32. Moda | 33. Desvio Padrão | 34. Integral Indefinida | 35. Integral Definida")
    print("36. Derivada | 37. Equação Diferencial | 38. Soma Complexo | 39. Subtração Complexo | 40. Multiplicação Complexo")
    print("41. Divisão Complexo | 42. Representação Polar | 43. Transformada de Fourier | 0. Sair")

def calcular():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '0':
            print("Saindo da calculadora...")
            break
        try:
            if opcao in {'1', '2', '3', '4', '5'}:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                oparacoes = {
                    '1': soma,
                    '2': subtracao,
                    '3': multiplicacao,
                    '4': divisao,
                    '5': potencia
                }
                resultado = oparacoes[opcao](x, y)
                print(f"Resultado: {resultado}")
            elif opcao in {'6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'}:
                x = float(input("Digite o número: "))
                oparacoes = {
                    '6': raiz,
                    '7': seno,
                    '8': cosseno,
                    '9': tangente,
                    '10': arcoseno,
                    '11': arcocoseno,
                    '12': arcotangente,
                    '13': senohiperbolico,
                    '14': cossenohiperbolico,
                    '15': tangentehiperbolico,
                    '16': logaritmonatural,
                    '17': logaritmobase10,
                    '18': logaritmobaseb
                }
                resultado = oparacoes[opcao](x)
                print(f"Resultado: {resultado}")
            elif opcao in {'20', '21', '22', '23', '24', '25', '26', '27', '28', '29'}:
                if opcao in {'20', '21'}:
                    n = int(input("Digite n: "))
                    r = int(input("Digite r: "))
                    resultado = combinacao(n, r) if opcao == '20' else permutacao(n, r)
                else:
                    x = int(input("Digite o número: "))
                    if opcao == '22':
                        resultado = grausradianos(x)
                    elif opcao == '23':
                        resultado = radianosgraus(x)
                    elif opcao == '24':
                        resultado = binario(x)
                    elif opcao == '25':
                        resultado = octal(x)
                    elif opcao == '26':
                        resultado = hexadecimal(x)
                    elif opcao == '27':
                        b = input("Digite o número binário: ")
                        resultado = binariodecimal(b)
                    elif opcao == '28':
                        o = input("Digite o número octal: ")
                        resultado = octaldecimal(o)
                    elif opcao == '29':
                        h = input("Digite o número hexadecimal: ")
                        resultado = hexadecimaldecimal(h)
                print(f"Resultado: {resultado}")
            elif opcao in {'30', '31', '32', '33'}:
                if opcao == '30':
                    resultado = media()
                elif opcao == '31':
                    resultado = mediana()
                elif opcao == '32':
                    resultado = moda()
                elif opcao == '33':
                    resultado = desvioPadrao()
                print(f"Resultado: {resultado}")
            elif opcao in {'34', '35', '36'}:
                expressao = input("Digite a expressão: ")
                variavel = input("Digite a variável: ")
                if opcao == '34':
                    resultado = integralIndefinida(expressao, variavel)
                elif opcao == '35':
                    a = float(input("Digite o limite inferior: "))
                    b = float(input("Digite o limite superior: "))
                    resultado = integralDefinida(expressao, variavel, a, b)
                elif opcao == '36':
                    resultado = derivada(expressao, variavel)
                print(f"Resultado: {resultado}")
            elif opcao == '37':
                equacao = input("Digite a equação diferencial: ")
                variavel = input("Digite a variavel: ")
                funcao = input("Digite o nome da função: ")
                resultado = equacaoDiferencial(equacao, variavel, funcao)
                print(f"Resultado: {resultado}")
            elif opcao in {'38', '39', '40', '41'}:
                z1Real = float(input("Digite a parte real do primeiro número complexo: "))
                z1Imag = float(input("Digite a parte imaginária do primeiro número complexo: ")) * 1j
                z2Real = float(input("Digite a parte real do segundo número complexo: "))
                z2Imag = float(input("Digite a parte imaginária do segundo número complexo: ")) * 1j
                z1 = z1Real + z1Imag
                z2 = z2Real + z2Imag
                operacoesComplexas = {
                    '38': somaComplexo,
                    '39': subtracaoComplexo,
                    '40': multiplicacaoComplexo,
                    '41': divisaoComplexo
                }
                resultado = operacoesComplexas[opcao](z1, z2)
                print(f"Resultado: {resultado}")
            elif opcao == '42':
                zReal = float(input("Digite a parte real do número complexo: "))
                zImag = float(input("Digite a parte imaginária do número complexo: ")) * 1j
                z = zReal + zImag
                resultado = representacaoPolar(z)
                print(f"Resultado: {resultado}")
            elif opcao == '43':
                dados = obterNumerosInput()
                resultado = transformadaFourier(dados)
                print(f"Resultado: {resultado}")
            else:
                print("Opção inválida! Tente novamente.")
        except Exception as e:
            print(f"ERRO: {e}")

if __name__ == "__main__":
    calcular()