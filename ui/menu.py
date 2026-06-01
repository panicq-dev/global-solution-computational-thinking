from config.config import api_key, base_url # importar configuração 
from services.clima import coordenadas, previsao_tempo, estimativa_chuva # importar funções do clima
from services.limpeza import simular_limpeza, executar_limpeza, executar_limpeza_manual, registrar_limpeza # importar funções de limpeza
from services.limpeza import exibir_relatorio # importar função de relatório

def menu():

    cidade = None
    lat = None
    lon = None

    while True:
        print()
        print("---------------- ADS menu ----------------")
        print("1. Definir local e obter previsão do tempo")
        print("2. Estimativa de chuva (próximos 5 dias)")
        print("3. Simulador de limpeza")
        print("4. Limpar painel solar")
        print("5. Modo de limpeza")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            print("Definir local e obter previsão do tempo selecionado.")
            print(api_key)
            cidade = input("Digite o nome da cidade: ").strip()
            coordenadas_resultado = coordenadas(cidade, api_key, base_url)

            if coordenadas_resultado:
                lat, lon = coordenadas_resultado
                previsao = previsao_tempo(api_key, lat, lon)

                if previsao:
                    print("-" * 30)
                    print(f"Previsão do tempo para {cidade}:")
                    print(f"Temperatura: {previsao['main']['temp']}°C")
                    print(f"Condição: {previsao['weather'][0]['description']}")
                    print("-" * 30)
                
                    if "rain" in previsao or previsao["weather"][0]["main"].lower() == "rain":
                        print("Está chovendo. Não é recomendado limpar o painel solar.")
                    else:
                        print("Não está chovendo. É um bom momento para limpar o painel solar.")

                else:
                    print("Não foi possível obter a previsão do tempo.")

            else:
                print("Não foi possível obter as coordenadas da cidade.")

        elif opcao == "2":
                print("Estimativa de chuva selecionada.")

                if cidade is None: # Se o local não tiver sido definido, mostrar erro.
                    print("Por favor, defina o local primeiro (opção 1).")
                    continue

                coordenadas_resultado = coordenadas(cidade, api_key, base_url) 

                if coordenadas_resultado:
                    lat, lon = coordenadas_resultado
                    estimativa = estimativa_chuva(api_key, lat, lon)

                    if estimativa:
                        print(f"Estimativa de chuva dos próximos 5 dias em {cidade}:")

                        dia_visitados = set()

                        for item in estimativa["list"]:
                            data = item["dt_txt"].split(" ")[0] # Pegar a data

                            if data not in dia_visitados: # Verificar se a data já foi visitada
                                dia_visitados.add(data) # Adicionar a data aos visitados
                                descricao = item["weather"][0]["description"] # Pegar a descrição do tempo
                                probabilidade = item.get("pop", 0) # Probalidade de chuva (pop)

                                print("-" * 20)
                                print(f"Data: {data}")
                                print(f"Condição: {descricao.capitalize()}")
                                print(f"Probabilidade de chuva: {probabilidade * 100:.0f}%")
                                print("-" * 20)

                                if probabilidade > 0.3: # Se a probabilidade de chuva for maior que 30%, mostrar aviso.
                                    print("Aviso: Alta probabilidade de chuva. Considere adiar a limpeza do painel solar.")

                            if len(dia_visitados) >= 5: # Limitar a 5 dias
                                break

                    else:
                        print("Não foi possível obter a estimativa de chuva.")

                else:
                    print("Não foi possível obter as coordenadas da cidade.")

        elif opcao == "3":
            print("Simulador de limpeza selecionado.")
            print("Insira os valores para simular a limpeza do painel solar.")

            try:
                nivel_poeira = float(input("Nível de poeira (%): ").strip())
                if 0 <= nivel_poeira <= 100:
                    simular_limpeza(nivel_poeira)
                else:
                    print("Por favor, insira um valor entre 0 e 100.")

            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o nível de poeira.")
                continue

        elif opcao == "4":
            print("Limpar painel solar selecionado.")

            try:
                nivel_poeira = float(input("Nível de poeira (%): ").strip())
                if 0 <= nivel_poeira <= 100:
                    confirmacao = input("Deseja executar a limpeza automática? (s/n): ").strip().lower()

                    if confirmacao == "s":
                        executar_limpeza(nivel_poeira)
                    else:
                        print("Cancelando limpeza manual.")

                else:  
                    print("Por favor, insira um valor entre 0 e 100.")

            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o nível de poeira.")
                continue

        elif opcao == "5":
            exibir_relatorio()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
