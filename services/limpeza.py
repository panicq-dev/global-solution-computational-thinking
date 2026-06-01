import time
from datetime import datetime

historico_limpezas = [] # histórico de limpezas

def registrar_limpeza(tipo, nivel_poeira, eficiencia_recuperada): # registrar limpeza
    registro = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "nivel_poeira": nivel_poeira,
        "eficiencia_recuperada": eficiencia_recuperada
    }

    historico_limpezas.append(registro)

def simular_limpeza(nivel_poeira): # simulação
    # Com a analise dos sensores, o sistema determina se a limpeza é necessária.
    print("Simulando limpeza do painel solar...")
    print("Analizando paneis solares")
    print(f"Nível de poeira detectado: {nivel_poeira}%")

    if nivel_poeira < 20:
        print("Nível de poeira baixo. Limpeza manual recomendada.")
        print("O sistema aguarda acumulo de poeira para economizar energia.")
        return
    elif 40 <= nivel_poeira < 60:
        print("Nível de poeira moderado. Limpeza automática recomendada.")
    else:
        perda = nivel_poeira * 0.8 # perda de eficiência estimada
        print("Nível de poeira alto. Limpeza automática urgente recomendada.")
        print(f"Perda de eficiência estimada: {perda:.1f}%. Iniciando limpeza automática imediata.")
    
    executar_limpeza(nivel_poeira) # executar limpeza

def executar_limpeza(nivel_poeira): # limpeza automática

    print("Ativando campo eletrostático")
    time.sleep(1)
    print("Gerando vibrações ultrassônicas")
    time.sleep(1)
    eficiencia = nivel_poeira * 0.9 # eficiência recuperada estimada
    print(f"\nLimpeza concluída. Eficiência recuperada: {eficiencia:.1f}%")
    print("Desativando campo eletrostático e vibrações ultrassônicas")

    registrar_limpeza("Automática", nivel_poeira, eficiencia)
def executar_limpeza_manual(nivel_poeira): # limpeza manual

    print("Iniciando limpeza manual")
    print("Ativando campo eletrostático")
    time.sleep(1)
    print("Gerando vibrações ultrassônicas")
    time.sleep(1)
    eficiencia = nivel_poeira * 0.9 # eficiência recuperada estimada para limpeza manual
    print(f"\nLimpeza manual concluída. Eficiência recuperada: {eficiencia:.1f}%")
    print("Desativando campo eletrostático e vibrações ultrassônicas")

    registrar_limpeza("Manual", nivel_poeira, eficiencia)
def exibir_relatorio(): # relatório de limpezas manuais e automáticas

    if not historico_limpezas:
        print("Nenhuma limpeza registrada.")
        return
    
    total_limpezas = len(historico_limpezas)
    total_simulacoes = 0
    total_manuais = 0
    eficiencia_total = 0
    for c in historico_limpezas:
        if c["tipo"] == "Automática":
            total_simulacoes += 1
        
        if c["tipo"] == "Manual":
            total_manuais += 1
        
        eficiencia_total += c["eficiencia_recuperada"]
    eficiencia_media = eficiencia_total / total_limpezas

    # Cálculo da economia de energia e manutenção
    kwh_recuperados = eficiencia_total * 0.6 # kWh recuperados estimados, considerando que seja uma placa solar de 600W.
    economia_energia = kwh_recuperados * 0.75 # 0.75R$ por kWh
    # imaginando que uma casa possui pelo menos 4 placas solares, e que cada placa custaria entre 15-25 reais para limpeza.
    economia_manutencao = total_simulacoes * 80
    economia_total = economia_energia + economia_manutencao

    print("-" * 30)
    print("Relatório de Limpezas") # Limpezas
    print(f"\n Total de limpezas realizadas: {total_limpezas}")
    print(f" Limpezas automáticas: {total_simulacoes}")
    print(f" Limpezas manuais: {total_manuais}")

    # Eficiência recuperada
    print(f"\n Eficiência total recuperada: {eficiencia_total:.1f}%")
    print(f" Eficiência média por limpeza: {eficiencia_media:.1f}%")
    
    # Economia estimada
    print(f"\n Energia estimada recuperada: {kwh_recuperados:.1f} kWh")
    print(f" Economia estimada de energia: R${economia_energia:.2f}")
    print(f" Economia estimada de manutenção: R${economia_manutencao:.2f}")
    print("-" * 30)
    print(f"Economia total estimada: R${economia_total:.2f}")

    detalhamento = input("Deseja ver o detalhamento de cada limpeza? (s/n): ").strip().lower()
    
    if detalhamento == "s":
        i = 1
        for c in historico_limpezas:
            print(f"\nLimpeza {i}:")
            print(f" Data: {c['data']}")
            print(f" Tipo: {c['tipo']}")
            print(f" Nível de poeira: {c['nivel_poeira']}%")
            print(f" Eficiência recuperada: {c['eficiencia_recuperada']:.1f}%")
            i += 1
    print(f"\n{'-' * 83}")
    print(" Estimativas baseada em painel solar de 600W e custo de energia de R$0.75 por kWh.")
    print(" Limpeza manual estimada em R$20 por placa, considerando 4 placas solares por casa.")
    print("-" * 83)
    