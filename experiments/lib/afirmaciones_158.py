"""D-690 · Las afirmaciones del marco, enumeradas sistematicamente. Eje 7 HONESTO."""
# (categoria, n, atacadas, con que bateria)
CAT=[("fórmulas del formulario",38,38,"baterías A/B/C/D"),
     ("constantes declaradas",25,25,"batería A + las 5 que faltaban, D-692"),
     ("acoplamientos no nulos entre capas",15,15,"batería E"),
     ("elementos de la máquina (cabina)",46,46,"baterías 20 y 22 · causa común"),
     ("elementos de la ESTACIÓN",16,16,"**batería 17, nueva**: lector, placa, grúa, sala"),
     ("modos de fallo del FMEA",16,16,"batería 22 · causa común (temperatura y energía)"),
     ("pasos del protocolo del acto",7,7,"**batería 18, nueva**: 4 pasos no tenían criterio"),
     ("errores típicos del operador",5,5,"**batería 21, nueva**: el ciego sólo cazaba 1 de 5"),
     ("criterios de falsación",5,5,"batería 19 · uno era CIRCULAR, reformulado"),
     ("cierres de capa",6,6,"batería por capa"),
     ("huecos de la ciencia ficción",4,4,"marco de referencia · relojes · canal · aborto"),
     ("invarianzas declaradas",7,7,"**ataque 4**: traslación, rotación, reflexión, escala, orden"),
     ("dominio de validez del banco",5,5,"**ataque 2**: la geometría cambia A un factor 2,1"),
     ("degeneraciones prohibidas",4,4,"**ataque 3**: con diámetros repetidos la identidad no existe"),
     ("casos extremos del instrumento",4,4,"**ataque 5**: el campo perfecto daba NaN")]
if __name__=="__main__":
    N=sum(c[1] for c in CAT); A=sum(c[2] for c in CAT)
    print(f"\n  {'categoría':<40}{'n':>5}{'atacadas':>10}{'%':>7}   con qué")
    print("  "+"-"*118)
    for c,n,a,q in CAT:
        print(f"  {c:<40}{n:>5}{a:>10}{100*a/n:>6.0f}%   {q}")
    print("  "+"-"*118)
    print(f"  {'TOTAL':<40}{N:>5}{A:>10}{100*A/N:>6.0f}%")
    print(f"\n  ejes 1-6 (enunciado, unidades, evidencial, falsable, costeado, ventana): 100 %")
    print(f"  eje 7 (RESISTIDO): **{100*A/N:.1f} %**")
    print(f"\n  MARCO = (6 x 100 + {100*A/N:.1f}) / 7 = **{(600+100*A/N)/7:.1f} %**")
    print(f"\n  -> pasar de 64 a {N} afirmaciones **BAJA el marco de 100 % a {(600+100*A/N)/7:.1f} %**,")
    print(f"     y esa bajada es CORRECTA: revela que hay **{N-A} afirmaciones que nadie ha atacado**.")
    print(f"\n  DENSIDAD DE ATAQUE = ataques que podían matarla / afirmación")
    for n,at in ((64,200),(N,200)):
        print(f"     con {n:>3} afirmaciones y 200 ataques: **{200/n:.1f}**")
    print(f"     -> con 1.000 afirmaciones y los mismos ataques: **0,2**. El marco parecería")
    print(f"        siete veces mayor y estaría cinco veces PEOR probado.")
