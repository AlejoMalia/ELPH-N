"""D-675 · Las seis capas son una RED. Quien alimenta a quien, y donde apalanca un calculo.

  Acoplamiento A[i][j] = cuantas condiciones de la capa j USAN algo de la capa i.
  DECLARADO por mi a partir de las dependencias reales de escala.py; se puede discutir
  celda a celda, que es justo lo que lo hace falsable.
"""
import numpy as np
CAPAS = ["1 marco","2 instrum","3 maquina","4 custodia","5 acto","6 humano"]
# filas = de, columnas = a
A = np.array([
 # 1  2  3  4  5  6
  [0, 5, 3, 2, 4, 2],   # 1 marco teorico -> el algebra, la ley A, n_min, g, phi, psi
  [0, 0, 4, 3, 5, 1],   # 2 instrumento   -> los 5 criterios, el suelo, delta, el ciego
  [0, 0, 0, 1, 4, 1],   # 3 maquina       -> GATE-0, lector, placa, paralaje
  [0, 0, 0, 0, 3, 3],   # 4 custodia      -> transporte, sello, choque, fuego
  [0, 0, 0, 0, 0, 0],   # 5 acto          -> SUMIDERO
  [0, 0, 0, 1, 0, 0],   # 6 humano        -> la envolvente restringe la custodia
])
if __name__ == "__main__":
    sal, ent = A.sum(1), A.sum(0)
    # apalancamiento: alcance transitivo (a quien llego, directa o indirectamente)
    R = (A > 0).astype(int); T = R.copy()
    for _ in range(6): T = ((T + T@R) > 0).astype(int)
    alc = T.sum(1)
    print(f"  {'capa':<12}{'salidas':>9}{'entradas':>10}{'alcance':>9}{'APALANCA':>11}   {'papel'}")
    print(f"  {'-'*74}")
    for i,c in enumerate(CAPAS):
        ap = sal[i]*(1+alc[i])
        papel = ("FUENTE" if ent[i]==0 else ("SUMIDERO PURO" if sal[i]==0 else "intermedia"))
        print(f"  {c:<12}{sal[i]:>9}{ent[i]:>10}{alc[i]:>9}{ap:>11}   {papel}")
    print()
    o = np.argsort(-np.array([sal[i]*(1+alc[i]) for i in range(6)]))
    print("  ORDEN DE ATAQUE (un calculo aqui vale por los de aguas abajo):")
    for k,i in enumerate(o,1): print(f"    {k}. {CAPAS[i]}")
    print(f"\n  ratio entradas/salidas (>1 = mas la usan de lo que ella aporta):")
    for i,c in enumerate(CAPAS):
        if sal[i]: print(f"    {c:<12}{ent[i]/sal[i]:>6.2f}")
