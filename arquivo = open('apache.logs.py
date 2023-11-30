with open('apache.logs.txt', 'r') as arquivo:
   for k in arquivo:
       k = k.strip()
       
       partes = k.split()
       

       endereco_ip = partes[0]
       tamanho_resposta = partes[6]
       print (tamanho_resposta)
       