import numpy as np
import matplotlib.pyplot as plt

# Valori fissati di N per ciascun caso, calcolati teoricamente nella relazione
N_pi = 9604
N_sfera = 61466
N_A = 98596
num_trials = 3  # numero realizzazioni indipendenti

def stima_pi(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    inside_circle = x**2 + y**2 <= 1
    return 4 * np.cumsum(inside_circle) / np.arange(1, N + 1)

def stima_volume_sfera(N):
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    z = np.random.uniform(-1, 1, N)
    inside_sphere = x**2 + y**2 + z**2 <= 1
    return 8 * np.cumsum(inside_sphere) / np.arange(1, N + 1)

def stima_volume_A(N):
    x = np.random.uniform(-2, 2, N)
    y = np.random.uniform(-2, 2, N)
    z = np.random.uniform(-2, 2, N)
    inside_body = x**2 + y**2 <= 1 + np.sin(np.pi * z)
    volume_box = 64  # volume di [-2,2]^3
    return volume_box * np.cumsum(inside_body) / np.arange(1, N + 1)

# Funzione per grafico con valore atteso
def plot_stime(stima_fun, N, titolo, filename, valore_atteso=None):
    plt.figure(figsize=(10, 6))
    for i in range(num_trials):
        stime = stima_fun(N)
        plt.plot(range(1, N + 1), stime, label=f'Serie {i+1}', alpha=0.7)
    if valore_atteso is not None:
        plt.axhline(y=valore_atteso, color='red', linestyle='--', label='Valore atteso')
    plt.xlabel('Numero di campioni')
    plt.ylabel('Stima Monte Carlo')
    plt.title(titolo)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

# Generazione grafici
plot_stime(stima_pi, N_pi, "Stima di π con Monte Carlo", "stima_pi.pdf", np.pi)
plot_stime(stima_volume_sfera, N_sfera, "Volume della sfera unitaria", "volume_sfera.pdf", 4/3 * np.pi)
plot_stime(stima_volume_A, N_A, "Volume del corpo A", "volume_A.pdf", None)