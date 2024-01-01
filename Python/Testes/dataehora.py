from datetime import datetime, date, time, timedelta

data_hora = datetime.now()


# hoje = date.today().strftime('%d/%m/%Y')
# agora = datetime.now().strftime('%d/%m/%Y %H:%M')
# print(f'Dia de hoje: {hoje}')
# print(f'Data e hora atuais: {agora}')
print(data_hora.strftime('%A, %H:%M'))
