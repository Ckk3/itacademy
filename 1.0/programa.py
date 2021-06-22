# @author Ana Carolina Sousa Dias
# date 13/06/2021

import csv
import sys
from math import radians, sin, cos, sqrt, asin


class Main:


# Init, construtor de classes
#   - Lê arquivo, removendo o cabeçalho (primeira linha)
#   - Define as opções do menu, e que a localização que o usuário vai inserir é um vetor
    def __init__(self):
        self.pontos_taxi = Main.lerArquivo()
        self.i_order = self.pontos_taxi.pop(0)
        self.options = [
            "Listar todos os pontos de táxi",
            "Informar minha localização",
            "Encontrar pontos próximos",
            "Buscar pontos por logradouro",
            "Fechar programa"
        ]
        self.u_loc = list()


# Ler arquivo
#   - Define que os pontos de táxi são uma lista
#   - Abre arquivo CSV e faz a devida "limpeza", delimitando com "enter" e ; (ponto-e-vírgula)
#   - Retorna a lista lida de pontos de táxi
    def lerArquivo():
        pontos_taxi = list()
        with open("pontos_taxi.csv", encoding="utf8") as file:
            read = csv.reader(file, delimiter="\n")
            quotes = '"'
            for row in read:
                pontos_taxi.append(row[0].replace(quotes, '').split(";"))
        return pontos_taxi


# Menu principal
#   - Imprime as opções do menu já definidas, pulando linha no final
#   - Validação da entrada do usuário
#   - Execução da funcionalidade (op-1 porque o vetor menuLista começa com o índice 0)
    def menu(self):
        print("=== MENU ===")
        ct = 1
        for i in self.options:
            print(f"{ct}. {i}")
            ct+=1
        print()

        while True:
            op = input("Escolha uma das opções: ")
            if op.isnumeric():
                op = int(op)
                if op in range(1,6):
                    break
            print("Opção inválida.")

        menuLista = [Main.listaTaxi, Main.salvaLoc, Main.encontraPonto, Main.procuraPonto, Main.quit_system]
        menuLista[op-1](self)


# 1. Listar todos os pontos de táxi
#   - Imprime tabela organizada dos pontos de táxi com as informações necessárias
#   - Pula linha
#   - Retorna ao menu
    def listaTaxi(self):
        print("Pontos de táxi: ")
        print("{:<10} {:<50} {:<15} {:<40} {:<10} {:<20} {:<20}".format("Código", "Nome", "Telefone", "Logradouro", "Número", "Latitude", "Longitude"))

        for row in self.pontos_taxi:
            lista = list()
            for i in row:
                if row.index(i) >= 1:
                    lista.append(i)
            print("{:<10} {:<50} {:<15} {:<40} {:<10} {:<20} {:<20}".format(*lista))
        print()
        Main.menu(self)


# 2. Informar minha localização (definir e salvar no programa coordenadas digitadas pelo usuário)
#   - Verificação da validade da localização
#   - Digitação da localização
#   - Substituição de vírgulas por pontos
#   - Validade das coordenadas digitadas (latitudes entre -90 e +90 e longitudes de -180 para +180)
#   - Retorna ao menu
    def salvaLoc(self):
        valido = True
        print()
        while valido:
            print("Informe sua localização: ")
            lat = input("Latitude: ")
            long = input("Longitude: ")
            try:
                lat = lat.replace(",", ".")
                long = long.replace(",", ".")
                lat = float(lat)
                long = float(long)
            except:
                print("\nFormato inválido")
            else:
                if lat >= -90.0 and lat <= 90.0 and long >= -180.0 and long <= 180.0:
                    self.u_loc = [lat, long]
                    print("Coordenadas armazenadas!")
                    valido = False
                else:
                    print("\nCoordenadas inválidas.")
        print()
        Main.menu(self)    


# 3. Encontra pontos próximos à localização definida
#   - Verifica se já foi cadastrada alguma localização -> se não, retorna ao menu principal para que isso seja feito
#   - Calcula a distância de cada ponto à coordenada informada, substituindo vírgulas por pontos no CSV
#   - Imprime os pontos mais próximos, identificando as 3 distâncias mais curtas
#   - Substitui a distância para não interferir nas próximas repetições
#   - Retorna ao menu
    def encontraPonto(self):
        print()
        try:
            u_lat = self.u_loc[0]
            u_lon = self.u_loc[1]
        except:
            print("Você ainda não definiu as coordenadas.\nVoltando ao menu principal...")
            Main.menu(self)
        else:
            distancesList = list()
            for ponto in self.pontos_taxi:
                distancesList.append(Main.haversine(u_lat, u_lon, float(ponto[6].replace(",", ".")), float(ponto[7].replace(",", "."))))
            
            print("Os pontos de táxi mais próximos são: ")
            print("{:<15} {:<10} {:<50} {:<15} {:<40} {:<10} {:<20} {:<20}".format("Distância","Código", "Nome", "Telefone", "Logradouro", "Número", "Latitude", "Longitude"))
            for _ in range(3): 
                menor = min(distancesList)
                i = distancesList.index(menor)
                measure = "km"
                if menor < 1.0:
                    menor *= 1000 
                    measure = "m"
                lista = list()
                for info in self.pontos_taxi[i]:
                    if self.pontos_taxi[i].index(info) > 0:
                        lista.append(info)
                print("{:<15} {:<10} {:<50} {:<15} {:<40} {:<10} {:<20} {:<20}".format(f"{round(menor, 2)}{measure}", *lista))
                distancesList[i] = sys.float_info.max # valor máximo de float, para que não confunda com os menores valores nas próximas iterações

        Main.menu(self)



# 4. Busca pontos por logradouro
#   - Foi encontrado (found)? False -> ainda não
#   - print() -> serve para pular linhas
#   - Coloca a busca em uppercase (maiúsculas) para 'bater' com o que está no CSV
#   - Se encontrado, found = true e uma lista é criada para armazenar os pontos, para posteriormente imprimi-los
#   - Se não, found continua false, e um aviso é dado. Retorna-se ao menu.
    def procuraPonto(self):
        found = False
        print()
        busca = input("Digite todo ou parte de um logradouro: ")
        print()

        for row in self.pontos_taxi:
            if busca.upper() in row[self.i_order.index("logradouro")].upper():
                print("{:<10} {:<50} {:<15} {:<40} {:<10} {:<20} {:<20}".format("Código", "Nome", "Telefone", "Logradouro", "Número", "Latitude", "Longitude")) if not found else ""
                found = True
                lista = list()
                for i in row:
                    if row.index(i) >= 1:
                        lista.append(i)
                print("{:<10} {:<50} {:<15} {:<40} {:<10} {:<20} {:<20}".format(*lista))
            
            if self.pontos_taxi.index(row) == len(self.pontos_taxi)-1:
                if not found:
                    print("Nenhum resultado encontrado")
        print()
        Main.menu(self) 


# 5. Fecha o programa
    def quit_system(self):
        print("Fechando programa...")


# Método estático: haversine -> fórmula de Haversine para distâncias triangulares em uma esfera. 
#   - Fornecido na documentação. Retorna o raio da Terra vezes a fórmula.
    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        R = 6372.8  
        dLat = radians(lat2 - lat1)
        dLon = radians(lon2 - lon1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
    
        a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
        c = 2 * asin(sqrt(a))
    
        return R * c

Main().menu()