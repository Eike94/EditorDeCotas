# Abrir o arquivo de entrada para leitura
with open('Cotas.txt', 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()

# Lista para armazenar as linhas modificadas
linhas_modificadas = []

# Variável para rastrear se estamos dentro de uma seção CT ou CF
esta_dentro_de_CT_CF = False

# Percorrer cada linha do arquivo
for linha in linhas:
    # Verificar se a linha contém "CT-" ou "CF-" seguido de um número maior que 1000
    if ("CT-" in linha or "CF-" in linha) and float(linha.split('-')[1].replace(',', '.')) > 1000:
        esta_dentro_de_CT_CF = True
        # Dividir a linha em partes usando '-' como separador
        partes = linha.split('-')
        if len(partes) >= 2:
            try:
                # Tentar subtrair o número por -3,324 e arredondar para 2 casas decimais
                numero = float(partes[1].replace(',', '.'))
                novo_numero = round(numero - 3.324, 2)
                # Reescrever a linha com o novo resultado
                linha = partes[0] + '-' + str(novo_numero) + '\n'
            except ValueError:
                pass
    elif esta_dentro_de_CT_CF:
        # Verificar se a linha contém apenas números
        if linha.strip().replace('.', '', 1).isdigit():
            esta_dentro_de_CT_CF = False
    # Adicionar a linha à lista de linhas modificadas
    linhas_modificadas.append(linha)

# Abrir o arquivo de saída para escrita
with open('Cotas_modificado.txt', 'w') as arquivo_saida:
    # Escrever as linhas modificadas no arquivo de saída
    arquivo_saida.writelines(linhas_modificadas)

print("Arquivo modificado e salvo como 'Cotas_modificado.txt'")
