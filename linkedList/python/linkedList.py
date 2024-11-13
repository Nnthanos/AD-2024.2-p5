from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def getLength(self):
        return self.length
    
    def ler(self, arquivo):
        with open(arquivo, 'r') as file:
            # Adicionando cada número na lista
            firstLine = file.readline()
            for char in (firstLine.split()):
                self.adicionar(char, self.length + 1)
            
            qtdAcoes = file.readline()
            
            for i in range(int(qtdAcoes)):
                line = file.readline()
                line = line.split()
                if line[0] == "A":
                    self.adicionar(line[1], int(line[2]))
                elif line[0] == "R":
                    self.remover(line[1])
                elif line[0] == "P":
                    self.imprimir()
                else:
                    print("Comando inválido! tente A, R ou P")
                
    
    def adicionar(self, data, position):
        newNode = Node(data)
        if position == 1:
            # Adicionando na primeira posição
            newNode.setNext(self.head)
            self.head = newNode
        elif position > 1 and position <= self.length + 1:
            # Adicionando em qualquer outra posição
            atual = self.head
            for i in range(position - 2):
                atual = atual.getNext()
            newNode.setNext(atual.getNext())
            atual.setNext(newNode)

        else:
            # Posição negativa ou fora do range
            return "Posição Inválida"
        
        self.length += 1

        return "Adicionado com sucesso"
    
    def remover(self, data):
        if self.head == None:
            return "Lista vazia"
        elif self.head.getData() == data:
            # Removendo o primeiro elemento
            self.head = self.head.getNext()
            self.length -= 1
            return "Removido com sucesso"
        else:
            # Removendo qualquer outro elemento
            atual = self.head
            while atual.getNext() != None:
                if atual.getNext().getData() == data:
                    atual.setNext(atual.getNext().getNext())
                    self.length -= 1

                    return "Removido com sucesso"
                atual = atual.getNext()       
        
        return "Elemento não encontrado"
    
    
    def imprimir(self):
        atual = self.head
        lista = []
        while atual != None:
            lista.append(atual.getData())
            atual = atual.getNext()
        print(lista)
        