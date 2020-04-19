import random


def getAnswers(anwserNumber):
    if anwserNumber == 1:
        return 'Скорей всего'
    elif anwserNumber == 2:
        return 'Возможно'
    elif anwserNumber == 3:
        return 'Да'
    elif anwserNumber == 4:
        return "Нет"
    elif anwserNumber == 5:
        return 'Попробуй ещё раз'
    elif anwserNumber == 6:
        return 'Сконцетрируйся'
    elif anwserNumber == 7:
        return 'Выглядит не очень'
    elif anwserNumber == 8:
        return 'Сомневаюсь'

print(getAnswers(random.randint(1, 9)))
