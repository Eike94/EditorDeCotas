# Projeto de Formatação de Números em Arquivo de Cotas

Este README fornece informações sobre um projeto que envolve a formatação de números em um arquivo de cotas. O projeto é realizado em Python e utiliza a função `round()` para arredondar os números para duas casas decimais antes de escrevê-los em um arquivo de saída. O objetivo principal é formatar os números que atendem a critérios específicos dentro do arquivo original "Cotas.txt".

# Funcionamento do Projeto

O projeto consiste em um script Python que realiza as seguintes etapas:

1. Abertura do arquivo de entrada: O script abre o arquivo "Cotas.txt" para leitura, lê todas as linhas e armazena essas linhas em uma lista chamada `linhas`.

2. Processamento das Linhas: O script percorre cada linha do arquivo de entrada e verifica se ela atende a determinados critérios. Em particular, ele procura por linhas que contenham "CT-" ou "CF-" seguido de um número maior que 1000. Se uma linha atender a esses critérios, ela será processada.

3. Formatação dos Números: Se uma linha atender aos critérios mencionados, o script identificará o número após o "CT-" ou "CF-", tentará subtrair 3.324 desse número e arredondará o resultado para duas casas decimais usando a função `round()`. O número formatado será então reescrito na linha.

4. Escrita das Linhas Modificadas: O script armazena todas as linhas modificadas em uma lista chamada `linhas_modificadas`.

5. Criação do Arquivo de Saída: O script cria um novo arquivo chamado "Cotas_modificado.txt" para armazenar as linhas modificadas.

6. Escrita das Linhas no Arquivo de Saída: As linhas modificadas são escritas no arquivo de saída "Cotas_modificado.txt".

7. Conclusão: O script exibe uma mensagem indicando que o arquivo foi modificado e salvo com sucesso.

# Executando o Projeto

Para executar este projeto, siga as etapas abaixo:

1. Certifique-se de que o arquivo "Cotas.txt" contendo os dados de cotas esteja na mesma pasta que o script Python.

2. Execute o script Python.

```bash
python nome_do_script.py
```

3. Após a execução, o arquivo formatado "Cotas_modificado.txt" será criado na mesma pasta.

# Requisitos

Este projeto requer que você tenha Python instalado em seu sistema.

# Observações

- Certifique-se de que o arquivo de entrada "Cotas.txt" siga o formato esperado para que o script funcione corretamente.

- Os números que atendem aos critérios mencionados serão arredondados para duas casas decimais no arquivo de saída.

- Se o arquivo de entrada for muito grande, o processo de formatação pode levar algum tempo.

- Este projeto é destinado a fins educacionais e pode ser personalizado de acordo com suas necessidades específicas. Certifique-se de entender como o código funciona antes de usá-lo em um ambiente de produção.
