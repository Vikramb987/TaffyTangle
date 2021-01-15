# Vikram Bawa
# 2018-03-11
# Candy crush clone
import stddraw
import math
import time
import stdarray
import random
import ast
import numpy


# returns all the lines of diagonal entries in a 9x7 list as a list of 15 groups of 1-7 numbers
def returnDiagonal(listA):
    diag = []
    for i in range(-8, 7):
        diag += [list(numpy.diagonal(listA, i))]
    return diag


# returns all the lines of antidiagonal entries in a 9x7 list as a list of 15 groups of 1-7 numbers
def returnAntidiagonal(listA):
    antidiag = []
    for i in range(-8, 7):
        antidiag += [list(numpy.diagonal(listA[::-1], i))]
    return antidiag


# returns the transposed list
def transpose(listA):
    a = ast.literal_eval(str(list(zip(*listA))).replace("(", "[").replace(")", "]"))
    return a


# returns a string of 3 random values. The same values are not side by side if there are any.
def threeRandom():
    rand = str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)) + ", " + str(random.randint(1, 6))
    while (rand.find("1, 1") != -1 or rand.find("2, 2") != -1 or rand.find("3, 3") != -1 or rand.find(
            "4, 4") != -1 or rand.find("5, 5") != -1 or rand.find("6, 6") != -1):
        rand = str(random.randint(1, 6)) + ", " + str(random.randint(1, 6)) + ", " + str(random.randint(1, 6))
    return rand


# returns true only if 3 of the same number do not horizontally occur in a row together
def horizCheck(gridValues):
    gridValues = str(gridValues)
    if (gridValues.find("1, 1, 1") == -1 and gridValues.find("2, 2, 2") == -1 and gridValues.find(
            "3, 3, 3") == -1 and gridValues.find("4, 4, 4") == -1 and gridValues.find(
        "5, 5, 5") == -1 and gridValues.find("6, 6, 6") == -1):
        return True
    else:
        return False


# returns true only if 3 of the same number do not vertically occur in a row together
def vertCheck(gridValues):
    gridValues = str(transpose(gridValues))
    if (gridValues.find("1, 1, 1") == -1 and gridValues.find("2, 2, 2") == -1 and gridValues.find(
            "3, 3, 3") == -1 and gridValues.find("4, 4, 4") == -1 and gridValues.find(
        "5, 5, 5") == -1 and gridValues.find("6, 6, 6") == -1):
        return True
    else:
        return False


# returns true only if 3 of the same number do not diagonally occur in a row together
def diagCheck(gridValues):
    diag = str(returnDiagonal(gridValues))
    if (diag.find("1, 1, 1") == -1 and diag.find("2, 2, 2") == -1 and diag.find("3, 3, 3") == -1 and diag.find(
            "4, 4, 4") == -1 and diag.find("5, 5, 5") == -1 and diag.find("6, 6, 6") == -1):
        return True
    else:
        return False


# returns true only if 3 of the same number do not antidiagonally occur in a row together
def antidiagCheck(gridValues):
    antidiag = str(returnAntidiagonal(gridValues))
    if (antidiag.find("1, 1, 1") == -1 and antidiag.find("2, 2, 2") == -1 and antidiag.find(
            "3, 3, 3") == -1 and antidiag.find("4, 4, 4") == -1 and antidiag.find("5, 5, 5") == -1 and antidiag.find(
        "6, 6, 6") == -1):
        return True
    else:
        return False


# returns false only if there is no instances of the same number in a row horizontally, vertically, diagonally, or antidiagally
def allCheck(gridValues):
    return not horizCheck(gridValues) or not vertCheck(gridValues) or not diagCheck(gridValues) or not antidiagCheck(
        gridValues)


# gridValues is a 9x7 2D array filled with 0's. Randomize the values in gridValues from 1-6 such that the same value does not occur diagonally, horizontally, or vertically 3 times in a row.
def randomValues():
    gridValues = stdarray.create2D(9, 7, 1)
    while (allCheck(gridValues)):
        for i in range(9):
            for j in range(7):
                gridValues[i][j] = random.randint(1, 6)
        randomThree = threeRandom()
        strGrid = str(gridValues)
        while (strGrid.find("1, 1, 1") != -1):
            strGrid = strGrid.replace("1, 1, 1", randomThree)
        while (strGrid.find("2, 2, 2") != -1):
            strGrid = strGrid.replace("2, 2, 2", randomThree)
        while (strGrid.find("3, 3, 3") != -1):
            strGrid = strGrid.replace("3, 3, 3", randomThree)
        while (strGrid.find("4, 4, 4") != -1):
            strGrid = strGrid.replace("4, 4, 4", randomThree)
        while (strGrid.find("5, 5, 5") != -1):
            strGrid = strGrid.replace("5, 5, 5", randomThree)
        while (strGrid.find("6, 6, 6") != -1):
            strGrid = strGrid.replace("6, 6, 6", randomThree)

        gridValues = ast.literal_eval(strGrid)
        strGrid = str(transpose(gridValues))

        while (strGrid.find("1, 1, 1") != -1):
            strGrid = strGrid.replace("1, 1, 1", randomThree)
        while (strGrid.find("2, 2, 2") != -1):
            strGrid = strGrid.replace("2, 2, 2", randomThree)
        while (strGrid.find("3, 3, 3") != -1):
            strGrid = strGrid.replace("3, 3, 3", randomThree)
        while (strGrid.find("4, 4, 4") != -1):
            strGrid = strGrid.replace("4, 4, 4", randomThree)
        while (strGrid.find("5, 5, 5") != -1):
            strGrid = strGrid.replace("5, 5, 5", randomThree)
        while (strGrid.find("6, 6, 6") != -1):
            strGrid = strGrid.replace("6, 6, 6", randomThree)

        gridValues = transpose(ast.literal_eval(strGrid))
        diag = str(returnDiagonal(gridValues))

        while (diag.find("1, 1, 1") != -1):
            diag = diag.replace("1, 1, 1", randomThree)
        while (diag.find("2, 2, 2") != -1):
            diag = diag.replace("2, 2, 2", randomThree)
        while (diag.find("3, 3, 3") != -1):
            diag = diag.replace("3, 3, 3", randomThree)
        while (diag.find("4, 4, 4") != -1):
            diag = diag.replace("4, 4, 4", randomThree)
        while (diag.find("5, 5, 5") != -1):
            diag = diag.replace("5, 5, 5", randomThree)
        while (diag.find("6, 6, 6") != -1):
            diag = diag.replace("6, 6, 6", randomThree)

        diag = ast.literal_eval(diag)

        for i in range(len(gridValues)):
            gridValues[i] = list(gridValues[i])
        for i in range(7):
            gridValues[i][i] = diag[8][i]
            gridValues[i + 1][i] = diag[7][i]
            gridValues[i + 2][i] = diag[6][i]
        for i in range(6):
            gridValues[i][i + 1] = diag[9][i]
            gridValues[i + 3][i] = diag[5][i]
        for i in range(5):
            gridValues[i][i + 2] = diag[10][i]
            gridValues[i + 4][i] = diag[4][i]
        for i in range(4):
            gridValues[i][i + 3] = diag[11][i]
            gridValues[i + 5][i] = diag[3][i]
        for i in range(3):
            gridValues[i][i + 4] = diag[12][i]
            gridValues[i + 6][i] = diag[2][i]

        antidiag = str(returnAntidiagonal(gridValues))

        while (antidiag.find("1, 1, 1") != -1):
            antidiag = antidiag.replace("1, 1, 1", randomThree)
        while (antidiag.find("2, 2, 2") != -1):
            antidiag = antidiag.replace("2, 2, 2", randomThree)
        while (antidiag.find("3, 3, 3") != -1):
            antidiag = antidiag.replace("3, 3, 3", randomThree)
        while (antidiag.find("4, 4, 4") != -1):
            antidiag = antidiag.replace("4, 4, 4", randomThree)
        while (antidiag.find("5, 5, 5") != -1):
            antidiag = antidiag.replace("5, 5, 5", randomThree)
        while (antidiag.find("6, 6, 6") != -1):
            antidiag = antidiag.replace("6, 6, 6", randomThree)

        antidiag = ast.literal_eval(antidiag)

        for i in range(len(gridValues)):
            gridValues[i] = list(gridValues[i])
        for i in range(7):
            gridValues[i][i] = antidiag[8][i]
            gridValues[i + 1][i] = antidiag[7][i]
            gridValues[i + 2][i] = antidiag[6][i]
        for i in range(6):
            gridValues[i][i + 1] = antidiag[9][i]
            gridValues[i + 3][i] = antidiag[5][i]
        for i in range(5):
            gridValues[i][i + 2] = antidiag[10][i]
            gridValues[i + 4][i] = antidiag[4][i]
        for i in range(4):
            gridValues[i][i + 3] = antidiag[11][i]
            gridValues[i + 5][i] = antidiag[3][i]
        for i in range(3):
            gridValues[i][i + 4] = antidiag[12][i]
            gridValues[i + 6][i] = antidiag[2][i]
    return gridValues


# given an integer x, and a number (from 1-6), the number is put in a string x times and is seperated by a space each time.
def numString2(num, x):
    one = "1 " * x
    length = len(one) - 1
    one = one[0:length]
    two = "2 " * x
    two = two[0:length]
    three = "3 " * x
    three = three[0:length]
    four = "4 " * x
    four = four[0:length]
    five = "5 " * x
    five = five[0:length]
    six = "6 " * x
    six = six[0:length]
    if (num == 1):
        return one
    elif (num == 2):
        return two
    elif (num == 3):
        return three
    elif (num == 4):
        return four
    elif (num == 5):
        return five
    elif (num == 6):
        return six


# given an integer x, and a number (from 1-6), the number is put in a string x times and is seperated by a comma and sapce each time.
def numString(num, x):
    one = "1, " * x
    length = len(one) - 2
    one = one[0:length]
    two = "2, " * x
    two = two[0:length]
    three = "3, " * x
    three = three[0:length]
    four = "4, " * x
    four = four[0:length]
    five = "5, " * x
    five = five[0:length]
    six = "6, " * x
    six = six[0:length]
    if (num == 1):
        return one
    elif (num == 2):
        return two
    elif (num == 3):
        return three
    elif (num == 4):
        return four
    elif (num == 5):
        return five
    elif (num == 6):
        return six


# It is at this moment that I ditch the diagonal/antidiagonal idea! I realized that it is not a requirement.
# finds all instances of "x" of the same non-zero number in a row/column. Returns indexes of such instances in the string version of the gridValues
def getRepeats(x, gridValues):
    one = numString2(1, x)
    two = numString2(2, x)
    three = numString2(3, x)
    four = numString2(4, x)
    five = numString2(5, x)
    six = numString2(6, x)
    horiz = []
    vert = []
    strGrid = str(gridValues).replace("[", "").replace("]", "").replace(",", "")
    if (strGrid.find(one) != -1):
        horiz += [int(0.5 * strGrid.find(one))]
    if (strGrid.find(two) != -1):
        horiz += [int(0.5 * strGrid.find(two))]
    if (strGrid.find(three) != -1):
        horiz += [int(0.5 * strGrid.find(three))]
    if (strGrid.find(four) != -1):
        horiz += [int(0.5 * strGrid.find(four))]
    if (strGrid.find(five) != -1):
        horiz += [int(0.5 * strGrid.find(five))]
    if (strGrid.find(six) != -1):
        horiz += [int(0.5 * strGrid.find(six))]

    strGrid = str(transpose(gridValues)).replace("[", "").replace("]", "").replace(",", "").replace("(", "").replace(
        ")", "")

    if (strGrid.find(one) != -1):
        vert += [int(0.5 * strGrid.find(one))]
    if (strGrid.find(two) != -1):
        vert += [int(0.5 * strGrid.find(two))]
    if (strGrid.find(three) != -1):
        vert += [int(0.5 * strGrid.find(three))]
    if (strGrid.find(four) != -1):
        vert += [int(0.5 * strGrid.find(four))]
    if (strGrid.find(five) != -1):
        vert += [int(0.5 * strGrid.find(five))]
    if (strGrid.find(six) != -1):
        vert += [int(0.5 * strGrid.find(six))]

    return horiz, vert


def replaceAndPoints(gridValues):
    tempGrid = gridValues.copy()
    flatnump = numpy.asarray(gridValues).flatten()
    three = getRepeats(3, gridValues)
    four = getRepeats(4, gridValues)
    five = getRepeats(5, gridValues)
    six = getRepeats(6, gridValues)
    seven = getRepeats(7, gridValues)
    eight = getRepeats(8, gridValues)
    nine = getRepeats(9, gridValues)
    points = []
    for i in range(len(tempGrid)):
        tempGrid[i] = str(tempGrid[i])

    if (len(three[0]) > 0):
        if (len(nine[0]) > 0):
            for i in range(len(nine[0])):
                temp = flatnump[nine[0][i]]
                temp = numString(temp, 9)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(9):
                            points += [(j, int((tempGrid[j].find(temp) - 1) * (1 / 3)) + k)]
        if (len(eight[0]) > 0):
            for i in range(len(eight[0])):
                temp = flatnump[eight[0][i]]
                temp = numString(temp, 8)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(8):
                            points += [(j, int((tempGrid[j].find(temp) - 1) * (1 / 3)) + k)]
        if (len(seven[0]) > 0):
            for i in range(len(seven[0])):
                temp = flatnump[seven[0][i]]
                temp = numString(temp, 7)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(7):
                            points += [(j, int((tempGrid[j].find(temp) - 1) * (1 / 3)) + k)]
        if (len(six[0]) > 0):
            for i in range(len(six[0])):
                temp = flatnump[six[0][i]]
                temp = numString(temp, 6)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(6):
                            points += [(j, int((tempGrid[j].find(temp) - 1) * (1 / 3)) + k)]
        if (len(five[0]) > 0):
            for i in range(len(five[0])):
                temp = flatnump[five[0][i]]
                temp = numString(temp, 5)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(5):
                            points += [(j, int((tempGrid[j].find(temp) - 1) * (1 / 3)) + k)]
        if (len(four[0]) > 0):
            for i in range(len(four[0])):
                temp = flatnump[four[0][i]]
                temp = numString(temp, 4)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(4):
                            points += [(j, int((tempGrid[j].find(temp) - 1) * (1 / 3)) + k)]
        if (len(three[0]) > 0):
            for i in range(len(three[0])):
                temp = flatnump[three[0][i]]
                temp = numString(temp, 3)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(3):
                            points += [(j, int((tempGrid[j].find(temp) - 1) * (1 / 3)) + k)]

    tempGrid = transpose(gridValues)
    flatnump = numpy.asarray(tempGrid).flatten()
    for i in range(len(tempGrid)):
        tempGrid[i] = str(tempGrid[i])

    if (len(three[1]) > 0):
        if (len(nine[1]) > 0):
            for i in range(len(nine[1])):
                temp = flatnump[nine[1][i]]
                temp = numString(temp, 9)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(9):
                            points += [(int(((tempGrid[j].find(temp) - 1) * (1 / 3) + k)), j)]
        if (len(eight[1]) > 0):
            for i in range(len(eight[1])):
                temp = flatnump[eight[1][i]]
                temp = numString(temp, 8)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(8):
                            points += [(int(((tempGrid[j].find(temp) - 1) * (1 / 3) + k)), j)]
        if (len(seven[1]) > 0):
            for i in range(len(seven[1])):
                temp = flatnump[seven[1][i]]
                temp = numString(temp, 7)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(7):
                            points += [(int(((tempGrid[j].find(temp) - 1) * (1 / 3) + k)), j)]
        if (len(six[1]) > 0):
            for i in range(len(six[1])):
                temp = flatnump[six[1][i]]
                temp = numString(temp, 6)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(6):
                            points += [(int(((tempGrid[j].find(temp) - 1) * (1 / 3) + k)), j)]
        if (len(five[1]) > 0):
            for i in range(len(five[1])):
                temp = flatnump[five[1][i]]
                temp = numString(temp, 5)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(5):
                            points += [(int(((tempGrid[j].find(temp) - 1) * (1 / 3) + k)), j)]
        if (len(four[1]) > 0):
            for i in range(len(four[1])):
                temp = flatnump[four[1][i]]
                temp = numString(temp, 4)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(4):
                            points += [(int(((tempGrid[j].find(temp) - 1) * (1 / 3) + k)), j)]
        if (len(three[1]) > 0):
            for i in range(len(three[1])):
                temp = flatnump[three[1][i]]
                temp = numString(temp, 3)
                for j in range(len(tempGrid)):
                    if (tempGrid[j].find(temp) != -1):
                        for k in range(3):
                            points += [(int(((tempGrid[j].find(temp) - 1) * (1 / 3) + k)), j)]
    points = list(set(points))
    for i in range(len(points)):
        gridValues[points[i][0]][points[i][1]] = 0

    return gridValues, points


# replaces a certain "x" in an array with "y", and returns the new array
def replaceInArray(list, x, y):
    return ast.literal_eval(str(list).replace(str(x), str(y)))


# draws an enormous white square. This will be used to erase everything
def allErase():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledSquare(0, 0, 9999)


# draws white square -- I usually use this to erase shapes
def erase(x, y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledSquare(x, y, 50)


# draws red circle centered on the point given
def drawRCircle(x, y):
    erase(x, y)
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledCircle(x, y, r)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.circle(x, y, r)


# draws yellow square centered on the point given
def drawYSquare(x, y):
    erase(x, y)
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.filledSquare(x, y, r)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.square(x, y, r)


# draws magenta diamond centered on the point given
def drawPDiamond(x, y, colour=stddraw.MAGENTA):
    x1 = [x - 40, x, x + 40, x]
    y1 = [y, y + 40, y, y - 40]
    erase(x, y)
    stddraw.setPenColor(colour)
    stddraw.filledPolygon(x1, y1)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.polygon(x1, y1)


# draws blue hexagon centered on the point given
def drawBHexagon(x, y):
    a = 20 * math.sqrt(3)
    x1 = [x - 40, x - 20, x + 20, x + 40, x + 20, x - 20]
    y1 = [y, y + a, y + a, y, y - a, y - a]
    erase(x, y)
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.filledPolygon(x1, y1)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.polygon(x1, y1)


# draws an orange equilateral triangle centered on the point given
def drawOTriangle(x, y):
    a = 20 * math.sqrt(3)
    x1 = [x - 40, x, x + 40]
    y1 = [y - a, y + a, y - a]
    erase(x, y)
    stddraw.setPenColor(stddraw.ORANGE)
    stddraw.filledPolygon(x1, y1)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.polygon(x1, y1)


# draws a green parallelogram centered on the given point
def drawGParallelogram(x, y):
    a = 14 * math.sqrt(3)
    x1 = [x - 42, x - 14, x + 42, x + 14]
    y1 = [y - a, y + a, y + a, y - a]
    erase(x, y)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.filledPolygon(x1, y1)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.polygon(x1, y1)


# when the user clicks somewhere in the window, a corresponding row and column associated with gridValues is outputted
def clickToValue():
    row = 9
    col = 9
    while (row == 9 or col == 9):
        waitForClick()
        y = stddraw.mouseY()
        x = stddraw.mouseX()

        if (y < 450 and y > 350):
            row = 0
        elif (y < 350 and y > 250):
            row = 1
        elif (y < 250 and y > 150):
            row = 2
        elif (y < 150 and y > 50):
            row = 3
        elif (y < 50 and y > -50):
            row = 4
        elif (y < -50 and y > -150):
            row = 5
        elif (y < -150 and y > -250):
            row = 6
        elif (y < -250 and y > -350):
            row = 7
        elif (y < -350 and y > -450):
            row = 8
        else:
            row = 9

        if (x < 350 and x > 250):
            col = 6
        elif (x < 250 and x > 150):
            col = 5
        elif (x < 150 and x > 50):
            col = 4
        elif (x < 50 and x > -50):
            col = 3
        elif (x < -50 and x > -150):
            col = 2
        elif (x < -150 and x > -250):
            col = 1
        elif (x < -250 and x > -350):
            col = 0
        else:
            col = 9

    return row, col


# swaps two taffies if they are adjacent, and the said swap will cause a row or column of 3 of the same taffies to occur
def swap(gridValues):
    gridVal = (0, 0)
    gridVal2 = (0, 0)
    notDone = True
    notDone2 = True
    lastVal = 0
    lastVal2 = 0
    while (notDone2):
        while (notDone):
            gridVal = clickToValue()
            stddraw.setPenColor(stddraw.RED)
            stddraw.square(-300 + 100 * gridVal[1], 400 - 100 * gridVal[0], 48.5)
            gridVal2 = clickToValue()
            if (gridVal2 == (gridVal[0] + 1, gridVal[1]) or gridVal2 == (gridVal[0] - 1, gridVal[1]) or gridVal2 == (
                    gridVal[0], gridVal[1] + 1) or gridVal2 == (gridVal[0], gridVal[1] - 1)):
                temp = gridValues[gridVal[0]][gridVal[1]]
                gridValues[gridVal[0]][gridVal[1]] = gridValues[gridVal2[0]][gridVal2[1]]
                gridValues[gridVal2[0]][gridVal2[1]] = temp
                fillValue(gridVal[0], gridVal[1], gridValues)
                fillValue(gridVal2[0], gridVal2[1], gridValues)
                notDone = False
            else:
                fillValue(gridVal[0], gridVal[1], gridValues)
        stddraw.show(250)
        if (not horizCheck(gridValues) or not vertCheck(gridValues)):
            gridValues = replaceAndPoints(gridValues)
            refresh(gridValues[0])
            notDone2 = False
        else:
            temp = gridValues[gridVal[0]][gridVal[1]]
            gridValues[gridVal[0]][gridVal[1]] = gridValues[gridVal2[0]][gridVal2[1]]
            gridValues[gridVal2[0]][gridVal2[1]] = temp
            fillValue(gridVal[0], gridVal[1], gridValues)
            fillValue(gridVal2[0], gridVal2[1], gridValues)
        if (horizCheck(gridValues) and vertCheck(gridValues) and notDone2):
            notDone = True
    return gridValues[0], gridValues[1]


# draws a certain shape at a certain location according to the row and column of the gridValue array inputted
def fillValue(i, j, gridValues):
    x = -300 + 100 * j
    y = 400 - 100 * i
    if (gridValues[i][j] == 1):
        drawRCircle(x, y)
    elif (gridValues[i][j] == 2):
        drawYSquare(x, y)
    elif (gridValues[i][j] == 3):
        drawPDiamond(x, y)
    elif (gridValues[i][j] == 4):
        drawBHexagon(x, y)
    elif (gridValues[i][j] == 5):
        drawOTriangle(x, y)
    elif (gridValues[i][j] == 6):
        drawGParallelogram(x, y)
    else:
        erase(x, y)


# refreshes the board according to whatever new "gridValues" array inputted
def refresh(gridValues):
    for i in range(len(gridValues)):
        for j in range(len(gridValues[0])):
            x = -300 + 100 * j
            y = 400 - 100 * i
            if (gridValues[i][j] == 1):
                drawRCircle(x, y)
            elif (gridValues[i][j] == 2):
                drawYSquare(x, y)
            elif (gridValues[i][j] == 3):
                drawPDiamond(x, y)
            elif (gridValues[i][j] == 4):
                drawBHexagon(x, y)
            elif (gridValues[i][j] == 5):
                drawOTriangle(x, y)
            elif (gridValues[i][j] == 6):
                drawGParallelogram(x, y)
            else:
                erase(x, y)


# given a 2 dimensional array and a value inside the array, this method returns the exact index where that value occurs
def twoDIndex(list, val):
    for i, j in enumerate(list):
        if val in j:
            return (i, j.index(val))


# this code is responsible for making taffies fall -- if there's a "blank" tile below, the tile obove switches with it
def fall(gridValues):
    notDone2 = True
    while (notDone2):
        notDone = bool(twoDIndex(gridValues, 0))
        stddraw.show(100)
        while (notDone):
            point = twoDIndex(gridValues, 0)
            if (point):
                if (point[0] != 0):
                    gridValues[point[0]][point[1]] = gridValues[point[0] - 1][point[1]]
                    gridValues[point[0] - 1][point[1]] = 0
                    stddraw.show(35)
                    refresh(replaceInArray(gridValues, -1, 0))
                else:
                    gridValues[point[0]][point[1]] = -1
            else:
                notDone = False
        if (not notDone and not bool(twoDIndex(gridValues, 0))):
            notDone2 = False
        elif (not bool(twoDIndex(gridValues, 0))):
            notDone = True

    return replaceInArray(gridValues, -1, 0)


# checks if 3 in a row or column occur, and performs the appropriate actions if such instances occur
def whileCheck(gridValues):
    points = 0
    while (not horizCheck(gridValues) or not vertCheck(gridValues)):
        temp = replaceAndPoints(gridValues)
        gridValues = temp[0]
        points += len(temp[1])
        gridValues = fall(gridValues)
        refresh(gridValues)
    return gridValues, points


# makes new taffies fall if there are "blank" tiles at the top most region of the grid
def reloadTaffies(gridValues):
    notDone = True
    while (notDone):
        temp = False
        for i in range(7):
            while (gridValues[0][i] == 0):
                gridValues[0][i] = random.randint(1, 6)
                gridValues = fall(gridValues)
                refresh(gridValues)
                pointsAndGrid = whileCheck(gridValues)
        notDone = False
        for i in range(7):
            temp = temp or gridValues[0][i] == 0
        if (temp):
            notDone = True
    return pointsAndGrid[0], pointsAndGrid[1]


# waits until the heat death of the universe unless the user clicks inside the window
def waitForClick():
    while (not stddraw.mousePressed()):
        stddraw.show(10)


# draws score when called
def showScore(score, x=0):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-350, 450, 700, 100)
    score = "Score: " + str(score)
    stddraw.setFontSize(60)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(-210 + x, 500, score)


# called when the user wins. 8 possible endings
def win(score, startTime):
    t = round(time.time() - startTime, 2)
    winTime = "Time Elapsed: " + str(t) + " seconds"
    if (t <= 31 and score >= 73):
        rating = 7
        text = "YOU ARE A CHAMPION -- YOU WIN!"
    elif (t <= 31 and score >= 69):
        rating = 6
        text = "Incredible!! Masterfully done!!"
    elif (t <= 31):
        rating = 5
        text = "Great job! Go get em' champ!!"
    elif (t <= 40):
        rating = 4
        text = "Good. Not perfect, but not bad!"
    elif (t <= 48):
        rating = 3
        text = "Sufficient, but could be better."
    elif (t <= 56):
        rating = 2
        text = "What's taking so long, slowpoke?"
    elif (t <= 70):
        rating = 1
        text = "Seriously, were you even trying?"
    else:
        rating = 0
        text = "Exceptional. Exceptionally bad, that is."
    allErase()
    for i in range(210):
        showScore(score, 1 + i)
        stddraw.show(5)
    stddraw.show(1500)
    stddraw.setFontSize(40)
    stddraw.setPenColor(stddraw.DARK_GRAY)
    stddraw.text(0, 400, winTime)
    stddraw.show(1000)
    stddraw.setFontSize(60)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(0, 200, "Rating")
    stddraw._thickLine(-90, 167, 90, 167, 2)
    stddraw.show(1000)
    stddraw.setFontSize(30)
    stddraw.setPenColor(stddraw.DARK_GRAY)
    stddraw.text(0, -350, text)
    stddraw.setFontSize(300)
    if (rating >= 6):
        stddraw.setPenColor(stddraw.MAGENTA)
        stddraw.text(0, -50, str(rating) + "/5")
    elif (rating == 5):
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.text(0, -50, str(rating) + "/5")
    elif (rating == 4):
        stddraw.setPenColor(stddraw.BOOK_BLUE)
        stddraw.text(0, -50, str(rating) + "/5")
    elif (rating == 3):
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.text(0, -50, str(rating) + "/5")
    elif (rating == 2):
        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.text(0, -50, str(rating) + "/5")
    elif (rating == 1):
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(0, -50, str(rating) + "/5")
    else:
        stddraw.setPenColor(stddraw.BOOK_RED)
        stddraw.text(0, -50, str(rating) + "/5")
    if (rating != 7):
        stddraw.show(1500)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setFontSize(30)
        stddraw.text(170, -500, "Click anywhere to exit.")
        waitForClick()
    else:
        val = True
        count = 0
        list = [stddraw.MAGENTA, stddraw.RED, stddraw.BLUE, stddraw.CYAN, stddraw.YELLOW, stddraw.GREEN]
        while (not stddraw.mousePressed()):
            count += 1
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.filledRectangle(-300, -200, 700, 300)
            stddraw.setPenColor(list[random.randint(0, 5)])
            stddraw.text(0, -50, str(rating) + "/5")
            if (val and count >= 30):
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.setFontSize(30)
                stddraw.text(170, -500, "Click anywhere to exit.")
                stddraw.setFontSize(300)
                val = False
            stddraw.show(45)


# declare variables
r = 40.0
notDone = True

# set scale of drawing
stddraw.setXscale(-350, 350)
stddraw.setYscale(-550, 550)
stddraw.setCanvasSize(560, 880)

# Tells user what the game is, and waits for a click on the window
stddraw.setFontSize(160)
stddraw.setPenColor(stddraw.BLUE)
stddraw.text(0, 350, "TAFFY")
stddraw.setPenColor(stddraw.BOOK_BLUE)
stddraw.text(0, 180, "TANGLE")
stddraw.setPenColor(stddraw.BLACK)
stddraw.setFontSize(40)
stddraw.text(0, 20, "Each taffy is 1 point.")
stddraw.text(0, -60, "Reach 60 points as")
stddraw.text(0, -120, "fast as you can!")
stddraw.setPenColor(stddraw.DARK_GRAY)
stddraw.setFontSize(30)
while (not stddraw.mousePressed()):
    stddraw.text(0, -300, "Click anywhere to start!")
    stddraw.show(350)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-300, -350, 700, 100)
    stddraw.show(350)
    stddraw.setPenColor(stddraw.DARK_GRAY)

# gets rid of everything except "TAFFY TANGLE"
stddraw.setPenColor(stddraw.WHITE)
stddraw.filledRectangle(-350, -350, 700, 400)
stddraw.setFontSize(160)

# cool transition into the game
for i in range(130):
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.text(-8 * i, 350, "TAFFY")
    stddraw.setPenColor(stddraw.BOOK_BLUE)
    stddraw.text(8 * i, 180, "TANGLE")
    stddraw.show(5)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(-350, -550, 1000, 1000)

# initializes board
gridValues = randomValues()
refresh(gridValues)
points = 0
startTime = time.time()

# loops forever or until the user wins (aka the user gets 60 points)
while (notDone):
    showScore(points)
    if (not twoDIndex(gridValues, 0)):
        temp = swap(gridValues)
        gridValues = temp[0]
        points += len(temp[1])
        gridValues = fall(gridValues)
        refresh(gridValues)
        temp = whileCheck(gridValues)
        gridValues = temp[0]
        points += temp[1]
    temp = False
    for i in range(7):
        temp = temp or gridValues[0][i] == 0
    if (temp):
        temp = reloadTaffies(gridValues)
        gridValues = temp[0]
        points += temp[1]
    stddraw.show(10)
    if (points >= 60):
        notDone = False
        win(points, startTime)
