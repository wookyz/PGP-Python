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
        lista = self.__gerarListaPrimos__()
        p = self.__gerarPrimo__(lista)
        q = self.__gerarPrimo__(lista)
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

    def __gerarPrimo__(self,lista) -> int:
        """
        Gera um número primo aleatório.
        """
        return random.choice(lista)
    def __gerarListaPrimos__(self) -> list:
        lista = [2,3,5]
        n = 7
        while(True):    
            if self.__ehPrimo__(lista, n):
                lista.append(n)
            n+=2
            if n >= 2000:
                break
        return lista
    def __ehPrimo__(self, lista , n):
        """
        Checa se um número é primo ou não.
        """
        for elemento in lista:
            if n % elemento == 0:
                return False
            if elemento >= math.sqrt(n):
                break
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
        return "".join([chr(self.descriptografarCaractere(char)) for char in mensagemCriptografada])

    def descriptografarCaractere(self, char: int) -> int:
        """
        Descriptografa um caractere.
        """
        return char ** self.d % self.n

    def __str__(self) -> str:
        """
        Representação da classe.
        """
        return f"\nChave pública: ({self.e}, {self.n})\nChave privada: ({self.d}, {self.n})"

    def exibirDados(self) -> None:
        """
        Exibe os dados da chave.
        """
        print(
            f"P: {self.p}\nQ: {self.q}\nN: {self.n}\nTotiente: {self.totiente}\nE: {self.e}\nD: {self.d}")
        print(f"Mensagem criptografada: {self.mensagemCriptografada}")


if __name__ == "__main__":
    mensagem = input("Digite a mensagem: ")
    pgp = PGP(mensagem)
    print(pgp)
    print("-="*20)
    pgp.exibirDados()
    print("-="*20)
    print(pgp.descriptografar(pgp.mensagemCriptografada))
