import datetime
 

def valida_data_iso8601_estendido(date):

    try:

        datetime.datetime.strptime(date, '%Y-%m-%d')

        return True

    except ValueError:

        print("\nFormato de data incorreta, o formato correto é YYYY-MM-DD")

        return False

 

def valida_data_iso8601_basico(date):

    try:

        datetime.datetime.strptime(date, '%Y%m%d')

        return True

    except ValueError:

        print("\nFormato de data incorreta, o formato correto é YYYYMMDD")

        return False

 

def valida_data_BR(date):

    try:

        datetime.datetime.strptime(date, '%d/%m/%Y')

        return True

    except ValueError:

        print("\nFormato de data incorreta, o formato correto é DD/MM/YYYY")

        return False

 

def valida_data_BR_short(date):

    try:

        datetime.datetime.strptime(date, '%d/%m/%y')

        return True

    except ValueError:

        print("\nFormato de data incorreta, o formato correto é DD/MM/YYYY")

        return False

 

def date_BR_to_iso_estendido(date):

    teste = valida_data_BR(date)

 

    if teste:

        data_iso_estendido = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')

        print(data_iso_estendido)

    else:

        print("Rever parâmetros")

 

def date_BR_to_iso_basico(date):

    teste = valida_data_BR(date)

 

    if teste:

        data_iso_estendido = datetime.datetime.strptime(date, '%d/%m/%Y').strftime('%Y%m%d')

        print(data_iso_estendido)

    else:

        print("Rever parâmetros")

 

def valida_string(variavel):

    if isinstance(variavel, str):

        return True

    else:

        print('\nCotação está no formato errado. Deve ser passado uma string. Ex: "5,24"\n')

        return False