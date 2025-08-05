import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# Parametri del problema
Voti_totali = 10**6
M_valori = np.arange(0, 5001, 10)    #Crea un array NumPy con valori interi che partono da 0, arrivano fino a 5000, con un passo di 10.
probabilità = []

# Calcolo delle probabilità
for M in M_valori:   #calcola al variare di M
    N = Voti_totali - M   #ricalcola N indecisi
    k = (N - M) // 2 + 1   #calcola la soglia di vittoria
    prob = 1 - binom.cdf(k - 1, N, 0.5)  #probabilità di A ddi vincere
    probabilità.append(prob)   #salva la probabilità per quel M


# Plot per rappresentare il grafico della funzione
plt.figure(figsize=(12, 7))
# Linea principale 
plt.plot(M_valori, probabilità, 
         color='#E63946', 
         linewidth=3, 
         label="Probabilità di vittoria di A",
         zorder=3)
# Personalizzazione assi e griglia
plt.xlabel("Numero di voti sicuri per A (M)", fontsize=12, fontweight='bold')
plt.ylabel("Probabilità di vittoria", fontsize=12, fontweight='bold')
plt.title("Probabilità di vittoria del candidato A\n(N + M = 1.000.000, M ∈ [0,5000])", 
          fontsize=14, pad=20, fontweight='bold')

# Griglia 
plt.grid(True, linestyle='--', alpha=0.7, zorder=1)

#  limiti assi
plt.xticks(np.arange(0, 5001, 500), fontsize=10)
plt.yticks(np.arange(0.5, 1.01, 0.1), fontsize=10)
plt.ylim(0.45, 1.02)

# Linea orizzontale a 0.5 per riferimento
plt.axhline(y=0.5, color='#457B9D', linestyle=':', linewidth=1.5, zorder=2)

# Legenda con stile
plt.legend(loc='lower right', fontsize=12, framealpha=1)

# Aggiunta testo esplicativo
plt.text(3000, 0.6, 
         "Transizione rapida:\nM > 1500 → Prob ≈ 1", 
         fontsize=11, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()

# Salvataggio in PDF 
desktop_path = os.path.expanduser("~/Desktop/probabilita_vittoria.pdf")
plt.savefig(desktop_path, dpi=300, bbox_inches='tight')
plt.show()