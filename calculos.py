from random import randint 

historico = [] # relatório


# Configurações 

def sys_cfg():
    print("\n--- Configuração do Sistema ---")

    try:

        voltagem = float(input("Digite a voltagem do sistema (V): "))
        fases = int(input("Digite o número de fases: "))
        frequencia = float(input("Digite a frequência (Hz): "))

        print("\nSistema configurado com sucesso!")

    except:

        print("\nErro! Entrada inválida.")



#  Simulação do Campo eletrostático

def simular_campo():
    try:
        intensidade = (voltagem * fases) / frequencia
        print("\n--- Simulação do Campo eletrostático ---")
        
        print(f'Voltagem: {voltagem}V')
        print(f'Fases: {fases}')
        print(f'Frequência: {frequencia} Hz')
        print(f'Intensidade estimada do campo: {intensidade:.2f}')

        # adicionar condição de moderagem
    except:
        print("\nErro! Faça a configuração do sistema.")



# Calcular Repulsão das Partículas

def calcular_repulsao():

    print("\n--- Cálculo de repulsão das partículas ---")

    try:
        q1 = float(input("Carga da partícula 1: "))
        q2 = float(input("Carga da partícula 2: "))
        r = float(input("Distância entre partículas (m): "))
        k = 9*10**9 # constante

        forca = k * abs(q1 * q2) / r**2

        print(f'\nForça de repulsão: {forca:.2f} N')
        
        # adicionar condição de moderagem

    except:
        print("Valores Inválidos.")



# Simulação de poeira

def simular_poeira():

    print("\n--- Simulação de acúmulo de poeira ---")

    tempo_sim = int(input("Tempo de Simulação (segs): "))

    eficiencia = 100

    for segundo in range(1, tempo_sim + 1):
        aumento_particulas += randint(10, 30)
        aumento_temp += randint(1, 4)

        particulas += aumento_particulas
        temperatura += aumento_temp

        eficiencia -= (particulas * 0.002)
        eficiencia -= (temperatura * 0.001)

        if eficiencia < 0:
            eficiencia = 0
        
        if temperatura >= 80 or particulas >= 800:
            risco = "Crítico"
        elif temperatura >= 60 or particulas >= 500:
            risco = "Moderado"
        else:
            risco = "Baixo"
        
        print(f'Tempo: {segundo}s')
        print(f'Temperatura: {temperatura}°C')
        print(f'Partículas: {particulas}ppm')
        print(f'Eficiência ADS: {eficiencia}%')
        print(f'Risco do sistema: {risco}')

        historico.append({
            "Tempo": tempo_sim,
            "Temperatura": temperatura,
            "Partículas": particulas,
            "Eficiência ADS": eficiencia,
            "Risco do sistema": risco
            })
    print("Simulação Finalizada.")




# Relatório

def relatorio():
    print("\n--- Relatório de Eficiência ---")

    if len(historico) == 0:
        print("Nenhuma simulação encontrada")
        return
    
    print(f"""
-------------------------
Relatório do sistema:
      
Temperatura: {historico[-1]['Temperatura']}°C
Partículas: {historico[-1]['Partículas']} ppm
Eficiência: {historico[-1]['Eficiência ADS']}%
Risco: {historico[-1]['Risco do sistema']}          
-------------------------          
""")