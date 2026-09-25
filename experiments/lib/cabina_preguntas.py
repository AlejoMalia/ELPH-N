"""D-688 · Las cuatro preguntas de la cabina, contestadas con lo que ya medimos."""
import math
print("  "+"="*96)
print("  Q1 · ¿SE PUEDE CONSTRUIR Y OPERAR AL AIRE LIBRE?")
print("  "+"="*96)
print("\n  No hace falta preguntarse qué EMITE. La respuesta sale de lo que hay que MEDIRLE.\n")
ALFA,SUELO,LEC = 12e-6, 141e-6, 0.52e-6
print(f"  a) TERMICA · el suelo es {SUELO*1e6:.0f} um y el acero dilata {ALFA*1e6:.0f} um/m/K")
print(f"     {'cabina':>8}{'dT para mover 10 % del suelo':>32}")
for L in (0.3,1.26,2.71,4.0):
    dT=0.1*SUELO/(ALFA*L)
    print(f"  {L:>10.2f} m{dT:>28.2f} K")
print(f"     -> **hace falta +-1 K.** Una nave al aire libre ve 15 K en una tarde.")
print(f"     -> la metrologia dimensional de precision trabaja a 20 +- 0,1 C. NO es opcional.\n")
print(f"  b) PARTICULAS · D-674 lo midio: **UNA mota de 50 um en UN fiducial de 25**")
print(f"     arrastra alpha de 0,974 a 0,765 y convierte PASA en INTERMEDIO.")
print(f"     Con Theil-Sen aguanta hasta el 29 % de fiduciales contaminados = 7 de 25.")
print(f"     -> al aire libre, 7 motas de 50 um sobre una placa en horas es **seguro**.\n")
print(f"  c) VIBRACION · el suelo de 141 um se mide RE-COLOCANDO 10 veces.")
print(f"     Cualquier vibracion ambiental entra directa en esa dispersion.\n")
print("  >>> **RESPUESTA: NO. Y no porque la cabina EMITA algo, sino porque se la MIDE.**")
print("      El recubrimiento no es blindaje: es **sala de metrologia**. +-1 K, filtrada,")
print("      sobre bancada aislada. Es un requisito de la ESTACION, no de la cabina.")
print("\n  "+"="*96)
print("  Q2 · ¿ES ESCALABLE DE 30x30 cm A 4x4 m?")
print("  "+"="*96)
print(f"\n  {'lado':>7}{'Om':>11}{'alpha con ups=300':>20}{'upsilon necesaria':>20}{'   proceso que la da'}")
import sys; sys.path.insert(0,'experiments/lib')
from alpha_gp import alpha_efectiva
for L,proc in ((0.3,"mecanizado o prensa pequena"),(1.26,"embuticion profunda"),
               (2.71,"hidroconformado grande"),(4.0,"repulsado / domo de tanque")):
    al=alpha_efectiva(300.,'gauss',16.,L*1000*0.9)
    u=next(u for u in [100*1.05**i for i in range(200)] if alpha_efectiva(u,'gauss',16.,L*1000*0.9)>=0.95)
    print(f"  {L:>5.2f} m{141e-6/L:>11.1e}{al:>20.3f}{u:>17.0f} mm   {proc}")
print("\n  >>> **RESPUESTA: SI, pero el PROCESO DE FABRICACION no es el mismo en los dos extremos.**")
print("      Om mejora con el tamano (x13 de 30 cm a 4 m) y alpha empeora. Lo que hace")
print("      escalable el marco NO es la geometria: es que exista un utillaje que conforme")
print("      la pieza entera de una vez a ese tamano. **A 4 m eso existe: los domos de")
print("      tanque de cohete se repulsan a 5-10 m. A 30 cm tambien. En medio, tambien.**")
print("      La escalabilidad es una propiedad de la INDUSTRIA disponible, no del marco.")
print("\n  "+"="*96)
print("  Q3 · ¿NECESITA ENERGIA CONTINUA?")
print("  "+"="*96)
P={'sensores continuos OCHMO (5 canales)':10,'iluminacion interior':20,
   'comunicacion y telemetria':50,'control de ventilacion':15,'instrumentacion del ocupante':5}
tot=sum(P.values())
print(f"\n  {'elemento':<40}{'W':>6}")
for k,v in P.items(): print(f"  {k:<40}{v:>6}")
print(f"  {'TOTAL':<40}{tot:>6} W\n")
print(f"  {'acto':<34}{'duracion':>12}{'energia':>12}{'   equivalente'}")
for nom,h in (("Londres-Berlin (1 persona)",74.6/60),("Tierra-Luna",2.3),("Tierra-Marte",15.1)):
    E=tot*h
    print(f"  {nom:<34}{h:>10.1f} h{E:>10.0f} Wh   {'bateria de portatil' if E<200 else ('bateria de moto' if E<2000 else 'bateria de coche electrico pequena')}")
print(f"\n  Y lo que NO consume energia:")
print(f"     depurador de CO2 de LiOH .... reaccion quimica, **pasiva**")
print(f"     suministro de O2 ............ gas comprimido, **pasivo**")
print(f"     diluvio ..................... presion almacenada, **pasivo hasta que dispara**")
print(f"     sello, cascara, fiduciales .. **pasivos**")
print("\n  >>> **RESPUESTA: NO necesita alimentacion CONTINUA externa.** La energia es una")
print(f"      cantidad ALMACENADA y es pequena: **{tot*74.6/60:.0f} Wh para un acto terrestre**,")
print("      lo que lleva un portatil. Los subsistemas criticos (CO2, O2, extincion) son")
print("      **quimicos o de presion almacenada, no electricos**. Eso es una decision de")
print("      diseno que el marco puede EXIGIR: **ningun elemento vital depende de la corriente.**")
print("\n  "+"="*96)
print("  Q4 · ¿INDEPENDIENTE O DEPENDIENTE?")
print("  "+"="*96)
print("""
  Hay que separar las dos fases, porque la respuesta es distinta en cada una:

  EN TRANSITO ................ **INDEPENDIENTE**
     sellada · energia almacenada · CO2 y O2 pasivos · extincion a bordo ·
     registrador autonomo · apertura desde dentro. No necesita NADA de fuera.

  EN LAS ESTACIONES .......... **DEPENDIENTE, y totalmente**
     lector optico · placa de fiduciales · asiento cinematico · grua ·
     sala a +-1 K · el SUELO medido localmente (10 re-colocaciones)

  >>> **RESPUESTA: la burbuja lleva su propia VIDA; NO lleva su propia CERTIFICACION.**

  Y eso tiene una consecuencia programatica que no habiamos enunciado:
""")
print("     **NO SE PUEDE CERTIFICAR UNA LLEGADA A UN SITIO QUE NO TIENE ESTACION.**")
print("     El suelo de destino se mide EN destino, re-colocando alli. Luego Marte")
print("     necesita una estacion CONSTRUIDA ANTES del primer acto, y esa estacion")
print("     no puede llegar teletransportada: **tiene que ir en nave, como todo.**")
print("\n     El teletransporte certificado no es un sustituto del transporte: es lo que")
print("     se puede hacer DESPUES de que el transporte haya construido las dos orillas.")
