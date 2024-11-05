from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def getLength(self):
        return self.length
    
    def adicionar(self, data, position):
        newNode = Node(data)
        if position == 1:
            newNode.setNext(self.head)
            self.head = newNode
        elif position > 1 and position <= self.length + 1:
            atual = self.head
            for i in range(position - 2):
                atual = atual.getNext()
            newNode.setNext(atual.getNext())
            atual.setNext(newNode)

        else:
            return "Posição Inválida"
        
        self.length += 1

        return "Adicionado com sucesso"
    
    def remover(self, posicion):
        if posicion == 1:
            self.head = self.head.getNext()
        
        elif posicion > 1 and posicion <= self.length:
            atual = self.head
            for i in range(posicion - 2):
                atual = atual.getNext()
            atual.setNext(atual.getNext().getNext())
        else:
            return "Posição Inválida"
        
        self.length -= 1
    
    
    def imprimir(self):
        atual = self.head
        while atual != None:
            print(atual.getData())
            atual = atual.getNext()
        