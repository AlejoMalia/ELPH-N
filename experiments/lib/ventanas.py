"""D-674 · Las once ventanas, DERIVADAS. Coste 0 (TRIADA).

  Toda cota lleva su ventana (regla 594). Una ventana tiene DOS limites:

    POR RUIDO           N >= 9 (sigma/tol)^2        promediar baja el ruido como 1/raiz(N)
    POR ENMASCARAMIENTO N <= 1/beta                 un estimador de punto de ruptura beta
                                                    NO VE un defecto en menos de beta*N muestras

  **La ventana la fija el PUNTO DE RUPTURA.** Y existe solo si N_ruido <= N_masc.
"""
import math
# (criterio, sigma, tolerancia, beta del estimador, n unidades, cadencia)
C = [
 ("Om disposicion",          0.141, 0.423, 0.50,  50, "por re-colocacion"),
 ("inventario p98",          0.141, 0.423, 0.02,  50, "por re-colocacion"),
 ("recuento nA==nB",         0.0,   1.0,   1/50., 50, "por acto"),
 ("identidad |dd|",          0.0005,0.061, 1/50., 50, "por acto"),
 ("contrato A>1",            0.141, 0.423, 0.50,  50, "por acto"),
 ("GATE-0 alpha>=0,95",      0.041, 0.05,  0.293,300, "por par · Theil-Sen (D-674)"),
 ("GATE-0 D(176)<=35 um",    7.2,   35.0,  0.293,300, "por par · Theil-Sen (D-674)"),
 ("K_DELTA=3 (suelo)",       0.141, 0.423, 0.50,  50, "por re-colocacion"),
 ("suelo deteccion 1,0 mm",  0.141, 1.0,   0.02,  50, "por re-colocacion"),
 ("choque (pico,dur,onset)", 0.1,   1.0,   0.02,  1,  "a >=2000 muestras/s (ISTA)"),
 ("ppCO2 <= 3 mmHg",         0.3,   3.0,   0.50,  1,  "continuo · media 1 h (OCHMO)"),
 ("O2 <= 23,5 % (FUEGO)",    0.2,   2.0,   1.0,   1,  "continuo · INSTANTANEO (NFPA 99)"),
 ("diluvio en <= 3 s",       0.0,   3.0,   1.0,   1,  "instantaneo (NFPA 99 Class A)"),
]
print(f"  {'criterio':<26}{'N ruido':>9}{'N masc.':>9}{'VENTANA':>12}   {'cadencia'}")
print(f"  {'-'*78}")
huecos=[]
for nom,sig,tol,beta,n,cad in C:
    Nr = max(1, math.ceil(9*(sig/tol)**2))
    Nm = math.floor(1/beta)
    ok = Nr <= Nm
    v = f"{Nr}-{Nm}" if ok else "**NO EXISTE**"
    if not ok: huecos.append((nom,Nr,Nm))
    print(f"  {nom:<26}{Nr:>9}{Nm:>9}{v:>12}   {cad}")
print(f"\n  N_SUELO_MIN declarado = 10")
print(f"\n  PREDICCION 2 {'SE CUMPLE' if huecos else 'FALLA'}: {len(huecos)} criterio(s) sin ventana valida.")
for nom,Nr,Nm in huecos:
    print(f"    {nom}: el ruido pide {Nr} muestras y el enmascaramiento no deja pasar de {Nm}.")
print("\n  -> Donde N_ruido > N_masc la ventana NO EXISTE, y la salida es NO PROMEDIAR:")
print("     se exige que **TODAS** las repeticiones pasen, no que pase la media.")
print("     Asi el defecto presente en una sola no se diluye, y el ruido se controla")
print("     con la probabilidad conjunta. VENTANA = 1, REGLA = todas.")
