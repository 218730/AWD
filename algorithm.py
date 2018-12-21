import numpy as np

class algorithm:
    def __init__(self, *options):
        self.opt = options #???

        self.CATEGORIES_COUNT = 5
        self.CROPS_COUNT = 6
        self.categoriesMatrix = np.array([[1.0, 1.0, 1.0, 1.0, 1.0],
                                          [1.0, 1.0, 1.0, 1.0, 1.0],
                                          [1.0, 1.0, 1.0, 1.0, 1.0],
                                          [1.0, 1.0, 1.0, 1.0, 1.0],
                                          [1.0, 1.0, 1.0, 1.0, 1.0]])
        self.categoriesMeansVector = np.zeros(self.CATEGORIES_COUNT)
        self.normalizedCategoriesMatrix = np.zeros((self.CATEGORIES_COUNT, self.CATEGORIES_COUNT))
        self.meansMatrix = np.zeros((self.CROPS_COUNT, self.CATEGORIES_COUNT))

        self.preferencesMatrices = list()
        self.normalizedPreferencesMatrices = list()


    def fillCategoriesMatrix(self, val, i, j):
        switcher = {
            1: 1.0/9.0,
            2: 1.0/7.0,
            3: 1.0/5.0,
            4: 1.0/3.0,
            5: 1.0,
            6: 3.0,
            7: 5.0,
            8: 7.0,
            9: 9.0
        }

        output = switcher.get(val, 0.0)
        self.categoriesMatrix[i,j]=output
        self.categoriesMatrix[j,i]=(output**(-1))
        

    def prepareVars(self):
        self.preferencesMatrices.append(np.genfromtxt('macierz1.csv', delimiter=';'))
        self.preferencesMatrices.append(np.genfromtxt('macierz2.csv', delimiter=';'))
        self.preferencesMatrices.append(np.genfromtxt('macierz3.csv', delimiter=';'))
        self.preferencesMatrices.append(np.genfromtxt('macierz4.csv', delimiter=';'))
        self.preferencesMatrices.append(np.genfromtxt('macierz5.csv', delimiter=';'))
        self.normalizedPreferencesMatrices.append(np.zeros((self.CROPS_COUNT, self.CROPS_COUNT)))
        self.normalizedPreferencesMatrices.append(np.zeros((self.CROPS_COUNT, self.CROPS_COUNT)))
        self.normalizedPreferencesMatrices.append(np.zeros((self.CROPS_COUNT, self.CROPS_COUNT)))
        self.normalizedPreferencesMatrices.append(np.zeros((self.CROPS_COUNT, self.CROPS_COUNT)))
        self.normalizedPreferencesMatrices.append(np.zeros((self.CROPS_COUNT, self.CROPS_COUNT)))
        if self.opt is not ():
            self.fillCategoriesMatrix(self.opt[1],1,0)
            self.fillCategoriesMatrix(self.opt[8],2,0)
            self.fillCategoriesMatrix(self.opt[6],3,0)
            self.fillCategoriesMatrix(self.opt[5],4,0)
            self.fillCategoriesMatrix(self.opt[4],4,3)
            self.fillCategoriesMatrix(self.opt[2],2,1)
            self.fillCategoriesMatrix(self.opt[9],3,1)
            self.fillCategoriesMatrix(self.opt[7],4,1)
            self.fillCategoriesMatrix(self.opt[3],3,2)
            self.fillCategoriesMatrix(self.opt[0],4,2)


    def fillNormalizedVector(self, originalMatrix):
        tmp = 0.0
        normalizedMatrix = np.zeros((len(originalMatrix),len(originalMatrix)))
        for i in range(len(originalMatrix)):
            tmp = 0.0
            for j in range(len(originalMatrix)):
                tmp += originalMatrix[j,i]
            for j in range(len(originalMatrix)):
                normalizedMatrix[j,i] = originalMatrix[j,i]*1.0/tmp
        return normalizedMatrix


    def checkConsistency(self, matrix: np.array, meansVector):
        RI = 0.0
        CI = 0.0
        suma = 0.0
        sumsVector = np.zeros(len(matrix))
        lambd = 0.0
        switcher = {
            2: 0.0,
            3: 0.58,
            4: 0.89,
            5: 1.11,
            6: 1.25,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49,
        }

        RI = switcher.get(len(matrix), 0.0)
        for i in range(len(matrix)):
            suma = 0.0
            for j in range(len(matrix)):
                suma += matrix[j, i]
            sumsVector[i] = suma
        
        for i in range(len(matrix)):
            lambd += sumsVector[i] * meansVector[i]

        CI = ((lambd - len(matrix)) / (RI * (len(matrix) - 1)))

        return CI


    def oblicz(self):
        self.prepareVars()

        CROPS = ["Nawra" , "Hezja", "Jasna", "Vinjett", "Zebra", "Bryza"]
        normalizedCategoriesMatrix = self.fillNormalizedVector(self.categoriesMatrix)
        categoriesMeansVector = np.mean(normalizedCategoriesMatrix, 1)
        consistency = self.checkConsistency(self.categoriesMatrix, categoriesMeansVector)
        ciString= "CI: %s" % consistency
        if(consistency>0.1):
            outputString ="CI: %s" % consistency + "\n" + "Dane nie są spójne!"
            return outputString
        for i in range(self.CATEGORIES_COUNT):
            self.normalizedPreferencesMatrices[i] = self.fillNormalizedVector(self.preferencesMatrices[i])
        for i in range(self.CATEGORIES_COUNT):
            self.setRow(self.meansMatrix, np.mean(self.normalizedPreferencesMatrices[i], 1), i)

        tmp = np.zeros((len(self.categoriesMatrix),1))

        for i in range(len(categoriesMeansVector)):
            tmp[i,0] = categoriesMeansVector[i]
        result = np.matmul(self.meansMatrix, tmp)

        wyniki = np.zeros(result.shape[0])
        for i in range(result.shape[0]):
            wyniki[i] = result[i, 0]
        
        temp = 0.0
        tmpCrop = ""

        for _ in range(len(wyniki)):
            for sort in range(len(wyniki)-1):
                if wyniki[sort] < wyniki[sort+1]:
                    temp = wyniki[sort+1]
                    wyniki[sort+1] = wyniki[sort]
                    wyniki[sort] = temp
                    tmpCrop = CROPS[sort+1]
                    CROPS[sort +1] = CROPS[sort]
                    CROPS[sort] = tmpCrop

        outputString = "CI: %s" % consistency + "\n"
        for i in range(len(wyniki)):
            outputString += str(i+1) + ". " + str(CROPS[i]) + ": " + str(wyniki[i]) + "\n"
        return outputString


    def setRow(self, matrix, vector, row):
        for i  in range(matrix.shape[0]):
            matrix[i, row] = vector[i]
        return


if __name__ == "__main__":
    ahp = algorithm()