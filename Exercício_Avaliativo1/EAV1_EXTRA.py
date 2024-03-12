import threading
import time
import random
from pymongo import MongoClient
import matplotlib.pyplot as plt

def conectar_mongoDB():
    client = MongoClient('localhost', 27017)
    db = client.bancoiot
    return db.sensores

def gerar_temperatura():
    return round(random.uniform(30, 40), 2)

def sensor_temperatura(nome_sensor, intervalo, db_collection, ultimas_leituras):
    while True:
        temperatura = gerar_temperatura()
        print(f'{nome_sensor} - Temperatura: {temperatura}')
        ultimas_leituras[nome_sensor].append(temperatura)
        if len(ultimas_leituras[nome_sensor]) > 12:  # Manter apenas as últimas 12 leituras (última hora)
            ultimas_leituras[nome_sensor].pop(0)
            
        documento = db_collection.find_one({'nome': nome_sensor})
        if documento:
            db_collection.update_one({'nome': nome_sensor}, {'$set': {'temperatura': temperatura}})
            if temperatura > 38:
                print(f'A temperatura do sensor {nome_sensor} está acima do limite!')
                db_collection.update_one({'nome': nome_sensor}, {'$set': {'sensorAlarmado': True}})
                break
        else:
            db_collection.insert_one({'nome': nome_sensor, 'temperatura': temperatura})
            if temperatura > 38:
                print(f'A temperatura do sensor {nome_sensor} está acima do limite!')
                db_collection.update_one({'nome': nome_sensor}, {'$set': {'sensorAlarmado': True}})
                break
        time.sleep(intervalo)

def plotar_grafico(ultimas_leituras):
    while True:
        plt.clf()  # Limpar o gráfico para atualização
        for sensor, leituras in ultimas_leituras.items():
            plt.plot(range(len(leituras)), leituras, label=sensor)
        plt.xlabel('Tempo (última hora)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Valores medidos pelos sensores na última hora')
        plt.legend()
        plt.grid(True)
        plt.pause(60)  # Atualizar o gráfico a cada minuto

def iniciar():
    db_collection = conectar_mongoDB()
    ultimas_leituras = {sensor: [] for sensor in ['sensor1', 'sensor2', 'sensor3']}
    sensores = ['sensor1', 'sensor2', 'sensor3']
    intervalo = 5
    threads = []
    
    for sensor in sensores:
        t = threading.Thread(target=sensor_temperatura, args=(sensor, intervalo, db_collection, ultimas_leituras))
        t.start()
        threads.append(t)
    
    t_plot = threading.Thread(target=plotar_grafico, args=(ultimas_leituras,))
    t_plot.start()
    threads.append(t_plot)
    
    for t in threads:
        t.join()
        
if __name__ == '__main__':
    iniciar()
