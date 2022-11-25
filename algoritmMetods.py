import time

def findProbabilityField(field:list): #Метод\код вычисляет для каждой ячейки набор соседних ячеек(групп) в радиусе 1 клетка а так же вероятность нахождения мины в соседних ячейках относительно текущей

    listOfneighborCells = []          #лист соседов                                                                             #-1,-1 -1,0   -1,1
    container = []                    #лист для заполнения листа соседов                                                        # 0,1    0     0,1
    offsetList = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]] #Все возможные смещения для соседей клетки Рисунок:    # 1,-1  1,0    1,1  координаты в формате (y,x)
    xIndex,yIndex = 0,0                 # Индексы ячейки для которой ищем соседей, используем это потому что list.index работает немного кривовато для нас
    for row in field:                   # берём каждую строчку из поля
        for cell in row:                # к каждой ячейке в строчке применяем код ниже:
            for offset in offsetList:   # Применяем к индексам ячейки смещение
                if yIndex + offset[0] >= 0 and xIndex + offset[1] >=0 and yIndex + offset[0] <= len(field) - 1 and xIndex + offset[1] <= len(row) - 1 : # первый and проверка на отрицательность смещённых индексов, что бы не получать значения с конца. Третий and для определения вышли мы за предел листа и если вышли то пропускаем такое смещение
                    container.append([cell, xIndex, yIndex, field[yIndex + offset[0]][xIndex + offset[1]], xIndex + offset[1], yIndex + offset[0]]) # Состав одного элемента listOfneighborCells: [Ячейка, Координата X, Координата Y, Содержимое соседней ячейки, Координата Х соседа, Координата У соседа]
                    listOfneighborCells.append(container)   # добавляем соседа ячейки в лист соседов
                    container = []                          #Пересоздаём контейнер что бы не получать повторение одного массива
            xIndex += 1                       #rowIndex - счётчик символа в строке
        xIndex = 0                            #Обнуляем счётчик что бы не словить out of range
        yIndex +=1                         #columnindex - счётчик строки
    
    # for elem in listOfneighborCells:    #Цикл вывода в консоль содержимого листа соседей
    #     print(f"Ячейка: {elem[0][0]} Координаты x,y {elem[0][1]},{elem[0][2]} Содержимое соседней ячейки {elem[0][3]} Координаты x,y соседа: {elem[0][4]},{elem[0][5]} \n")
    #     time.sleep(20)
    
    probabilityField = [['*'] * len(field[0]) for i in range(len(field))] #Создаём лист который будет хранить вероятность нахождения мины в ячейках прилежащих к открытым
    xIndex,yIndex = 0,0                                                   #Используем индексы для нахождения совпадений с листом пососедей
    neighborCount = 0                                                     #Используем для хранения числа соседей
    neighborCountOpen = 0                                                 #Используем для хранения числа открытых соседних ячеек
    recordCopy = list()                                                   #Тк после нахождения последней правильной записи перебор пойдёт дальше(но он будет continue) мы будем получать record содержащий последнюю запись в листе соседей, что бы это фиксануть нужные записи добавляем в records
    for row in probabilityField:                                          #Так как probabilityField такого же размера как и field  можно искать записи о соседстве через индексы cell                                 
        for cell in row:                                                  #Для каждой ячейки в probabilityField прогоняем цикл поиска открытых и закрытых соседних ячеек
            for record in listOfneighborCells:                            #для каждой записи в листе соседей делаем прогон по условиям     
                
                if xIndex != record[0][1]:                                #проверка совпадения по координате x, а ниже и y, так мы находим запись в листе соседей для ячейки probabilityField
                    continue                                              #continue а не break потому что записи для другой ячейки будут прерывать цикл перебора не доходя до правильной записи

                if yIndex != record[0][2]:
                    continue

                if record[0][0] == "*":                                   #Для закрытой ячейки не ищем количество соседей, потому что не сможем узнать вероятность мины в соседних ячейках
                    continue

                if int(record[0][0]) == 0:                                #Для ячейки рядом с которой нет мин тоже не ищем соседей 
                    continue

                if xIndex == record[0][1]:                                #Для уверенности
                    if yIndex == record[0][2]:                          
                        if record[0][3] == "*":                           #Если соседняя ячейка закрыта +1 в количество соседних ячеек
                            neighborCount += 1
                            recordCopy = record.copy()
                        if str(record[0][3]).isdigit():                   #Если соседняя ячейка открыта +1 в количетсво открытых соседних ячеек
                            neighborCountOpen += 1
                            recordCopy = record.copy()                    
            
            if len(recordCopy) != 0 :
                print(recordCopy, listOfneighborCells.index(recordCopy))
                print(f"Значение ячейки: {recordCopy[0][0]} Координата х: {recordCopy[0][1]} Координата у: {recordCopy[0][2]}, Значение соседней ячейки {recordCopy[0][3]} Координата соседней x: {recordCopy[0][4]} Координата соседней y: {recordCopy[0][5]}  Закрытых сос-х ячеек: {neighborCount} Открытых соседних ячеек{neighborCountOpen}")
                
            recordCopy  = []
            neighborCount = 0                   
            neighborCountOpen = 0
            xIndex += 1                                                     #Обнуляем счётчики мин  обнуляем и инкримируем счётчики
        xIndex = 0
        yIndex += 1