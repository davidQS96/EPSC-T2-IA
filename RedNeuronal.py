#Importacion de bibliotecas
from random import random



#Importacion de clase neurona
from Neurona import *

class NeuronalNetwork:

    def __init__(self, numInputs = 1, numOutputs = 1, numHidden = 1):
        self.numInputs = -1
        self.numOutputs = -1
        self.numHidden = -1

        if type(numInputs) != int or numInputs < 1:
            print("NeuronalNetwork.__init__: valor de numero de entradas no es valido, se asigna un valor de 1")
            self.numInputs = 1

        if type(numOutputs) != int or numOutputs < 1:
            print("NeuronalNetwork.__init__: valor de numeros de salidas no es valido, se asigna un valor de 1")
            self.numOutputs = 1

        if type(numHidden) != int or numHidden < 1:
            print("NeuronalNetwork.__init__: valor de numero neuronas ocultas no es valido, se asigna un valor de 1")
            self.numHidden = 1

        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.numHidden = numHidden

        self.inputNeurons = []
        self.outputNeurons = []
        self.hiddenNeurons = []

        self.trainingData = [] #Lista de listas con los datos de entrada

        self.percTraining = 0.7 #Predefinido, menor o igual a 1
        self.batch = 5 #Numero de sets de datos por iteracion
        self.trainingData = [] #Datos de cada cambio en la red por iteracion


    def createNetwork(self):
        for inNeuronNum in range(self.numInputs):
            print("Neurona in ", inNeuronNum + 1)

            self.inputNeurons += [Neuron()]

        for outNeuronNum in range(self.numOutputs):
            print("Neurona out ", outNeuronNum + 1)

            self.outputNeurons += [Neuron()]

        for hidNeuronNum in range(self.numHidden):
            print("Neurona hidd ", hidNeuronNum + 1)

            self.hiddenNeurons += [Neuron()]

        self.initializeNeuronParameters()


    def initializeNeuronParameters(self):

        #Neuronas entrada, tienen un ConnectionIn con neurona None
        for inNeuron in self.inputNeurons:
            inNeuron.addInputConn(ConnectionIn(None))

        #Neuronas salida, tienen una neurona de salida None y func activacion relu siempre (datos de salida esperados estan entre 0 y +inf)
        for outNeuron in self.outputNeurons:
            outNeuron.addOutputNeuron(None)
            outNeuron.setActivFunct("ReLU")

        for hiddNeuron in self.hiddenNeuron:
            pass


    def linkNeurons(self):
        return









