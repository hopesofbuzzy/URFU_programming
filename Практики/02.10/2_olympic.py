def check_winners(scores: list, student_score: int):
    """
    Определяет, попал ли студент в тройку победителей

    :param scores: список баллов всех студентов
    :param student_score: балл студента
    """
    scores_sorted = sorted(scores)
    if student_score in scores_sorted[-3:]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


scores_to_check = list(
    map(int, input("Через пробел введите данные всех студентов: ").split(" "))
)
student_score_to_check = int(input("Введите балл студента: "))
check_winners(scores_to_check, student_score_to_check)
