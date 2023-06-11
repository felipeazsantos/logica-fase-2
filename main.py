import string


def __main__():
    filteredValues = archiveFilteredValues()

    # Pergunta ao usuário quais dados ele deseja ver
    print()
    option = choiceShowOption()

    # Coloca o cabeçalho da lista filtrada
    print()
    showHeader(option)

    # Mostra os dados de acordo com periodo e opção escolhida pelo usuário
    for line in filteredValues:
        showData(option, line)


def userInput():
    initialMonth = input("Digite o mês inicial (1 a 12) que deseja visualizar os dados meteorológicos: ")
    while not monthValidate(initialMonth):
        initialMonth = input("Digite o mês inicial (1 a 12) que deseja visualizar os dados meteorológicos: ")

    initialYear = input("Digite o ano inicial (a partir de 1961) que deseja visualizar os dados meteorológicos: ")
    while not yearValidate(initialYear):
        initialYear = input("Digite o ano inicial (a partir de 1961) que deseja visualizar os dados meteorológicos: ")

    finalMonth = input("Digite o mês final (1 a 12) que deseja visualizar os dados meteorológicos: ")
    while not monthValidate(finalMonth):
        finalMonth = input("Digite o mês final (1 a 12) que deseja visualizar os dados meteorológicos: ")

    finalYear = input("Digite o ano final (até de 2016) que deseja visualizar os dados meteorológicos: ")
    while not yearValidate(finalYear) and not validateInitialYearAndFinalYear(initialYear, finalYear):
        finalYear = input("Digite o ano final (até de 2016) que deseja visualizar os dados meteorológicos: ")

    return int(initialMonth), int(initialYear), int(finalMonth), int(finalYear)


def monthValidate(monthValue):
    validValue = isNumber(monthValue)
    if not validValue:
        return False

    monthCheck = int(monthValue)
    if monthCheck >= 1 and monthCheck <= 12:
        return True
    else:
        return False

def yearValidate(yearValue):
    validValue = isNumber(yearValue)
    if not validValue:
        return False

    yearCheck = int(yearValue)
    if yearCheck >= 1961 and yearCheck <= 2016:
        return True
    else:
        return False

def validateInitialYearAndFinalYear(initialYear, finalYear):
    return initialYear < finalYear


def isNumber(valueCheck):
    for value in valueCheck:
        if value not in string.digits:
            return False

    return True


def archiveFilteredValues():
    # Pergunta ao usuário o período que deseja visualizar os dados
    initialMonth, initialYear, finalMonth, finalYear = userInput()

    archive = open("OK_Anexo_Arquivo_Dados_Projeto.csv", "r")
    firstLine = True
    filteredValues = []
    for line in archive:
        if firstLine:
            firstLine = False
            continue

        lineValue = line[:-1].split(";")
        date = lineValue[0]
        month = int(date[3:5])
        year = int(date[6:])
        archiveYearMonth = int(str(year) + str(month))
        initialUserYearMonth = int(str(initialYear) + str(initialMonth))
        finalUserYearMonth = int(str(finalYear) + str(finalMonth))

        # Se estiver no período que o usuário escolheu adiciona na lista dos dados filtrados
        if (archiveYearMonth >= initialUserYearMonth) and (archiveYearMonth <= finalUserYearMonth):
            filteredValues.append(lineValue)

    archive.close()
    return filteredValues


def showData(option, line):
    data = line[0]

    if float(line[1]) > 0:
        rainVolume = float(line[1])
    else:
        rainVolume = 0

    maxTemperature = float(line[2])
    minTemperature = float(line[3])
    airHumidity = float(line[6])
    windSpeed = float(line[7])

    match option:
        case 1:
            print(f"{data}         {rainVolume:.2f}               {maxTemperature:.2f}                {minTemperature:.2f}                {airHumidity:.2f}              {windSpeed:.2f}")
        case 2:
            print(f"{data}         {rainVolume:.2f}")
        case 3:
            print(f"{data}         {maxTemperature:.2f}                {minTemperature:.2f}")
        case 4:
            print(f"{data}         {airHumidity:.2f}              {windSpeed:.2f}")


def showHeader(option):
    match option:
        case 1:
            print("Data        | Volume de Chuva | Temperatura Máxima | Temperatura Mínima | Umidade do AR | Velocidade do Vento ")
        case 2:
            print("Data        | Volume de Chuva ")
        case 3:
            print("Data        | Temperatura Máxima | Temperatura Mínima ")
        case 4:
            print("Data        | Umidade do AR | Velocidade do Vento ")

def choiceShowOption():
    option = input("Escolha os dados que deseja visualizar:  \n"
                   " 1) todos os dados. \n" +
                   " 2) apenas os de precipitação. \n" +
                   " 3) apenas os de temperatura. \n" +
                   " 4) apenas os de umidade e vento para o período informado. \n")

    while not isNumber(option):
        option = input("Escolha os dados que deseja visualizar:  \n"
                       " 1) todos os dados. \n" +
                       " 2) apenas os de precipitação. \n" +
                       " 3) apenas os de temperatura. \n" +
                       " 4) apenas os de umidade e vento para o período informado. \n")

    option = int(option)

    while option < 1 or option > 4:
        option = input("Escolha os dados que deseja visualizar:  \n"
                       " 1) todos os dados. \n" +
                       " 2) apenas os de precipitação. \n" +
                       " 3) apenas os de temperatura. \n" +
                       " 4) apenas os de umidade e vento para o período informado. \n")

    return option

__main__()