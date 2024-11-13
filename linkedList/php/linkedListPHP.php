<?php
include_once 'NodePHP.php';

class LinkedListPHP{

    public ?NodePHP $head;
    public int $lenth;

    public function __construct(){
        $this->head = null;
        $this->lenth = 0;
    }
    public function ler($filePath){
        try {
            $file = fopen($filePath, "r");
            if (!$file) {
                throw new Exception("Não foi possível abrir o arquivo.");
            }
            // Primeira linha
            $firstLine = trim(fgets($file));
            $firstLineSplit = explode(" ", $firstLine);
            foreach ($firstLineSplit as $index => $data) {
                $this->adicionar((int)$data, $index + 1);
            }

            // Segunda linha
            $secondLine = trim(fgets($file));
            $qtdAcoes = (int)$secondLine;

            // Executa as ações
            for ($i = 0; $i < $qtdAcoes; $i++) {
                $acao = trim(fgets($file));
                $acaoSplit = explode(" ", $acao);
                
                if ($acaoSplit[0] === "A") {
                    $this->adicionar((int)$acaoSplit[1], (int)$acaoSplit[2]);
                } elseif ($acaoSplit[0] === "R") {
                    $this->remover((int)$acaoSplit[1]);
                } elseif ($acaoSplit[0] === "P") {
                    $this->mostrar();
                }
            }

            fclose($file);
        } catch (Exception $e) {
            echo $e->getMessage() . PHP_EOL;
            echo "Arquivo não encontrado" . PHP_EOL;
        }
    }

    public function adicionar(int $data, int $position){
        $newNode = new NodePHP($data);
        if ($position == 1){
            // Adicionando no início
            $newNode->next =  $this->head;
            $this->head = $newNode;
            $this->lenth++;
        } elseif ($position > 1 && $position <= $this->lenth + 1){
            // Adicionando em qualquer outra posição
            $atual = $this->head;
            for ($i = 1; $i < $position - 1; $i++) {
                $atual = $atual->next;
            }
            $newNode->next = $atual->next;
            $atual->next = $newNode;
            $this->lenth++;
        } else{
            print_r("Posição inválida\n");
        }
    }

    public function remover(int $data){
        if ($this->head->data == $data){
            $this->head = $this->head->next;
            $this->lenth--;
        } else{
            $atual = $this->head;
            while ($atual->next != null){
                if ($atual->next->data == $data){
                    $atual->next = $atual->next->next;
                    $this->lenth--;
                    return;
                }
                $atual = $atual->next;
            }
            print_r("Elemento não encontrado\n");
        }
    }
    public function mostrar(){
        $atual = $this->head;
        $lista = New ArrayObject();

        while ($atual != null) {
            $lista->append($atual->data);
            $atual = $atual->next;
        }
        print_r($lista);
    }
}