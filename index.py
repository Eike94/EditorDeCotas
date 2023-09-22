import re

# Função para subtrair um valor de números nas linhas correspondentes aos padrões especificados
def subtrair_valor_arquivo(nome_arquivo_entrada, nome_arquivo_saida, valor_subtrair):
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada, open(nome_arquivo_saida, 'w') as arquivo_saida:
        for linha in arquivo_entrada:
            # Verifica se a linha corresponde a um dos padrões
            padroes = ["CT-", "CF-", "CF\P{\C2;PSC} \P", "CF\P", "{\C5;CF\P", "{\C5;CF \P", "CF \P", "CF"]
            if any(padrao in linha for padrao in padroes):
                partes = linha.split()
                nova_linha = ""
                for parte in partes:
                    if re.match(r'(.*\d+\.\d+.*)', parte):
                        # A parte contém números decimais com "." como separador decimal
                        numeros = re.findall(r'(\d+\.\d+)', parte)
                        for numero in numeros:
                            valor_numerico = float(numero)
                            novo_valor = valor_numerico - valor_subtrair
                            parte = parte.replace(numero, "{:.3f}".format(novo_valor).replace('.', ','))
                    elif re.match(r'(.*\d+,\d+.*)', parte):
                        # A parte contém números decimais com "," como separador decimal
                        numeros = re.findall(r'(\d+,\d+)', parte)
                        for numero in numeros:
                            valor_numerico = float(numero.replace(',', '.'))
                            novo_valor = valor_numerico - valor_subtrair
                            parte = parte.replace(numero, "{:.3f}".format(novo_valor).replace('.', ','))
                    nova_linha += parte + " "
                linha = nova_linha.strip() + '\n'
            arquivo_saida.write(linha)

# Nome do arquivo de entrada e saída
arquivo_entrada = "Cotas.txt"
arquivo_saida = "novo_Cotas.txt"

# Valor a ser subtraído
valor_subtrair = 3.324

# Chama a função para realizar a subtração e criar o novo arquivo
subtrair_valor_arquivo(arquivo_entrada, arquivo_saida, valor_subtrair)
