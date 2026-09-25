"""D-682 · Cierre de los once modos de fallo del FMEA. TRIADA: se DERIVAN, no se miden."""
import math
E,NU,ALPHA,RHO,SY = 200e9,0.3,12e-6,7850.,205e6
L,t,R = 3.0,0.0044,1.5
print("  "+"="*96)
print("  1 · PANDEO EXTERNO (colapso por vacio)")
Pcr=2*E/math.sqrt(3*(1-NU**2))*(t/R)**2
print(f"      P_cr = 2E/raiz(3(1-nu^2)) (t/R)^2 = {Pcr/1e5:.0f} bar  ·  con knockdown 0,2 -> {0.2*Pcr/1e5:.0f} bar")
print(f"      exigencia: 1 bar.  **MARGEN x{0.2*Pcr/1e5:.0f}. CERRADO por derivacion.**")
print("\n  2 · FATIGA POR CICLADO  (cada acto = 1 ciclo de presion)")
sig=0.7e5*R/(2*t)
print(f"      sigma = P R/(2t) = {sig/1e6:.1f} MPa  ·  limite de fatiga del acero ~ {0.4*SY/1e6:.0f} MPa")
print(f"      **{0.4*SY/sig:.0f}x por debajo -> vida infinita. CERRADO.** Criterio: sigma_ciclica < 0,4 Sy")
print("\n  3 · CORROSION")
print(f"      practica estandar: sobreespesor de corrosion 1-3 mm sobre la pared de calculo.")
print(f"      **CERRADO por criterio: t_final = t_calculo + 1,5 mm de sobreespesor.**")
print("\n  4 · FRACTURA FRAGIL")
print(f"      criterio: T_servicio > T_transicion + 20 C.  Acero al carbono: DBTT ~ -20 a +30 C.")
print(f"      **CERRADO por SELECCION: austenitico (316L) o aluminio NO tienen DBTT.**")
print("\n  5 · FALLO DE UNION / SOLDADURA")
print(f"      **CERRADO POR EL PROPIO MARCO:** el requisito upsilon >= L (D-680) exige conformar")
print(f"      la pieza en UNA operacion. **Una cascara monolitica no tiene soldaduras.**")
print(f"      El requisito que puso el GATE-0 elimina un modo de fallo que no buscaba.")
print("\n  6 · CHOQUE TERMICO   <-- MIRAR ESTE")
for dT in (10,25,50,100):
    s=E*ALPHA*dT/(1-NU)
    print(f"      dT = {dT:>3} C  ->  sigma = E alpha dT/(1-nu) = {s/1e6:>5.0f} MPa   "
          f"{'**SUPERA Sy = 205 MPa**' if s>SY else f'({100*s/SY:.0f} % de Sy)'}")
print(f"      **NO es despreciable: a dT = 60 C se alcanza la fluencia.**")
print(f"      CRITERIO NUEVO: **|dT| <= 50 C entre cara interna y externa.** Ventana: instantanea.")
print("\n  7 · SOPORTES Y ANCLAJE")
M=RHO*4*math.pi*(L/2)**2*t; F=(M+75)*45*9.81
print(f"      cascara {M:.0f} kg + ocupante 75 kg a 45 g -> **F = {F/1e3:.0f} kN**")
print(f"      Eiband: 'la sujecion es la variable primaria' — y vale para la CABINA, no solo")
print(f"      para el ocupante. **CERRADO: anclaje certificado > {F/1e3:.0f} kN.**")
print("\n  8 · PASAMUROS")
print(f"      **CERRADO por referencia que YA citabamos: WRC 107 existe justo para cargas locales")
print(f"      en boquillas.** Criterio doble: (a) tension local dentro de WRC 107; (b) cada")
print(f"      penetracion es via de fuga Y perturbacion de fiducial -> **entra en el presupuesto**.")
print("\n  9 · AUTONOMIA DE SOPORTE VITAL   <-- Y MIRAR ESTE")
V=2.0
O2=V*1000*0.21; consumo=0.55; margen=0.065*O2
CO2lim=V*1000*(3/760); prod=0.5
print(f"      cabina sellada de {V} m3, un ocupante:")
print(f"        O2   : {O2:.0f} L a bordo · consumo {consumo} L/min · salir de la banda NASA")
print(f"               (155->145 mmHg) = {margen:.0f} L  ->  **{margen/consumo:.0f} MINUTOS**")
print(f"        CO2  : limite 3 mmHg = {CO2lim:.1f} L en {V} m3 · produccion {prod} L/min")
print(f"               ->  **{CO2lim/prod:.0f} MINUTOS**")
print(f"      **EL CO2 MANDA, Y DA {CO2lim/prod:.0f} MINUTOS. Una cabina SELLADA sin depuracion")
print(f"        solo sirve para saltos suborbitales (3,7 min). Para Marte (41,6 h) hace falta")
print(f"        ECLSS activo: {41.6*60/(CO2lim/prod):.0f} veces mas de lo que aguanta sellada.**")
print("\n  10 · ATRAPAMIENTO Y EGRESO")
print(f"      **CERRADO por criterio: apertura desde DENTRO sin herramienta, en <= 60 s.**")
print(f"      Es requisito estandar (IMCA, FAA) y coste 0 declararlo.")
print("\n  11 · EVENTO MEDICO DEL OCUPANTE")
print(f"      **FUERA DE ALCANCE, DECLARADO.** El marco certifica el VOLUMEN y su envolvente,")
print(f"      no la salud previa del ocupante. Se declara como exclusion explicita, no como hueco.")
print("  "+"="*96)
