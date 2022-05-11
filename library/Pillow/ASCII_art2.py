import sys, random, argparse #argparse библиотека для разбора командной строки
import numpy as np           #numpy библиотека для больших матричных вычислений
import math

# https://russianblogs.com/article/4135570214/

from PIL import Image
#PIL библиотека - де-факто стандартная библиотека Python для обработки изображений

# Основной принцип изображения в ASCII состоит в том, чтобы разделить изображение в градациях серого на множество
# маленьких сеток, рассчитать среднюю яркость маленьких сеток и заменить их символами различной яркости.
# Символы, соответствующие градиенту серого, можно найти по адресу: http://paulbourke.net/dataformats/asciiart/
# Серый градиент уровня 70 (становится все ярче)
# gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale1 = "$@B%8&WM###########************************************..........     "
# 10-уровневый градиент серого
# gscale2 = '@%#*+=-:. '
gscale3 = '@%#*+.    '

# Рассчитать среднюю яркость каждого маленького блока
def getAverageL(image):
    im = np.array(image)# Небольшой блок в двумерный массив
    w, h = im.shape# Сохранить небольшой размер блока
    return np.average(im.reshape(w * h))# Превратите двумерный массив в одно измерение и найдите среднее

# Согласно средней яркости каждого маленького блока, соответствующего символам ASCII
def covertImageToAscii(fileName, cols, scale, moreLevels):
    global gscale1, gscale2, gscale3# Серый градиент
    image = Image.open(fileName).convert('L')# Откройте изображение и преобразуйте его в оттенки серого.
    W, H = image.size[0], image.size[1]# Сохранить ширину и высоту изображения
    print("Ширина и высота изображения:% dx% d" % (W, H))
    w = W / cols# Рассчитать ширину маленького блока
    h = w / scale# Вычислите высоту маленького блока. Коэффициент вертикальной шкалы используется здесь, чтобы уменьшить нарушение изображения. Протестированная шкала равна 0,43, и эффект лучше.
    rows = int(H / h)# Подсчитать количество строк
    print('Всего% d строк и% d столбцов' % (rows,cols))
    print('Ширина и высота каждого небольшого блока:% dx% d' % (w, h))

    # Изображение слишком маленькое для выхода
    if cols > W or rows > H:
        print('Изображение слишком маленькое для сегментации! (Улучшить разрешение изображения или уменьшить тонкость)')
        exit(0)

    aimg = []# Текстовая графика хранится в списке
    # Матч ASCII блок за блоком
    for j in range(rows):
        y1 = int(j * h)#Y координата начала малого блока
        y2 = int((j + 1) * h)# Координата y конца малого блока
        if j == rows - 1:
            y2 = H# Последняя ячейка недостаточно велика, конечная координата y представлена ​​высотой изображения H
        aimg.append("")# Первая вставка пустой строки
        for i in range(cols):
            x1 = int(i * w)#X координата начала малого блока
            x2 = int((i + 1) * w)#X координата малого конца
            if i == cols - 1:
                x2 = W# Последняя ячейка недостаточно велика, конечная координата x представлена ​​шириной изображения W
            img = image.crop((x1, y1, x2, y2))# Извлечь мелкие кусочки
            avg = int(getAverageL(img))# Рассчитать среднюю яркость
            if moreLevels:
                gsval = gscale1[int((avg * 69) / 255)]# Среднее значение яркости [0,255] соответствует десятиуровневому градиенту серого [0,69], и получить соответствующие символы ASCII
            else:
                # gsval = gscale2[int((avg * 9) / 255)]# Среднее значение яркости [0,255] соответствует семидесяти градиентам серого [0,9], и получается соответствующий символ ASCII
                gsval = gscale3[int((avg * 9) / 255)]  # Среднее значение яркости [0,255] соответствует семидесяти градиентам серого [0,9], и получается соответствующий символ ASCII
            aimg[j] += gsval# Обновить текстовую графику
    return aimg

#Основная функция
def main():
    # descStr = 'Python реализует изображение в ASCII-графике'
    # parser = argparse.ArgumentParser(description=descStr)
    # # Установить возможные параметры командной строки для запуска программы
    # parser.add_argument('--file', dest='imgFile', required=True)# Должен быть установлен
    # parser.add_argument('--scale', dest='scale', required=False)# По умолчанию
    # parser.add_argument('--out', dest='outFile', required=False)
    # parser.add_argument('--cols', dest='cols', required=False)
    # parser.add_argument('--morelevels', dest='moreLevels', action='store_true')# Установите больше уровней в True

    # args = parser.parse_args()# Параметры хранятся в аргументах

    # imgFile = args.imgFile# Введенное изображение
    # outFile = 'out.txt'# Выходная текстовая графика ASCII
    # if args.outFile:
    #     outFile = args.outFile
    # scale = 0.43# Вертикальный коэффициент масштабирования имеет хороший результат 0,43, и текст должен отображаться шрифтами одинаковой длины, такими как Song Dynasty, Courier
    # if args.scale:
    #     scale = float(args.scale)
    # cols = 80# Количество столбцов, разделенных по умолчанию, чем больше количество столбцов, тем больше тонкость, но не рекомендуется быть слишком большим
    # if args.cols:
    #     cols = int(args.cols)

    imgFile = '/home/fox/Pictures/images/010.jpg'
    cols = 200

    scale = 0.43
    moreLevels = False
    outFile = '/home/shared/images/out10.txt'

    print('Преобразование ...')
    aimg = covertImageToAscii(imgFile, cols, scale, moreLevels)# Функция сопоставления вызовов

    f = open(outFile, 'w')# Сохранить изображение документа
    for row in aimg:
        f.write(row + '\n')
    f.close()
    print('Текстовая графика ASCII хранится в% s' % outFile)

#основная функция
if __name__ == '__main__':
    main()

#Pycharm Установите метод работы параметра командной строки: Run → Run → Edit Configuration → Defaults → Python → Parameters справа
# Требуется: введите путь к изображению - файл test.jpg
#По желанию:
# (Рекомендуется) Количество столбцов в сегментации изображения - протоколы 100
#Output ASCII текстовая графическая дорожка --out out.txt
# Вертикальный масштабный коэффициент - масштаб 1
# Используйте градиент градаций серого с 70 уровнями - больше уровней