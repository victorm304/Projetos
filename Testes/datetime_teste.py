from datetime import timedelta, datetime, timezone

# Deslocamento em segundos
offset_seconds = -10800

# Criando um objeto timedelta com o deslocamento
offset = timedelta(seconds=offset_seconds)

# Criando um objeto de fuso horário a partir do deslocamento
custom_timezone = timezone(offset)

# Obtendo o nome do fuso horário
timezone_name = datetime.now(custom_timezone).strftime('%z')

print(f"Fuso horário: {timezone_name}")
