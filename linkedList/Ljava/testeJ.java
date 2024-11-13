package Ljava;
import java.io.File;
public class testeJ {
    public static void main(String[] args) {
        File file = new File("arqgrandinho.txt");
        linkedListJ lista = new linkedListJ();

        lista.ler(file);
    }
}
