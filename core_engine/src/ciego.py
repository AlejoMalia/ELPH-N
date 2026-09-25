#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIEGO DE VERDAD (D-662) · el operador no puede saber si la tirada lleva defecto.

  ISO 13528 / NAS: 'ciego' = el examinador NO SABE que esta en una prueba, y el
  item es INDISTINGUIBLE de uno normal. Nuestro veredicto era ciego a la
  RESPUESTA, pero el operador sabia que era un test. Esto lo cierra. Coste: 0 EUR.

  Protocolo:
    1. sellar   -> se genera una semilla, se guarda su HASH y se destruye el log
    2. preparar -> por cada tirada, la semilla decide EN SECRETO si inyecta defecto
    3. el operador corre `maquina.py verificar` sin saber nada
    4. abrir    -> se revela la semilla, se comprueba el hash y se puntua
"""
import sys, json, hashlib, secrets, os
import numpy as np

REG = 'ciego_registro.json'

def sellar(n_tiradas, p_defecto=0.5):
    """Genera la semilla, publica su compromiso, y NO la escribe en claro."""
    semilla = secrets.token_hex(16)
    comp = hashlib.sha256(semilla.encode()).hexdigest()
    json.dump({'compromiso': comp, 'n_tiradas': n_tiradas, 'p_defecto': p_defecto,
               'veredictos': []}, open(REG, 'w'), indent=1)
    print(f"  sellado · compromiso **{comp[:32]}...**")
    print(f"  **la semilla se imprime UNA vez y no se guarda. Custodiala aparte:**")
    print(f"      {semilla}")
    print(f"  {n_tiradas} tiradas · p(defecto) = {p_defecto}")
    return semilla

def preparar(semilla, k, P, diam):
    """Decide en secreto si la tirada k lleva defecto, y cual. El operador NO llama a esto."""
    h = hashlib.sha256(f"{semilla}:{k}".encode()).digest()
    r = np.random.default_rng(int.from_bytes(h[:8], 'big'))
    reg = json.load(open(REG))
    if r.random() >= reg['p_defecto']:
        return P.copy(), diam.copy(), 'limpia'
    modo = r.choice(['permutar', 'desplazar', 'sustraer'])
    Q, D = P.copy(), diam.copy()
    if modo == 'permutar':
        i, j = r.choice(len(D), 2, replace=False); D[i], D[j] = D[j], D[i]
    elif modo == 'desplazar':
        Q[r.integers(len(Q))] += r.normal(0, 1.0, Q.shape[1])
    else:
        m = r.integers(len(Q)); Q = np.delete(Q, m, 0); D = np.delete(D, m)
    return Q, D, modo

def anotar(k, veredicto):
    """El operador anota su veredicto SIN saber la verdad."""
    reg = json.load(open(REG))
    reg['veredictos'].append({'tirada': k, 'veredicto': veredicto})
    json.dump(reg, open(REG, 'w'), indent=1)
    print(f"  tirada {k} anotada: **{veredicto}**  (la verdad sigue sellada)")

def abrir(semilla):
    """Revela, comprueba el compromiso y puntua."""
    reg = json.load(open(REG))
    if hashlib.sha256(semilla.encode()).hexdigest() != reg['compromiso']:
        print("  **EL COMPROMISO NO CUADRA. La semilla no es la sellada.**"); return
    print(f"  compromiso verificado.\n")
    ok = 0; vp=fp=vn=fn=0
    for v in reg['veredictos']:
        k = v['tirada']
        h = hashlib.sha256(f"{semilla}:{k}".encode()).digest()
        r = np.random.default_rng(int.from_bytes(h[:8], 'big'))
        limpia = r.random() >= reg['p_defecto']
        dijo_pasa = (v['veredicto'] == 'pasa')
        acierto = (limpia == dijo_pasa); ok += acierto
        if limpia and dijo_pasa: vn+=1
        elif limpia and not dijo_pasa: fp+=1
        elif not limpia and not dijo_pasa: vp+=1
        else: fn+=1
        print(f"  tirada {k:>2}: verdad **{'limpia' if limpia else 'CON DEFECTO'}**"
              f"   dijo **{v['veredicto']}**   {'ok' if acierto else '**FALLO**'}")
    n = len(reg['veredictos'])
    if n:
        print(f"\n  aciertos **{ok}/{n}** = {100*ok/n:.0f} %")
        print(f"  defecto detectado {vp} · defecto NO detectado (riesgo del consumidor) **{fn}**")
        print(f"  limpia aprobada {vn} · limpia rechazada (riesgo del productor) **{fp}**")

if __name__ == '__main__':
    if len(sys.argv) < 2: print(__doc__)
    elif sys.argv[1] == 'sellar': sellar(int(sys.argv[2]) if len(sys.argv)>2 else 8)
    elif sys.argv[1] == 'anotar': anotar(int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == 'abrir': abrir(sys.argv[2])
    else: print(__doc__)
