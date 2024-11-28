import java.util.List;

public class bubbleSort {

    public static void ordenar(List<Integer> lista) {
        System.out.println("Ordenando a lista...");
        int n = lista.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (lista.get(j) > lista.get(j + 1)) {
                    int temp = lista.get(j);
                    lista.set(j, lista.get(j + 1));
                    lista.set(j + 1, temp);
                }
            }
        }
    }
}


