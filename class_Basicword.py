from homework_9.class_Player import player1


class BasicWord:
    def __init__(self, basic_word, available_words):
        """
        инициализируем исходное слово и список слов, которые можно получить из исходного слова
        """
        self.basic_word = basic_word
        self.available_words = available_words

    def iscorrect(self, user_input):
        """
        проверка введённого слова
        """
        if user_input in self.available_words:
            player1.list_of_used_words(user_input)
            return "Правильно!"
        return "Неправильно!"

    def subwords_lenght(self):
        """
        подсчёт количества списка подслов
        """
        return len(self.available_words)

    def __repr__(self):
        """
        через репр реализуем исходное слово
        """
        return self.basic_word
