class Player:
    def __init__(self, name):
        """
        инициализируем имя игрока и список введённых слов
        """
        self.name = name
        self.used_words = []

    def length_of_used_words(self):
        """
        длина списка используемых слов
        """
        return len(self.used_words)

    def list_of_used_words(self, used_word):
        """
        добавляем введённое слово в список использованных слов
        """
        self.used_words.append(used_word)
        return self.used_words

    def __repr__(self):
        """
        репр имени
        """
        return self.name

# экземпляр класса Player


enter_name = input("Введите имя игрока: ")
player1 = Player(enter_name)
