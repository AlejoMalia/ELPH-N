"""D-675 · LA BATERIA · 100 calculos GENERADOS, no inventados.

  Seis familias x listas que ya existen, ordenadas por apalancamiento de red
  (red_capas.py):  capa 1 (96) > capa 2 (65) > capa 3 = capa 4 (24) > capa 6 (4) > capa 5 (0)
  Coste declarado por calculo:  0 = deriva/simula  ·  E = necesita banco  ·  P = necesita paper
"""
B = {
"A · SENSIBILIDAD  d(conclusion)/d(constante)": [
 (1,"K_d = 0,632 / 0,597: ¿que A da un K 10 % distinto?","0"),
 (1,"g = 3 + (3-dim): ¿y si el grupo de simetria se mide mal en 1?","0"),
 (1,"n_min = dn - d(d+1)/2: sensibilidad de A a n por debajo de 49","0"),
 (1,"phi: ¿que cambia en el contrato si una clase 2 se trata como 3?","0"),
 (1,"psi = gK^4/A^4: ¿a que A la exclusion deja de morder?","0"),
 (1,"exponente de la ley: ¿y si fuese a/sigma^0,4 en vez de ^0,5?","0"),
 (2,"K_DELTA = 3,0: barrido 1-6 y su efecto en el % de falsos vetos","0"),
 (2,"PCT_INV = 98: barrido 90-99,9 y el punto de ruptura resultante","0"),
 (2,"N_SUELO_MIN = 10: ¿desde cuantas re-colocaciones se estabiliza delta?","0"),
 (2,"N_IMP = 100.000: coste CPU frente a cota FAR afirmable","0"),
 (2,"tolerancia de identidad = media brecha minima: barrido","0"),
 (3,"L_CAM_MM = 1500: sensibilidad del paralaje a la distancia","0"),
 (3,"CAMPO_MM = 200 y R_BORDE = 88: ¿como escala alpha con el campo?","0"),
 (3,"N_FID = 9 y 25: ¿cuantos hacen falta de verdad?","0"),
 (3,"R0_MM = 176: ¿cambia el veredicto con otra referencia?","0"),
 (3,"D0_MAX = 35 um: barrido y su % de PASA","0"),
 (4,"sigma_colocacion = 141 um: sensibilidad del suelo de deteccion","0"),
 (4,"K de Archard 1e-4 a 1e-1: ¿aguanta la conclusion de desgaste?","0"),
 (6,"k de cascara 0,2-0,5: espesor minimo (YA HECHO en D-674)","0"),
 (6,"onset rate 500 G/s de Eiband: sensibilidad de la envolvente","0"),
],
"B · RUPTURA  ¿a que contaminacion cae cada estimador?": [
 (2,"mediana de Om: curva de deteccion frente a fraccion contaminada","0"),
 (2,"p98 del inventario: idem","0"),
 (2,"max de identidad: idem","0"),
 (2,"el ciego SHA-256: ¿resiste un operador que conoce p_defecto?","0"),
 (3,"Theil-Sen en alpha: ¿a que fraccion de pares malos cae? (predicho 29,3 %)","0"),
 (3,"la asignacion optima: ¿a que ruido empieza a emparejar mal?","0"),
 (3,"el ajuste de paralaje: ¿y si un diametro se lee mal?","0"),
 (4,"la bascula: ¿que masa sustituida no ve?","E"),
 (5,"el FAR: ¿como degrada con la multiplicidad efectiva medida?","E"),
 (6,"la identidad del ocupante: FRR del iris bajo estres/dilatacion","P"),
],
"C · TRIANGULACION  dos rutas al mismo numero": [
 (1,"K_d: derivado vs medido en 3 sustratos vs D-605","0"),
 (1,"n_min: Maxwell 1864 vs nuestro banco 2D/3D","0"),
 (1,"capacidad de identificacion: Ahlswede-Dueck vs nuestro FAR","0"),
 (2,"delta: 1/raiz(n) derivado vs dispersion medida del suelo","0"),
 (2,"puntos de ruptura: teoricos vs medidos en el banco","0"),
 (3,"sigma_lector: nuestro 0,52 um vs EURAMET 0,5 um vs M3'","0"),
 (3,"alpha: nucleo GP (D-668) vs ajuste directo (D-669)","0"),
 (3,"la altura de asiento: por diametro (D-663) vs 3-D de Gunther 2016","P"),
 (4,"109 g de Hertz (D-618) vs 45 g de Eiband: ¿misma curva?","0"),
 (4,"permeacion O2: x4 desde N2 vs tabla directa si aparece","P"),
 (5,"A: mediana vs minimo vs FAR observado (tres rutas)","0"),
 (5,"tolerancia de montaje: MAA +-0,1 mm vs wing-box 0,3/0,46 mm","P"),
 (6,"envolvente de presion: Armstrong vs OCHMO 34,5-103 kPa","0"),
 (6,"fallo de volumen cerrado: UHMS 113/135 vs 37 buzos sin muertes","0"),
],
"D · FRONTERA  ¿el umbral esta donde esta la transicion?": [
 (1,"A > 1: ¿es 1 la frontera o hay zona muerta?","0"),
 (1,"clase 2 vs 3: ¿donde esta el corte de phi?","0"),
 (2,"delta = K*disp*raiz(2): ¿es raiz(2) o es otra cosa?","0"),
 (2,"riesgo del consumidor: curva completa defecto vs P(detectar)","0"),
 (3,"alpha >= 0,95: curva PASA/INTERMEDIO/VETO continua","0"),
 (3,"alpha < 0,35 (el VETO): ¿donde esta de verdad el 98,7 %?","0"),
 (3,"D(176) <= 35 um: curva de discriminacion","0"),
 (4,"suelo de deteccion 1,0 mm al 90 %: curva completa","0"),
 (4,"choque: superficie (pico, duracion, onset) en 3D","0"),
 (4,"O2 <= 23,5 %: ¿por que 23,5 y no 21 o 25?","P"),
 (4,"diluvio <= 3 s: ¿de donde sale el 3?","P"),
 (6,"13,5 psi/min: ¿es lineal o hay codo?","P"),
 (6,"45 g a 44 ms: la curva de Eiband completa, digitalizada","P"),
 (6,"pared >= 4,0 mm acero: frontera exacta con k medido","P"),
 (6,"bulbo humedo 21,9-33,7 C: ¿que parte de la banda nos aplica?","0"),
],
"E · ACOPLAMIENTO  como se propaga capa i -> capa j": [
 (1,"1->2: un error en la ley A, ¿cuanto mueve los 5 criterios?","0"),
 (1,"1->3: n_min mal, ¿cuantos fiduciales de mas hacen falta?","0"),
 (1,"1->4: phi mal, ¿que criterio de custodia deja de aplicar?","0"),
 (1,"1->5: g mal, ¿cuanto se mueve A en el acto?","0"),
 (1,"1->6: clase 3 mal, ¿cambia la envolvente del ocupante?","0"),
 (2,"2->3: suelo mal medido, ¿cuanto se mueve el veredicto GATE-0?","0"),
 (2,"2->4: delta mal, ¿cuantas falsas alarmas de custodia?","0"),
 (2,"2->5: los 5 criterios, ¿cual domina el fallo del acto?","0"),
 (2,"2->6: el ciego, ¿aplica igual a la monitorizacion del ocupante?","0"),
 (3,"3->4: paralaje sin corregir, ¿pasa un sello violado?","0"),
 (3,"3->5: alpha por debajo de 0,95, ¿que A sale en el acto?","0"),
 (3,"3->6: flexion de cascara, ¿cuanto contamina la lectura?","0"),
 (4,"4->5: sello batido, ¿lo cazan los 5 criterios? (Johnston)","0"),
 (4,"4->6: fuego, ¿que hace la envolvente fisiologica?","0"),
 (6,"6->4: envolvente del ocupante, ¿que custodia deja fuera?","0"),
],
"F · CONTROL NEGATIVO  ¿rechaza lo que debe?": [
 (2,"permutacion de 2 unidades adyacentes","0"),
 (2,"desplazamiento a alveolo vecino (12 mm)","0"),
 (2,"sustraccion de 1 unidad","0"),
 (2,"ADICION de 1 unidad (nunca probado)","0"),
 (2,"dos defectos que se compensan (nunca probado)","0"),
 (3,"fiducial contaminado a 50 um (YA HECHO, D-674)","0"),
 (3,"placa girada 72 grados y vuelta: ¿cierra el lazo?","0"),
 (4,"sustitucion de masa igual y diametro distinto (B2)","E"),
 (4,"taladro de 0,5 mm (B4)","E"),
 (5,"impostor a 3,1 sigma: ¿lo rechaza el contrato?","0"),
 (6,"ocupante distinto con iris parecido","P"),
 (6,"atmosfera fuera de banda durante 59 minutos (ventana horaria)","0"),
],
"G · PROPAGACION  Monte Carlo extremo a extremo": [
 (1,"todas las constantes a la vez, 1e5 tiradas -> banda de A","0"),
 (2,"idem con los 5 criterios acoplados","0"),
 (3,"GATE-0 -> acto: curva de transferencia con Theil-Sen","0"),
 (4,"custodia -> acto: ¿que fraccion de fallos de sello ve el acto?","0"),
 (6,"TODO -> capa 6: la acumulacion en el colector (ratio 7,00)","0"),
 (5,"presupuesto de error completo del acto, termino a termino","0"),
 (5,"¿que termino domina? (analisis de Sobol)","0"),
 (5,"¿cuantas repeticiones del acto para A con 2 cifras?","0"),
],
"H · REPRODUCIBILIDAD": [
 (2,"20 semillas distintas: ¿cambia algun veredicto?","0"),
 (2,"float32 vs float64 en omega()","0"),
 (3,"dos plataformas (scipy distinta): ¿mismo alpha?","0"),
 (3,"orden de los fiduciales: ¿invariante?","0"),
 (5,"re-correr el ciego con otra semilla sellada","0"),
 (5,"el registro completo re-ejecutable de cero","0"),
],
}
if __name__ == "__main__":
    APAL = {1:96, 2:65, 3:24, 4:24, 6:4, 5:0}
    tot = sum(len(v) for v in B.values())
    print(f"  {tot} calculos generados\n")
    for fam, items in B.items():
        c0 = sum(1 for _,_,c in items if c=="0")
        print(f"  {fam}\n      {len(items)} calculos · {c0} a coste CERO")
    todos = [(APAL[c], c, t, k) for items in B.values() for c,t,k in items]
    todos.sort(key=lambda x:-x[0])
    print(f"\n  {'':<4}{'capa':<10}{'coste':<7}{'calculo'}")
    print(f"  {'-'*86}")
    for i,(_,c,t,k) in enumerate(todos[:12],1):
        print(f"  {i:>2}. capa {c:<5}{k:<7}{t}")
    print(f"  ... ({tot-12} mas)")
    c0 = sum(1 for _,_,_,k in todos if k=="0")
    print(f"\n  COSTE CERO: {c0}/{tot}  ·  banco: {sum(1 for _,_,_,k in todos if k=='E')}"
          f"  ·  paper: {sum(1 for _,_,_,k in todos if k=='P')}")
