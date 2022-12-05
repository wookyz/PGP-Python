import random
import math


class PGP:

    def __init__(self, mensagem: str) -> None:
        self.gerarChave()
        self.mensagemCriptografada = self.criptografar(mensagem)

    def gerarChave(self) -> None:
        """
        Gera as chaves pública e privada.
        """
        p = self.__gerarPrimo__()
        q = self.__gerarPrimo__()
        self.p = p
        self.q = q

        n = p * q
        self.n = n

        totiente = self.__calculaTotiente__(p, q)
        self.totiente = totiente

        e = self.__calculaCoprimos__(self.totiente)
        d = self.__calculaInverso__(e, totiente)
        self.e = e
        self.d = d

    def __gerarPrimo__(self) -> int:
        """
        Gera um número primo aleatório.
        """
        while True:
            num = random.randint(100, 1000)
            if num % 2 == 0:
                num += 1
            if self.__ehPrimo__(num):
                return num

    def __ehPrimo__(self, n: int) -> bool:
        """
        Checa se um número é primo ou não.
        """
        if n == 1:
            return False

        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def __calculaTotiente__(self, p: int, q: int) -> int:
        """
        Calcula a função totiente de n a partir dos primos que geram n.
        """
        totiente = (p - 1) * (q - 1)
        return totiente

    def __calculaCoprimos__(self, totiente: int) -> int:
        """
        Calcula um coprimo de n.
        """
        while True:
            e = random.randint(2, totiente)
            if math.gcd(e, totiente) == 1:
                return e

    def __calculaInverso__(self, e, totiente: int) -> int:
        """
        Calcula o inverso multiplicativo de e.
        """
        d = 1
        while True:
            if e * d % totiente == 1:
                return d
            d += 1

    def criptografar(self, mensagem: str) -> list:
        """
        Criptografa a mensagem.
        """
        return [self.criptografarCaractere(char) for char in mensagem]

    def criptografarCaractere(self, char: str) -> int:
        """
        Criptografa um caractere.
        """
        return ord(char) ** self.e % self.n

    def descriptografar(self, mensagemCriptografada: list) -> str:
        """
        Descriptografa a mensagem.
        """
        return "".join([chr(self.descriptografarCaractere(char))
                        for char in mensagemCriptografada])

    def descriptografarCaractere(self, char: int) -> int:
        """
        Descriptografa um caractere.
        """
        return char ** self.d % self.n

    def __str__(self) -> str:
        """
        Representação da classe.
        """
        return f"\nChave pública: ({self.e}, {self.n})\
                \nChave privada: ({self.d}, {self.n})"

    def exibirDados(self) -> None:
        """
        Exibe os dados da chave.
        """
        print(f"P: {self.p}\nQ: {self.q}\nN: {self.n}\
            \nTotiente: {self.totiente}\nE: {self.e}\nD: {self.d}")
        print(f"Mensagem criptografada: {self.mensagemCriptografada}")


if __name__ == "__main__":
    mensagem = input("Digite a mensagem: ")
    pgp = PGP(mensagem)
    print(pgp)
    print("-="*20)
    pgp.exibirDados()
    print("-="*20)
    print(pgp.descriptografar(pgp.mensagemCriptografada))
