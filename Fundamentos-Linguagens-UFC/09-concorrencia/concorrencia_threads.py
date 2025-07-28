import threading
import time

def tarefa(nome, tempo):
    print(f"Iniciando {nome}...")
    time.sleep(tempo)
    print(f"{nome} finalizada após {tempo} segundos.")

# Criando duas threads
thread1 = threading.Thread(target=tarefa, args=("Tarefa 1", 2))
thread2 = threading.Thread(target=tarefa, args=("Tarefa 2", 3))

# Iniciando as threads
thread1.start()
thread2.start()

# Aguardando as threads terminarem
thread1.join()
thread2.join()

print("Todas as tarefas foram concluídas.")
