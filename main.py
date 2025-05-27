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
            user_input = input("Введите пропущенное число (или 'q' для выхода): ").strip()
            if user_input.lower() == 'q':
                print(f"\nИгра окончена. Ваш результат: {correct_answers} из {total_questions}.")
                return
            
            try:
                user_answer = int(user_input)
                break
            except ValueError:
                print("Ошибка! Введите целое число или 'q' для выхода.")
        
        total_questions += 1
        
        if user_answer == correct_answer:
            print("Правильно! Это действительно", correct_answer, "\n")
            correct_answers += 1
        else:
            print(f"Неправильно. Ваш ответ: {user_answer}. Правильный ответ: {correct_answer}\n")
            
if __name__ == "__main__":
    play_lcm_game()
