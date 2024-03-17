from datetime import datetime
import os

pair_and_incidence = {}
ip_pair = []
max_tcp_size = 0
total_udp_payload_size = 0
total_udp_packets = 0
total_frag_pack = 0
ip_traffic = {}
higher_traffic_pair = None
higher_traffic = 0

file_name = input("Digite o nome do arquivo que deseja tratar; \nObs:incluir a extensão (ex: .dump): ")
str_path = os.path.abspath(__file__)
str_path = os.path.dirname(str_path)
dir = os.path.join(str_path, file_name)
try:
    fd = open(dir, "rb")
except :
    print("O arquivo especificado não foi encontrado.")
    exit()

header = fd.read(24)
magic_number = header[:4]

if magic_number == b'\xa1\xb2\xc3\xd4':
    endianess = 'big endian'
    endian = 'big'
elif magic_number == b'\xd4\xc3\xb2\xa1':
    endianess = 'little endian'
    endian = 'little'
else:
    endianess = 'desconhecido'
    exit()

recHeader = fd.read(16)
start_time = datetime.fromtimestamp(int.from_bytes(recHeader[0:4], endian))
while len(recHeader) == 16:
    recLen =    int.from_bytes(recHeader[8:12], endian)
    total_len = int.from_bytes(recHeader[12:16], endian)
    if recLen != total_len:
        total_frag_pack +=1
    recTime = datetime.fromtimestamp(int.from_bytes(recHeader[0:4], endian))

    if endianess == 'desconhecido':
        print("Ordem dos bytes desconhecida.")
        break

    print(f'\n{recTime}')

    recPacket = fd.read(recLen)
    recHeader = fd.read(16)

    acess_layer = recPacket[:14]
    mac_origem = ':'.join(f'{x:02x}' for x in acess_layer[6:12])  # Formata como xx:xx:xx:xx:xx:xx
    mac_destino = ':'.join(f'{x:02x}' for x in acess_layer[0:6])
    print(f'Mac origem : {mac_origem}')
    print(f'Mac destino: {mac_destino}')
    type = ''.join(f'{x:02x}' for x in acess_layer[12:14])  # Extrai o tipo de protocolo encapsulado

    # Se o tipo do protocolo for IPv4
    if type == '0800':
        print("Protocolo: IPv4")
        network_layer = recPacket[14:34]

        version_and_length = network_layer[0]
        # Sepaira os bits da versão
        version = version_and_length >> 4
        print(f"Versão do IP: {version}")

        header_length = (version_and_length & 0b00001111) * 4  # Multiplica por 4 paira obter o tamanho real em bytes
        print(f"Tamanho do cabeçalho IP: {header_length} bytes")
        if header_length > 20:
            print(f'Há opções encapsuladas dentro do pacote')

        tos = int.from_bytes(network_layer[1:2], endian)  # [1:2] != [1] / o [1:2] Cria uma sequencia de bytes que a função int.from_bytes consegue tratar
        print(f"Tipo de Serviço (TOS): {tos}")

        total_length = int.from_bytes(network_layer[2:4], endian)  # Comprimento total do cabeçalho ip
        print(f"Comprimento Total: {total_length} bytes")

        identification = int.from_bytes(network_layer[4:6], endian)
        print(f'Identificador: {identification}')

        # Extrai o byte que contém as flags do cabeçalho IP
        flags_byte = network_layer[6]

        active_flags = []
        if flags_byte & 0b10000000:  # Como o campo "flag" usa somente os 3 primeiros bits do byte é preciso somente identificar se tem um "1" no bit referente a cada flag
            active_flags.append("Flag Reservada")
        if flags_byte & 0b01000000:
            active_flags.append("Don't Fragment")
        if flags_byte & 0b00100000:
            active_flags.append("More Fragments")
        if active_flags:
            print(f'Flag: {active_flags}')
        else:
            print('Flag: Sem flags')

        fragment_offset_bytes = network_layer[6:8]

        fragment_offset = int.from_bytes(fragment_offset_bytes, endian) & 0b0001111111111111
        print(f'Fragment Offset: {fragment_offset}')

        time_to_leave_bytes = network_layer[8:9] # TTL
        time_to_leave = int.from_bytes(time_to_leave_bytes, endian)
        print(f'TTL: {time_to_leave}')

        protocol_bytes = network_layer[9:10] # Protocolo da proxima camada
        protocol = hex(int.from_bytes(protocol_bytes, endian))
        print(f'Protocolo: {protocol}')

        header_checksum_bytes = network_layer[10:12] # FCS
        header_checksum = hex(int.from_bytes(header_checksum_bytes, endian))
        print(f'Header Checksum: {header_checksum}')

        # Extrai o endereço IP fonte e converte para o formato decimal
        ip_bytes = []
        for byte in network_layer[12:16]:
            text_byte = str(byte)
            ip_bytes.append(text_byte)
        source_address = '.'.join(ip_bytes)
        print(f"IP de origem: {source_address}")
        # *Fiz das duas formas pois estou me acostumando a forma abaixo

        # Extrai o endereço IP de destino e converte para formato decimal
        destination_address = '.'.join(str(byte) for byte in network_layer[16:20])
        print(f"IP de destino: {destination_address}")

        # Prepara os dados para a contagem de incidencia de ips 
        ip_sd = source_address, destination_address
        ip_pair.append(ip_sd)


        ip_traffic.setdefault((source_address, destination_address), 0)  # Define um valor padrão de 0 para o par de IPs se ainda nao tiver
        ip_traffic[(source_address, destination_address)] += total_len   # Adiciona o tamanho total do pacote ao tráfego entre os IPs

        if protocol == '0x6':  # Verifica se é um pacote TCP e pepara os dados para a contagem do maior TCP capturado
            tcp_header = recPacket[34:54]
            tcp_payload = recPacket[54:]
            tcp_size = len(tcp_payload)
            if tcp_size > max_tcp_size:
                max_tcp_size = tcp_size
        if protocol == '0x11': # Verifica se é um pacote UDP e pepara os dados para a contagem do tamanho do tráfego médio dos UDPs
            udp_header = recPacket[34:42]
            udp_payload = recPacket[42:]
            udp_payload_size = len(udp_payload)
            total_udp_payload_size += udp_payload_size
            total_udp_packets += 1

finish_time = recTime
print(f'\nInício da captura: {start_time} \nFim da captura: {finish_time}')

print(f'Tamanho do maior payload de TCP capturado: {max_tcp_size} bytes')

if total_udp_packets > 0: 
    averange_payload = total_udp_payload_size / total_udp_packets
print(f'Tamanho médio dos payloads UDP: {averange_payload:.3f}... bytes') 

if total_frag_pack != 0:
    print(f'Um total de {total_frag_pack} pacotes não foram capturados em sua totalidade')
else:
    print(f'Todos os pacotes foram capturados em sua totalidade')

for pair, actual_trafic in ip_traffic.items(): # Loop para calcular o par de IPs com maior tráfego entre eles
    if actual_trafic > higher_traffic:
        higher_traffic = actual_trafic
        higher_traffic_pair = pair
print(f"O par de IPs com maior tráfego entre eles é: {higher_traffic_pair}, com um total de {higher_traffic} bytes transferidos.")

for pair in ip_pair: # Loop para iterar sobre os pares da lista
    if pair in pair_and_incidence: # Se existir
        pair_and_incidence[pair] += 1
    else:
        # Se não existir no dicionário e verificação do par invertido
        inverted_pair = (pair[1], pair[0])
        if inverted_pair in pair_and_incidence:
            pair_and_incidence[inverted_pair] += 1
        else:
            pair_and_incidence[pair] = 1

# Encontrar o par com a maior incidência
max_ocurence_pair = max(pair_and_incidence, key=pair_and_incidence.get)
max_ocurence = pair_and_incidence[max_ocurence_pair]
print(f"Maior número de comunicações registado foi entre:, {max_ocurence_pair} com uma incidência de: {max_ocurence}")


fd.close()
