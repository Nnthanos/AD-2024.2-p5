import java.util.ArrayList;
import java.util.List;

public class mergeSort {

    public static void ordenar(List<Integer> lista) {
        if (lista.size() > 1) {
            // Dividir a lista no meio
            int meio = lista.size() / 2;

            // Criar sublistas esquerda e direita (criar novas listas, não sublistas)
            List<Integer> esquerda = new ArrayList<>(lista.subList(0, meio));
            List<Integer> direita = new ArrayList<>(lista.subList(meio, lista.size()));

            // Ordenar as sublistas recursivamente
            ordenar(esquerda);
            ordenar(direita);

            // Mesclar as sublistas ordenadas
            mesclar(lista, esquerda, direita);
        }
    }

    private static void mesclar(List<Integer> lista, List<Integer> esquerda, List<Integer> direita) {
        int i = 0, j = 0, k = 0;

        // Combinar elementos de 'esquerda' e 'direita' na lista original
        while (i < esquerda.size() && j < direita.size()) {
            if (esquerda.get(i) <= direita.get(j)) {
                lista.set(k++, esquerda.get(i++));
            } else {
                lista.set(k++, direita.get(j++));
            }
        }

        // Adicionar os elementos restantes da esquerda (se houver)
        while (i < esquerda.size()) {
            lista.set(k++, esquerda.get(i++));
        }

        // Adicionar os elementos restantes da direita (se houver)
        while (j < direita.size()) {
            lista.set(k++, direita.get(j++));
        }
    }
}
