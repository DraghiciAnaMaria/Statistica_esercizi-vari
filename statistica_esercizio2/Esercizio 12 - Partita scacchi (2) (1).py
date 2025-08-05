import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# --- PARAMETRI DI SIMULAZIONE ---
NUM_SIMULAZIONI = 100000  # Numero totale di partite simulate
RIGA_VITTORIA = 19         # Altezza da raggiungere per vincere
COLONNE_TOTALI = 13        # Colonne numerate da 1 a 12 (la 0 e >12 non usate)

# --- CONTATORI PER RISULTATI ---
vittorie_col7_vs_col8 = 0  # Contatore vittorie colonna 7 contro colonna 8
vittorie_per_colonna = [0] * COLONNE_TOTALI  # Vittorie per ogni colonna
durata_partite = []        # Registra la durata di ogni partita

# --- SIMULAZIONE ---
pos_counter = [0]*COLONNE_TOTALI
for _ in range(NUM_SIMULAZIONI):
    posizioni = [0] * COLONNE_TOTALI
    turni = 0

    while all(riga < RIGA_VITTORIA for riga in posizioni):
        turni += 1
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        somma = dado1 + dado2

        if 2 <= somma <= 12:
            posizioni[somma] += 1
            pos_counter[somma] += 1

    durata_partite.append(turni)

    # Verifica se la colonna 7 ha vinto contro la 8
    if posizioni[7] >= RIGA_VITTORIA and posizioni[8] < RIGA_VITTORIA:
        vittorie_col7_vs_col8 += 1

    # Trova la prima colonna che ha vinto
    for colonna in range(2, 13):
        if posizioni[colonna] >= RIGA_VITTORIA:
            vittorie_per_colonna[colonna] += 1
            break
    print(
        f" esecuzione n {len(durata_partite)}, su {NUM_SIMULAZIONI} = {len(durata_partite)/NUM_SIMULAZIONI*100:.2f} %")

# --- CALCOLO DEI RISULTATI ---
prob_col7_vince = vittorie_col7_vs_col8 / NUM_SIMULAZIONI
prob_vittoria = [v / NUM_SIMULAZIONI for v in vittorie_per_colonna]

conteggio_durate = Counter(durata_partite)
prob_oltre_100 = sum(
    freq for t, freq in conteggio_durate.items() if t > 100) / NUM_SIMULAZIONI
prob_oltre_200 = sum(
    freq for t, freq in conteggio_durate.items() if t > 200) / NUM_SIMULAZIONI
durata_media = sum(durata_partite) / NUM_SIMULAZIONI

# --- STAMPA RISULTATI ---
print("\nRISULTATI DELLA SIMULAZIONE")
print("="*40)

print(
    f"\nProbabilità che la colonna 7 vinca contro la colonna 8: {prob_col7_vince:.2%}")

print("\nProbabilità di vittoria per colonna:")
print("Colonna | Probabilità")
print("--------|------------")
for colonna in range(0, 13):
    print(f"{colonna:7d} | {prob_vittoria[colonna]:.2%}")

print("\nStatistiche durata partite:")
print(f"- Probabilità >100 turni: {prob_oltre_100:.2%}")
print(f"- Probabilità >200 turni: {prob_oltre_200:.2%}")
print(f"- Durata media: {durata_media:.1f} turni")
print(f"Durata massima osservata: {max(durata_partite)}")
print(f"vittorie per colonna : {vittorie_per_colonna}")
print(f"contatore posizioni nel gioco gioco: {pos_counter}")
colonne = list(range(2, 13))  # solo le colonne da 2 a 12 sono valide
valore = [pos_counter[i] for i in colonne]

import matplotlib.pyplot as plt
from collections import Counter

# --- GRAFICO 1: Frequenza di selezione delle colonne ---
plt.figure(figsize=(10, 6))
plt.bar(colonne, valore, color='skyblue', edgecolor='black')
plt.title("Numero di volte che una colonna è stata scelta dai dadi")
plt.xlabel("Colonne (somma dei dadi)")
plt.ylabel("Totale numero di incrementi su tutte le simulazioni")
plt.xticks(colonne)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- GRAFICO 2: Probabilità di vittoria per colonna ---
plt.figure(figsize=(10, 6))
colonne_valide = range(2, 13)
prob_valide = [prob_vittoria[col] for col in colonne_valide]

plt.bar(colonne_valide, prob_valide, color='skyblue', edgecolor='black')
plt.title("Probabilità di vittoria per colonna")
plt.xlabel("Colonna (somma dei dadi)")
plt.ylabel("Probabilità di vittoria")
plt.xticks(colonne_valide)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- GRAFICO 3: Probabilità durata esatta N mosse ---
plt.figure(figsize=(12, 6))

# Calcola la probabilità per ogni N
max_N = 200
conteggio_durate = Counter(durata_partite)
total_partite = NUM_SIMULAZIONI
prob_N = [conteggio_durate.get(N, 0)/total_partite for N in range(1, max_N+1)]

plt.plot(range(1, max_N+1), prob_N, color='royalblue', linewidth=1.5)
plt.title("Probabilità che il gioco abbia durata esattamente N mosse")
plt.xlabel("Numero di mosse (N)")
plt.ylabel("Probabilità")
plt.xlim(1, max_N)
plt.grid(linestyle='--', alpha=0.5)
plt.show()