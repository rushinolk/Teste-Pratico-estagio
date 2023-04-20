
distancia = 100
vel_carro = 110
vel_caminhao = 80

# Realizei o calculo da velocidade total dos venciculos para em seguida calcular o tempo que eles iram se encontrarem
vel_total = vel_carro + vel_caminhao
tempo = distancia / vel_total
print("Tempo para os veículos se encontrarem:", tempo, "horas")

#Transformei o tempo adicional dos pedagios de minutos para horas e em seguida calculei o tempo adicional 
tempo_pedagio = 5 / 60
tempo_adicional = tempo_pedagio * 2
print("Tempo adicional do caminhão:", tempo_adicional, "horas")


#O tempo que o caminhão vai levar pra chegar sera o tempo de encontro mais o tempo adicional
tempo_caminhao = tempo + tempo_adicional
print("Tempo total do caminhão:", tempo_caminhao, "horas")


#Calculo da distancia que cada veiculo percorreu
dist_carro = vel_carro * tempo
dist_caminhao = vel_caminhao * tempo_caminhao
print("Distância percorrida pelo carro:", dist_carro, "km")
print("Distância percorrida pelo caminhão:", dist_caminhao, "km")


#Basicamente realizei o calculo para saber o tempo adicional que o caminhão iria levar baseado no tempo que ele levaria para encontrar com o carro
#Em seguida fiz o calculo de quantos km cada veiculo fez vendo que o carro andou mais que o caminhao, logo o caminhão esta mais proximo 