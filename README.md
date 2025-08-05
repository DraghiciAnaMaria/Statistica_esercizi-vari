# Statistica_esercizi-vari

## 📘 Panoramica esercizi

Il repository contiene una raccolta di esercizi di statistica applicata e simulazione Monte Carlo, ognuno focalizzato su un problema probabilistico o numerico specifico.

---
##  🗳️ Esercizio 1 – Probabilità di vittoria in un ballottaggio
In un ballottaggio tra due candidati (A e B), si analizza la probabilità che il candidato A vinca, considerando:

- M elettori che supportano A

- N elettori indecisi che votano a caso

La probabilità di vittoria viene calcolata modellando i voti degli indecisi con una variabile aleatoria binomiale, e determinando la probabilità che A ottenga più della metà dei voti totali.

---

##  🎲 Esercizio 2 – Simulazione Monte Carlo di un gioco a dadi
Si studia un gioco da tavolo in cui pedine si muovono su colonne in base al lancio di due dadi.
L'obiettivo è stimare, tramite simulazione Monte Carlo:

- La probabilità di vittoria di ciascuna colonna

- La durata media del gioco

Viene anche evidenziato che la colonna 1 non può mai vincere, poiché la somma di due dadi (min. 2) non consente mai di muoverla.

---

##  🧮 Esercizio 3 – Integrazione Monte Carlo in più dimensioni
Si utilizza l’integrazione Monte Carlo per stimare volumi geometrici, in particolare:

- L’area del quarto di cerchio (stima di π)

- Il volume della sfera tridimensionale unitaria

- Il volume di un corpo tridimensionale definito da una disuguaglianza su x^2 + y^2 , dipendente da z

In ciascun caso si calcola il numero di campioni Monte Carlo 𝑁 necessario a garantire un errore assoluto < 0.01 con probabilità ≥ 95%, sfruttando la disuguaglianza di Chebyshev e il Teorema del Limite Centrale.
