#Arthur Alexandre 1°D n°7 - Programa das aula remotas dia 11/10/25, Programação e algoritmo

def ler_numeros():
    nums = []
    i = 1
    while len(nums) < 15:
        n = int(input(f"Digite o {i}º número: "))
        if n in nums:
            print("Digite outro número que não seja repetido.")
        else:
            nums.append(n)
            i += 1
    return nums


def ordenar(nums):
    return sorted(nums)


def analisar(nums):
    maior = max(nums)
    menor = min(nums)
    soma = sum(nums)
    media = soma / len(nums)
    pares = sum(1 for x in nums if x % 2 == 0)
    impares = len(nums) - pares
    return maior, menor, soma, media, pares, impares


def mostrar(nums, maior, menor, soma, media, pares, impares):
    print("\nNúmeros em ordem crescente:", nums)
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media:.2f}")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


def programa():
    nums = ler_numeros()
    nums = ordenar(nums)
    maior, menor, soma, media, pares, impares = analisar(nums)
    mostrar(nums, maior, menor, soma, media, pares, impares)


def main():
    while True:
        programa()
        repetir = input("\nDeseja repetir o programa? (s/n): ").strip().lower()
        if repetir != 's':
            print("\nPrograma encerrado.")
            break


if __name__ == "__main__":
    main()
