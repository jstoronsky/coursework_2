
from homework_9.utils_1 import load_random_word
from homework_9.class_Player import player1

# Принтуем всю приветственную информацию
print(f"Привет, {player1}!")
print(f"Составьте {load_random_word().subwords_lenght()} слов из слова {load_random_word()}")
print("Слова должны быть не короче 3 букв.\nЧтобы закончить игру угадайте все слова или напишите 'stop'")

attempt_count = load_random_word().subwords_lenght()
# Запускаем основной цикл
while attempt_count != 0:
    user_input_ = input("\nВведите слово: ")
    if user_input_ in player1.used_words:
        print("уже использовано")
    elif len(user_input_) <= 2:
        print("слишком короткое слово")
    elif user_input_ == "стоп" or user_input_ == "stop":
        break
    else:
        print(load_random_word().iscorrect(user_input_))
    attempt_count -= 1
# Выводим результат
if player1.length_of_used_words() in [2, 3, 4]:
    print(f"\nИгра завершена, вы угадали {player1.length_of_used_words()} слова")
else:
    print(f"\nИгра завершена, вы угадали {player1.length_of_used_words()} слов")
