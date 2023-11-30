lista = []

with open('apache.logs.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        partes = linha.split()

        contagem_ip = partes[0]
        if contagem_ip not in lista:
            lista.append(contagem_ip)
        print (partes)



# Criar um dicionário onde as chaves são os endereços IP únicos
dicionario = {ip: None for ip in lista}

# Imprimir o dicionário final


       
       
       


























#endereco_ip = partes[0]
#identd = partes[1]
#user = partes[2]
#data_e_hora = partes[3] + '  ' + partes[4] 
#http = partes[5] + '  ' + partes[6] + '  ' + partes[7]
#codigo_status_http = partes[8]
#tamanho_do_objeto = partes[9]
        
   
    