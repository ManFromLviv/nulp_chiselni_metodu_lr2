import numpy as np # Для зберігання й обчислення діпазону значення Х і У функції.
import matplotlib.pyplot as plt # Для побудуви графіку (полотно).
from sympy import symbols, Eq, real_roots # Для обрахунку коренів.

# Обрахунок функції зі значенням змінної.
def getFx(x=float) -> float:
    return round(x ** 4 - 3 * x ** 3 + 2 * x - 7, 2)


# Обрахунок похідної функції зі значенням змінної.
def getFxDerivative(x=float) -> float:
    return round(4 * x ** 3 - 9 * x ** 2 + 2, 2)


# Обрахунок першої остачі зі значенням змінної.
def getR1Fx(x=float) -> float:
    return round(27.0 / 16 * x ** 2 - 3.0 / 2 * x + 53.0 / 8, 2)


# Обрахунок другої остачі зі значенням змінної.
def getR2Fx(x=float) -> float:
    return round(1664.0 / 81 * x - 5680.0 / 243, 2)


# Обрахунок третьої остачі зі значенням змінної.
def getR3Fx(x=float) -> float:
    return round(-1229211.0 / 173056, 2)


# Повернення ітераційного списку при певному значенні змінної.
def getIterationList(x=float) -> list:
    iterationList = [getFx(x), getFxDerivative(x), getR1Fx(x), getR2Fx(x), getR3Fx(x)]
    return iterationList


# Повернення знаку числа.
def getSignNumber(number=float) -> str:
    if number > 0:
        return "+"
    elif number < 0:
        return "-"
    else:
        return "0"


# Повернення списку знаків ітераційного списку.
def getSignIterationList(iterationList=list) -> list:
    signIterationList = []
    for i in iterationList:
        signIterationList.append(getSignNumber(i))
    return signIterationList


# Обрахунок кількості змін знаків при ітерації.
def getCountChangeInSignIterationList(signIterationList=list) -> int:
    counter = 0
    for i in range(len(signIterationList) - 1):
        if signIterationList[i] != "0" and signIterationList[i] != signIterationList[i + 1]:
            counter += 1
    return counter


# Повернення списку з діапазоном коренів.
def getRangeOfRootsList(xList=list, countSignChangeList=list) -> list:
    rangeOfRootsList = ["Кількість коренів: " + str(int(countSignChangeList[0] - countSignChangeList[-1]))]
    counterRoots = 0
    for i in range(len(countSignChangeList) - 1):
        if countSignChangeList[i] - countSignChangeList[i + 1] != 0:
            counterRoots += 1
            rangeOfRootsList.append(
                "Діапазон № " + str(counterRoots) + ": " + str(xList[i]) + " < x < " + str(xList[i + 1]))
    return rangeOfRootsList


# Вивід таблиць зі значеннями або знаками функції.
def getTablesOfResultLists(message=str, xList=list, resultList=list, countChangeList=list) -> None:
    print(message)
    sepValue = " | "
    lengthLine = 45
    line = "\t" + "=" * lengthLine
    print("\tx", "f(x)", "f(x)'", "R1", "R2", "R3", "W", sep=sepValue)
    print(line)
    for i in range(len(xList)):
        print("\t", xList[i], end=sepValue)
        for j in range(len(resultList[i])):
            print(resultList[i][j], sep=sepValue, end=sepValue)
        print(countChangeList[i])
        print(line)

# Вивід діапазону коренів
def getInformationRangeOfRoots(message=str, rangeOfRootsList=list) -> None:
    print(message)
    for i in rangeOfRootsList:
        print(f"\t{i}")

# Вивід графіку функції.
def drawFx(a=int, b=int) -> None:
    # Константи підібрані вручну.
    num = 40 # Кількість Х для подальшого зображення графіку.
    aY = -12.5 # Нижня межа У.
    bY = 4 # Верхня межа У.
    # Діапазон Х.
    X = np.linspace(a, b, num)
    # Обраховуємий діапазон У.
    Y = X ** 4 - 3 * X ** 3 + 2 * X - 7
    # Малювання графіку.
    plt.plot(X, Y, label='Графік функції', color='b')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('ЛР № 2, Варіант № 3, Вальчевський П. В., група ОІ-11 сп')
    plt.legend()
    plt.grid(True)
    plt.xlim(a, b)
    plt.ylim(aY, bY)
    plt.axvline(0, color='r', linewidth=1)  # Вісь X.
    plt.axhline(0, color='r', linewidth=1)  # Вісь Y.
    plt.show()

# Обрахунок й вивід коренів функції.
def calcAndOutputRoots() -> None:
    # Оголошуємо символ X для подальшого обчислення рівняння.
    X = symbols('X')
    # Вивід лише дійсних коренів від рівняння.
    print("Корені рівняння (обчислено за допомогою бібліотеки для перевірки):")
    counter = 0
    for root in real_roots(Eq(X ** 4 - 3 * X ** 3 + 2 * X - 7, 0)):
        counter += 1
        print(f"\tКорінь № {counter} : {round(root.evalf(), 2)}")


# Виконання програми.
if __name__ == "__main__":
    try:
        getResult = []  # Список значень усіх функцій при кожному значенню х (ітерації).
        getResultSign = []  # Список знаків усіх функцій при кожному значенню х (ітерації).
        getResultChangeSign = []  # Список кількості змін знаків кожної функції при ітераціях.
        getValuesX = []  # Список значень х.
        getRangeOfRoots = []  # Список діапазону зміни кореня функції.

        a = -3 # Нижня межа.
        b = 4 # Верхня межа.

        # Обрахунок логіки програми.
        for x in range(a, b + 1):
            getValuesX.append(x)
            getResult.append(getIterationList(x))
            getResultSign.append(getSignIterationList(getResult[-1]))
            getResultChangeSign.append(getCountChangeInSignIterationList(getResultSign[-1]))
        getRangeOfRoots = getRangeOfRootsList(getValuesX, getResultChangeSign)

        # Вивід результатів.
        print(f"ЛР № 2, Варіант № 3, Вальчевський П. В., група ОІ-11 сп, взято відрізок [{a}; {b}]")
        lengthLineForOutput = 100
        lineForOutput = "-" * lengthLineForOutput
        print(lineForOutput)
        nameTableOne = "Таблиця № 1 значення функції:"
        getTablesOfResultLists(nameTableOne, getValuesX, getResult, getResultChangeSign)
        print(lineForOutput)
        nameTableTwo = "Таблиця № 2 знаки функції:"
        getTablesOfResultLists(nameTableTwo, getValuesX, getResultSign, getResultChangeSign)
        print(lineForOutput)
        nameInformationBlock = "Висновки програми:"
        getInformationRangeOfRoots(nameInformationBlock, getRangeOfRoots)
        print(lineForOutput)
        calcAndOutputRoots()
        print("Графік функції відображено в іншому вікні!")
        drawFx(a, b)
    except Exception:
        print("Помилка при виконанні програми. Перевірте коректність запису алгоритму!")