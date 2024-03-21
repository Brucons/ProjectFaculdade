import random

class Jogo:
    def __init__(self):
        self.target = 0

    def initGame(self):
        self.target = random.randint(1, 20)
        print("START GAME\n ->Advinhe um número de 1 a 20")

    def play_round(self, guess):
        if guess == self.target:
            print("Parabéns! Você acertou o número {}".format(self.target))
            return True
        elif self.target > 100:
            print("GAME OVER")
            return True
        else:
            print("TRY AGAIN")
            return False

class User:
    @staticmethod
    def make_guess():
        return int(input("Digite seu palpite: "))

def main():
    jogo = Jogo()
    jogo.initGame()

    while True:
        guess = User.make_guess()
        if jogo.play_round(guess):
            break

if __name__ == "__main__":
    main()