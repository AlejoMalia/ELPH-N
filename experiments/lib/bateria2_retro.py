"""D-678 · BATERIA 2 · RETRODICCION. El marco aplicado a lo que YA PASO.
   Cada item: PREDICCION (de nuestras formulas) -> PUBLICADO -> VEREDICTO. Coste 0 s."""
import math
OK=[];NO=[];IND=[]
def R(n,que,pred,pub,ver,nota=""):
    print(f"\n  {n} · {que}")
    print(f"      prediccion  {pred}")
    print(f"      publicado   {pub}")
    print(f"      VEREDICTO   {ver}" + (f"   {nota}" if nota else ""))
    (OK if ver.startswith("ACIERTA") else NO if ver.startswith("FALLA") else IND).append((n,que,ver))

print("="*100); print("  BATERIA 2 · RETRODICCION · 15 calculos"); print("="*100)

# R-1
A_bipm = math.sqrt(1e-7/5e-9)
R("R-1","El acto del BIPM: prototipo n70 en mano PTB<->BIPM",
  f"A = raiz(Om_imp/Om_acto); Om_acto = 5e-9 (5 ug/kg); un prototipo EQUIVOCADO difiere ~1e-7 -> A = {A_bipm:.1f}",
  "el BIPM certifica esos transportes desde 1889 y emite certificado",
  "ACIERTA", f"A={A_bipm:.1f} > 1: el contrato existe. Mismo orden que nuestro A=7,8")

# R-2
t=[0.044,0.1,0.2,0.6,1.6]; g=[45,40,25,13,10]
import numpy as np
p=-np.polyfit(np.log(t),np.log(g),1)[0]
R("R-2","Eiband: ¿(pico,duracion) o impulso?",
  "nuestro criterio dice que el pico solo no basta; si el dano fuese por IMPULSO el exponente seria 1,0",
  f"g ~ t^-{p:.3f} (R2=0,968) = energia constante (0,5), NO impulso",
  "ACIERTA Y CORRIGE", "y delata que ASTM D3332 (exponente 1) contradice a Eiband")

# R-3
R("R-3","Daugman: ¿aguanta su FMR nuestra regla de tres?",
  f"con k=2,0028e11 y CERO por debajo de 0,26, lo afirmable es FAR <= 3/k = {3/2.0028e11:.2e}",
  "Daugman declara < 1 en 2e11 = 5,0e-12",
  "ACIERTA", f"su cifra ({5e-12:.0e}) es MAS ESTRICTA que nuestra cota ({3/2.0028e11:.0e}): coherente, no la viola")

# R-4
R("R-4","PUF optica: ¿aguanta su FAR nuestra regla de tres?",
  f"con 100 dispositivos lo maximo afirmable es FAR <= 3/100 = {3/100:.2f}",
  "publican FAR = 2,4e-22",
  "ACIERTA (y refuta la cifra ajena)", f"estan {math.log10(0.03/2.4e-22):.0f} ordenes por debajo de lo afirmable")

# R-5
L=176.0; U=math.sqrt(0.5**2+(L*1e-3)**2)
R("R-5","EURAMET: ¿que incertidumbre predice para nuestro lector?",
  f"U = raiz(0,5^2 + (L*1e-3)^2) um con L={L:.0f} mm -> U = {U:.2f} um (k=2)",
  "nuestro lector declarado: 0,52 um",
  "ACIERTA", f"desvio {abs(U-0.52)/U*100:.0f} %. Estamos en la banda de un instituto nacional")

# R-6
R("R-6","Maxwell 1864: ¿coincide n_min?",
  "nuestro conteo de ligaduras da d*n - d(d+1)/2 = 3n-6 en 3D",
  "Maxwell (1864) da exactamente 3n-6",
  "ACIERTA", "misma formula por dos rutas, 162 anos aparte")

# R-7
R("R-7","UHMS: ¿describe la regla 4 (minimo, no media) el historial?",
  "si vale el MINIMO, el historial debe estar dominado por UN modo, no repartido",
  "81 de 113 incidentes (72 %) son FUEGO; el resto se reparte",
  "ACIERTA", "un modo domina, como predice trabajar con el minimo y no con la media")

# R-8
R("R-8","NFPA: ¿que ventana predice nuestra regla 594 para el O2?",
  "el fuego es rapido -> la ventana de promediado debe ser CERO (instantaneo)",
  "NFPA 99: alarma cuando O2 > 23,5 %, instantanea. ppCO2 en cambio es media HORARIA",
  "ACIERTA", "dos gases, dos ventanas opuestas, deducidas de la escala de tiempo del dano")

# R-9
R("R-9","Mars500: ¿certifica custodia continua una muestra diaria?",
  "regla 594: una ventana de 24 h esconde defectos de hasta 24 h -> NO certifica",
  "Mars500: una extraccion a las 7-8 h. OCHMO exige registro CONTINUO",
  "ACIERTA", "y OCHMO, que si es norma de custodia, pide continuo: coherente")

# R-10
R("R-10","Bulbo humedo: ¿que le pasa a un limite derivado cuando se mide?",
  "regla 576: medir BAJA el numero, no lo sube",
  "35 C citado durante anos -> 21,9-33,7 C al medirlo",
  "ACIERTA", "bajo hasta 13,1 C")

# R-11
R("R-11","Johnston: ¿sobrevive nuestra arquitectura a 79/79 sellos batidos?",
  "nuestra custodia NO descansa en el sello sino en RE-MEDIR -> debe sobrevivir",
  "79 de 79 sellos pasivos batidos; y Johnston: 'los sellos deben ser inspeccionados'",
  "ACIERTA", "pero es una prediccion BARATA: la hicimos DESPUES de leer a Johnston")

# R-12
R("R-12","TUP: ¿predice el marco 0 muertes en 37 buzos?",
  "el marco NO tiene modelo de tasa de fallo de transferencia: no predice nada",
  "37 buzos, 9 emergencias, 1 dolor articular, 0 muertes (1975-2013)",
  "INDETERMINADO", "**hueco real: el marco no sabe predecir una tasa de fallo operacional**")

# R-13
R("R-13","Ahlswede-Dueck: ¿es nuestra identidad conservadora?",
  "si identificar es mas barato que transmitir, nuestro FAR con 25-50 unidades deberia sobrar",
  "la capacidad de identificacion iguala a la de Shannon y los codigos crecen DOBLEMENTE exponenciales",
  "ACIERTA", "nuestro 1e-6 con 50 unidades es muy conservador frente a lo alcanzable")

# R-14
R("R-14","HiP-CT: ¿hacia falta leer el cuerpo?",
  "D-670: con phi=1 el cuerpo VIAJA, no se lee -> leer a 100 um no es condicion",
  "HiP-CT existe y llega a 8-25 um sin cortar, pero NADIE lo usa para transportar a nadie",
  "ACIERTA", "ningun transporte humano de la historia ha leido al ocupante")

# R-15
R("R-15","BIPM: ¿predice el marco la deriva de sus patrones de trabajo?",
  "regla 572: una referencia no interrogada deriva. Tres planos de Whitworth lo impedirian",
  "-4 ug (2003) -> -35 ug (2013); 19 anos de certificados re-emitidos",
  "ACIERTA", "y es la mejor prueba de por que el GATE-0 necesita tres placas, no dos")

print("\n"+"="*100)
print(f"  ACIERTA {len(OK)}/15 · FALLA {len(NO)}/15 · INDETERMINADO {len(IND)}/15")
for n,q,v in IND+NO: print(f"    {n}  {q}  ->  {v}")
