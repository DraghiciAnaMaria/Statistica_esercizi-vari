import numpy as np
import matplotlib.pyplot as plt
from math import lgamma
import os

def log_binomial(N, k):
    """Calcola log(C(N, k)) usando log-gamma per evitare overflow."""
    return lgamma(N + 1) - lgamma(k + 1) - lgamma(N - k + 1)

def logsumexp(log_values):
    """Calcola log(sum(exp(log_values))) in modo numericamente stabile."""
    a = max(log_values)
    return a + np.log(np.sum(np.exp(np.array(log_values) - a)))

def probabilita_vittoria(N_total=10**6, M_values=range(0, 5001, 10)):
    risultati = {}
    log2 = np.log(2)  # Usa np.log per coerenza con altre operazioni su array
    log_binoms = {}
    
    for M in M_values:
        N = N_total - M
        k_min = (N - M) // 2 + 1
        
        # Calcola tutti i log binomiali necessari per questo M
        log_p = log_binomial(N, k_min)
        log_probs = [log_p - N * log2]
        
        # Calcola ricorsivamente i successivi termini
        for i in range(k_min + 1, N + 1):
            log_p += np.log(N - (i - 1)) - np.log(i)
            log_probs.append(log_p - N * log2)
        
        # Calcola la probabilità totale
        log_P = logsumexp(log_probs)
        risultati[M] = np.exp(log_P)
    
    return risultati

# Ottimizzazione: si potrebbe usare meno punti per M_values 
M_values = range(0, 5001, 10)  
probabilità = probabilita_vittoria(M_values=M_values)

# Plot
plt.figure(figsize=(12, 7))
plt.plot(M_values, [probabilità[M] for M in M_values], 
         color='#E63946', linewidth=3, label="Probabilità di vittoria di A")

plt.xlabel("Numero di voti sicuri per A (M)", fontsize=12, fontweight='bold')
plt.ylabel("Probabilità di vittoria", fontsize=12, fontweight='bold')
plt.title("Probabilità di vittoria del candidato A\n(N + M = 1.000.000, M ∈ [0,5000])", 
          fontsize=14, pad=20, fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(0, 5001, 500), fontsize=10)
plt.yticks(np.arange(0.5, 1.01, 0.1), fontsize=10)
plt.ylim(0.45, 1.02)
plt.axhline(y=0.5, color='#457B9D', linestyle=':', linewidth=1.5)
plt.legend(loc='lower right', fontsize=12)
plt.text(3000, 0.6, "Transizione rapida:\nM > 1500 → Prob ≈ 1", fontsize=11, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig(os.path.expanduser("~/Desktop/probabilita_vittoria.pdf"), dpi=300)
plt.show()