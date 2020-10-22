import math
import numpy as np

#Clase que incluye neuronas vecinas y parametros correspondientes a la entrada de una neurona
class ConnectionIn:


    #Metodo constructor
    def __init__(self, neuron = None, inputValue = 0, weight = 0):
        self.neuron = neuron
        self.inputValue = inputValue
        self.weight = weight


    #Añade una neurona en la conexion o None si es entrada de red
    def setNeuronLink(self, neuron):
        if(type(neuron) != Neuron):
            print("ConnectionIn.setNeuronLink: la entrada no es de tipo Neuron")
            return -1

        self.neuron = neuron

        return 0


    #Asigna valor de entrada a conexion
    def setInputValue(self, inputValue):
        if(type(inputValue) != float):
            print("ConnectionIn.setInputValue: la entrada no es de tipo float")
            return -1

        self.inputValue = inputValue

        return 0


    #Asigna peso a conexion
    def setWeight(self, weight):
        if(type(weight) != float):
            print("ConnectionIn.setWeight: la entrada no es de tipo float")
            return -1

        self.weight = weight

        return 0


#Clase que crea una neurona perceptron
class Neuron:

    #Metodo constructor
    def __init__(self):

        self.inputConnections = [] #Objetos ConnectionIn
        self.inputNeurons = [] #Objetos Neuron
        self.outputNeurons = [] #Objetos Neuron

        self.activFunct    = "Sigmoid"
        self.possibleAFncs = {"Sigmoid":  lambda x: 1 / (1 + math.e ** (-x)),
                              "Tanh":     lambda x: (2 / (1 + math.e ** (-2 * x))) - 1,
                              "ReLU":     lambda x: x if x > 0 else 0,
                              "Identity": lambda x: x}
        self.netValue      = 0
        self.outputValue   = 0


    #Se calcula y actualiza el valor neto de la neurona y devuelve el resultado
    def calcNetValue(self):
        netSum = 0

        for conn in self.inputConnections:
            netSum += conn.inputValue * conn.weight

        self.netValue = netSum
        return netSum


    #Se cambia la func. acticacion activa
    def setActivFunct(self, activFunct):
        if(activFunct not in self.possibleAFncs):
            print("Neuron.setActivFunct: entrada no es una func. activacion valida")
            return -1

        self.activFunct = activFunct
        return 0


    #Calcula funcion de activacion y devuelve el resultado
    def calcFuncActiv(self):
        self.outputValue = self.possibleAFncs[self.activFunct](self.netValue)
        return self.outputValue


    #Calcula la salida de la neurona
    def calcOutput(self):
        self.calcNetValue()
        return calcFuncActiv()


    #Asigna un peso fijo a cada conexion de entrada
    def setFixedWeights(self, newWeight):
        if(type(newWeight) != float):
            print("Neuron.setFixedWeight: entrada no es tipo float")
            return -1

        for inputConn in self.inputConnections:
            inputConn.setWeight(newWeight)

        return 0


    #Asigna un peso diferente a cada conexion de entrada
    def setDiffWeights(self, weights):
        if(type(weights) != list):
            print("Neuron.setDiffWeights: entrada no es tipo list")
            return -1

        if(len(weights) != len(self.inputConnections)):
            print("Neuron.setDiffWeights: tamaño de lista de entrada no coincide con numero de conexiones")
            return -1

        for elem in weights:
            if(type(elem) != float):
                print("Neuron.setDiffWeights: algun elemento de lista no es tipo float")
                return -1

        for ix in range(len(self.inputConnections)):
            self.inputConnections[ix].setWeight(weights[ix])

        return 0


    #Asigna un peso con ruido gaussiano -25% a +25% a cada conexion de entrada
    def setGaussWeights(self, meanWeight):
        if(type(meanWeight) != float):
            print("Neuron.setGaussWeights: entrada no es tipo float")
            return -1

        sigma = meanWeight / 12 #99.73 son datos entre 0.75mu y 1.25 mu%

        for inputConn in self.inputConnections:
            weight = 0
            while(weight < meanWeight * 0.75 or weight > meanWeight * 1.25): #Se asegura que unicamente aparezcan valores entre el rango, nada mas, nada menos
                #https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
                weight = desv * np.random.randn() + meanWeight

            inputConn.setWeight(weight)

        return 0


    #Añade una conexion de entrada, primero verifica posibles errores
    def addInputConn(self, *inputConns):
        if len(self.inputConnections) == 1 and self.inputConnections[0].neuron == None:
            print("Neuron.addInputConn: no se pueden agregar conexiones si ya se tiene una tipo None (entrada de red)")
            return -1

        for ix in range(len(inputConns)):
            if(type(inputConns[ix]) != ConnectionIn):
                print("Neuron.addInputConn: una de las entradas no es de tipo ConnectionIn")
                return -1

            if(inputConns[ix] == self):
                print("Neuron.addInputConn: la conexion no se puede autoreferenciar")
                return -1

            if(inputConns[ix] in self.inputConnections):
                print("Neuron.addInputConn: no se puede agregar una conexion que ya existia")
                return -1

            if(inputConns[ix] in inputConns[(ix + 1):]):
                print("Neuron.addInputConn: no se pueden agregar 2 o mas objetos ConnectionIn identicos")
                return -1

            if(inputConns[ix].neuron == None and len(inputConns) > 1):
                print("Neuron.addInputConn: no se pueden agregar conexiones de entrada si una agregada es None (entrada de red)")
                return -1

        for inputConn in inputConns:
            self.inputNeurons += [inputConn.neuron]
            self.inputConnections += [inputConn]

        return 0


    #Añade una neurona de entrada, primero verifica posibles errores
    def addInputNeuron(self, *neurons):
        for ix in range(len(neurons)):
            if(type(neurons[ix]) != Neuron):
                print("Neuron.addInputNeuron: una de las entradas no es de tipo Neuron")
                return -1

            if(neurons[ix] == self):
                print("Neuron.addInputNeuron: la neurona no se puede autoreferenciar")
                return -1

            if(neurons[ix] in self.inputNeurons):
                print("Neuron.addInputNeuron: no se puede agregar una neurona de entrada que ya existia")
                return -1

            if(neurons[ix] != None and neurons[ix] in self.outputNeurons):
                print("Neuron.addInputNeuron: una neurona de salida no puede ser de entrada")
                return -1

            if(neurons[ix] in neurons[(ix + 1):]):
                print("Neuron.addInputNeuron: no se pueden agregar 2 o mas objetos Neurona identicos")
                return -1

        for neuron in neurons:
            self.addInputConn(ConnectionIn(neuron = neuron))

        return 0


    #Añade una neurona de salida, primero verifica posibles errores
    def addOutputNeuron(self, *neurons):
        if len(self.outputNeurons) == 1 and self.outputNeurons[0] == None:
            print("Neuron.addOutputNeuron: no se pueden agregar neuronas si ya se tiene una tipo None (salida de red)")
            return -1

        for ix in range(len(neurons)):
            if(neurons[ix] != None and type(neurons[ix]) != Neuron):
                print("Neuron.addOutputNeuron: una de las entradas no es de tipo Neuron o None (salida de red)")
                return -1

            if(neurons[ix] == self):
                print("Neuron.addOutputNeuron: la neurona no se puede autoreferenciar")
                return -1

            if(neurons[ix] in self.outputNeurons):
                print("Neuron.addOutputNeuron: no se puede agregar una neurona de salida que ya existia")
                return -1

            if(neurons[ix] != None and neurons[ix] in self.inputNeurons):
                print("Neuron.addOutputNeuron: una neurona de entrada no puede ser de salida")
                return -1

            if(neurons[ix] in neurons[(ix + 1):]):
                print("Neuron.addOutputNeuron: no se pueden agregar 2 o mas objetos Neurona identicos")
                return -1

            if(neurons[ix] == None and len(neurons) > 1):
                print("Neuron.addOutputNeuron: no se pueden agregar neuronas de salida si una agregada es None (salida de red)")
                return -1

        for neuron in neurons:
            self.outputNeurons += [neuron]

        return 0













