import random
import math

def calculate_lcm(a, b, ):
        return a * b // math.gcd(a, b)

def play_lcm_game():
    print("Добро пожаловать в игру 'Наименьшее общее кратное'!")
    print("Вам будут показаны три числа. Ваша задача - ввести их НОК.")
    print("Давайте начнем!\n")
    
    correct_answers = 0
    total_questions = 0
    
    while True:
        numbers = [random.randint(1, 50) for _ in range(2)]
        a, b = numbers
        
        print(f"Числа: {a}, {b}")
        correct_lcm = calculate_lcm(a, b)
        
        while True:
            try:
                user_answer = input("Введите НОК этих чисел (или 'q' для выхода): ")
                if user_answer.lower() == 'q':
                    print(f"\nИгра окончена. Ваш результат: {correct_answers} правильных ответов из {total_questions}.")
                    return
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Пожалуйста, введите целое число или 'q' для выхода.")
        
        total_questions += 1
        
        if user_answer == correct_lcm:
            print("Правильно! Молодец!\n")
            correct_answers += 1
        else:
            print(f"Неправильно. Ваш ответ: {user_answer}. Правильный ответ: {correct_lcm}\n")
            
if __name__ == "__main__":
    play_lcm_game()