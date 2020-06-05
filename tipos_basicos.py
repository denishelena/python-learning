def print_result(result):
    print(result)

def soma(num1, num2):
    print("soma")
    result = num1 + num2
    print_result(result)

def subt(num1, num2):
    print("subt")
    result = num1 - num2
    print_result(result)

def main():
    num1 = int(input('Digite num1:'))
    num2 = int(input('Digite num2:'))
    op = input("Digite op: ")
    if op == '+':
        soma(num1, num2)
        print(soma)
    elif op == '-':
        subt(num1, num2)
        print(subt)
    else:
        return False

while True:
    main()