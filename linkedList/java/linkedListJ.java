package java;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
public class linkedListJ {
    private NodeJ head;
    private int length;

    public linkedListJ() {
        this.head = null;
        this.length = 0;
    }

    public int getLength() {
        return this.length;
    }

    public void ler(File file){
        try {
            Scanner scanner = new Scanner(file);
            String firstLine = scanner.nextLine();
            // Adicionando os elementos da primeira linha
            String[] firstLineSplit = firstLine.split(" ");
            for (int i = 0; i < firstLineSplit.length; i++){
                int data = Integer.parseInt(firstLineSplit[i]);
                this.adicionar(data, i + 1);
            }
            
            // Segunda linha
            String secondLine = scanner.nextLine();
            int qtdAcoes = Integer.parseInt(secondLine);

            for (int i = 0; i < qtdAcoes; i++){
                String acao = scanner.nextLine();
                String[] acaoSplit = acao.split(" ");
                if (acaoSplit[0].equals("A")){
                    this.adicionar(Integer.parseInt(acaoSplit[1]), Integer.parseInt(acaoSplit[2]));
                } else if (acaoSplit[0].equals("R")){
                    this.remover(Integer.parseInt(acaoSplit[1]));
                } else if (acaoSplit[0].equals("P")){
                    this.mostrar();
                }
            }
            scanner.close();

        } catch (Exception e) {
            System.out.println(e);
            System.out.println("Arquivo não encontrado");
        }
    }

    public void adicionar(int data, int position){
        NodeJ newNode = new NodeJ(data);
        if (position == 1){
            // Adicionando no início
            newNode.setNext(this.head);
            this.head = newNode;

            this.length++;
        } else if(position > 1 && position <= this.length + 1){
            // Adicionando em qualquer outro elemento
            NodeJ atual = this.head;
            for (int i = 1; i < position - 1; i++){
                atual = atual.getNext();
            }
            newNode.setNext(atual.getNext());
            atual.setNext(newNode);
            
            this.length++;
        } else {
            System.out.println("Posição inválida");

        }
    }
    public void remover(int data){
        if (head.getData() == data){
            // Removendo o primeiro elemento
            this.head = this.head.getNext();

            this.length--;
        } else {
            // Removendo qulquer outro elemento
            NodeJ atual = this.head;
            while (atual.getNext() != null){
                if (atual.getNext().getData() == data){
                    atual.setNext(atual.getNext().getNext());
                    this.length--;
                    return;
                }
                atual = atual.getNext();

            }
            System.out.println("Elemento não encontrado");
        }
    }
    public void mostrar(){
        NodeJ atual = this.head;
        ArrayList<Integer> lista = new ArrayList<Integer>();

        while (atual != null){
            lista.add(atual.getData());
            atual = atual.getNext();
        }
        System.out.println(lista);
    }
}
