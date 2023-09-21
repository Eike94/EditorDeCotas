import re

# Função para subtrair um valor de números nas linhas correspondentes aos padrões especificados
def subtrair_valor_arquivo(nome_arquivo_entrada, nome_arquivo_saida, valor_subtrair):
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada, open(nome_arquivo_saida, 'w') as arquivo_saida:
        for linha in arquivo_entrada:
            # Verifica se a linha corresponde a um dos padrões
            padroes = ["CT-", "CF-", "CF\P{\C2;PSC} \P", "CF\P", "{\C5;CF\P"]
            if any(padrao in linha for padrao in padroes):
                # Divide a linha em partes usando espaços como separadores
                partes = linha.split()
                for i in range(len(partes)):
                    # Tenta encontrar números nas partes
                    numeros = re.findall(r'\d+\,\d+', partes[i])
                    for numero in numeros:
                        # Tenta converter o número e subtrair o valor
                        try:
                            valor_numerico = float(numero.replace(',', '.'))
                            novo_valor = valor_numerico - valor_subtrair
                            partes[i] = partes[i].replace(numero, "{:.2f}".format(novo_valor).replace('.', ','))
                        except ValueError:
                            pass  # Ignora partes que não podem ser convertidas em número
                # Recria a linha com as partes atualizadas
                linha = ' '.join(partes) + '\n'
            # Escreve a linha no arquivo de saída
            arquivo_saida.write(linha)

# Nome do arquivo de entrada e saída
arquivo_entrada = "Cotas.txt"
arquivo_saida = "novo_Cotas.txt"

# Valor a ser subtraído
valor_subtrair = 3.324

# Chama a função para realizar a subtração e criar o novo arquivo
subtrair_valor_arquivo(arquivo_entrada, arquivo_saida, valor_subtrair)
