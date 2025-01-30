
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class medeDesempenho {

    public static List<Integer> ler(String arquivo) {
        List<Integer> lista = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                lista.add(Integer.parseInt(linha.trim()));
            }
        } catch (IOException e) {
            System.err.println("Erro ao ler o arquivo: " + e.getMessage());
        }
        System.out.println("Arquivo lido com sucesso!");
        return lista;
    }

    public static void salvarListaEmArquivo(List<Integer> lista, String nomeArquivo) {
        File arquivo = new File(nomeArquivo);
        try {
            if (arquivo.exists()) {
                String base = nomeArquivo.substring(0, nomeArquivo.lastIndexOf('.'));
                String ext = nomeArquivo.substring(nomeArquivo.lastIndexOf('.'));
                int contador = 1;
                while (arquivo.exists()) {
                    arquivo = new File(base + "_" + contador + ext);
                    contador++;
                }
            }

            try (BufferedWriter bw = new BufferedWriter(new FileWriter(arquivo))) {
                for (int numero : lista) {
                    bw.write(numero + "\n");
                }
            }
            System.out.println("Lista ordenada salva em '" + arquivo.getAbsolutePath() + "'");
        } catch (IOException e) {
            System.err.println("Erro ao salvar o arquivo: " + e.getMessage());
        }
    }

    public static void salvarDadosEmPlanilha(double tempoMs, long memoriaKb, String metodo, String nomeArquivo) {
        File arquivo = new File(nomeArquivo);
        try {
            // Cria o arquivo se não existir
            if (!arquivo.exists()) {
                arquivo.createNewFile();
            }

            // Escrever os dados no arquivo CSV
            try (BufferedWriter bw = new BufferedWriter(new FileWriter(arquivo, true))) {
                // Verifica se é a primeira linha para escrever o cabeçalho
                if (arquivo.length() == 0) {
                    bw.write("Metodo,Tempo de Execucao (ms),Consumo de Memoria (KB),Versao do Java\n");
                }

                // Escreve os dados
                bw.write(metodo + "," + tempoMs + "," + memoriaKb + ",openjdk version '20.0.2'\n");
            }

            System.out.println("Dados salvos em '" + arquivo.getAbsolutePath() + "'");
        } catch (IOException e) {
            System.err.println("Erro ao salvar os dados na planilha: " + e.getMessage());
        }
    }

    public static void medirDesempenho(String arquivo) {
        List<Integer> lista = ler(arquivo);

        System.gc();
        Runtime runtime = Runtime.getRuntime();
        long memoriaAntes = runtime.totalMemory() - runtime.freeMemory();

        long inicioTempo = System.nanoTime();
        // String metodo = "bubbleSort";
        // bubbleSort.ordenar(lista);
        String metodo = "mergeSort";
        mergeSort.ordenar(lista);
        long fimTempo = System.nanoTime();

        long memoriaDepois = runtime.totalMemory() - runtime.freeMemory();
        double tempoMs = (fimTempo - inicioTempo) / 1_000_000.0;
        long memoriaKb = (memoriaDepois - memoriaAntes) / 1024;

        System.out.println("Tempo de execução: " + tempoMs + " ms");
        System.out.println("Consumo de memória: " + memoriaKb + " KB");

        // salvarListaEmArquivo(lista, "arq_saida.txt");
        salvarDadosEmPlanilha(tempoMs, memoriaKb,metodo, "resultadosJavaVM.csv");
    }

    public static void main(String[] args) {
        String arquivo = "ordenacao/arq-desafio.txt";

        for (int i = 0; i < 10; i++) {
            medirDesempenho(arquivo);
            System.out.println("Execução " + (i + 1) + " concluída!");
        }
    }
}