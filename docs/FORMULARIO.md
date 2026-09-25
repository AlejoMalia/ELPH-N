# FORMULARIO DEL MARCO · ELPH-N

**Las ecuaciones sólidas del marco, en un sitio.** Cada una con su dominio de validez, sus unidades y
su origen. Una fórmula sin dominio declarado no es sólida: es una fórmula con suerte.

Estado: **MED** medido · **DER** derivado · **LIT** literatura · **DEC** declarado.

---

## I · CONTRATO

### 1. Desacuerdo
```
Ω = 1 − corr                                      [adimensional]
Ω_disposición = mediana‖p_A − p_B‖ / L            punto de ruptura 50 %
Ω_inventario  = P_p‖p_A − p_B‖ / L                con p ≥ 100(1 − 1/2n)
```
**Dominio:** n ≥ 3, emparejamiento por asignación óptima. **DER + MED.**

### 2. Banda de acuerdo
```
A = √( Ω_imp / Ω_acto )                           [adimensional]
```
**Ω_imp = el impostor MÁS CERCANO**, no el típico. El impostor es *una dirección de destino
equivocada*, nunca otro individuo. **DER + MED** (3·10⁶ impostores).

### 3. Zona muerta del contrato
```
dA/A = ½ √( u_imp² + u_acto² )
contrato ⟺ A > 1 + dA/A
```
Con u = 10 %: **A ∈ [0,934 · 1,071] es EMPATE, no contrato.** **DER.**

### 4. Contrato como tasa
```
FAR = P(Ω_imp ≤ Ω_acto)
FAR ≤ 3/k          con k impostores y CERO por debajo   (regla de tres, 95 %)
```
**Un FAR sin su k no dice nada.** Medido: FAR ≤ 10⁻⁶ con k = 3·10⁶. **MED.**

### 5. Índice de decidibilidad (Daugman)
```
d′ = |μ_I − μ_G| / √( (σ_I² + σ_G²)/2 )
```
**LIT** (Daugman 2006, 2·10¹¹ comparaciones). Medido en nuestro acto: d′ = 5,5.

### 6. Multiplicidad — el mejor de k
```
F_k(x) = 1 − [1 − F_0(x)]^k
```
La asignación óptima escoge la mejor de muchas correspondencias. **La multiplicidad efectiva se MIDE
contando cuántas compiten dentro del umbral; ni 1 ni n!.** **DER + LIT.**

### 7. Ley de la banda
```
A = K_d √( a / σ )        K₂ = 0,632 · K₃ = 0,597
```
**Robusta a su propio exponente:** con 0,4 en lugar de 0,5, A = 3,82 y el contrato aguanta; haría
falta p < 0,212. **DER + MED** (3 sustratos + D-605: 0,56).

### 8. Exclusión instantáneo–certificado
```
ψ = g K⁴ / A⁴                 g = 3 + (3 − dim del grupo de simetría)
ψ = 1  ⟺  A = (g K⁴)^¼ = 0,786 < 1
```
**Instantáneo y certificado se excluyen, con margen.** En nuestro acto ψ = 1,03·10⁻⁴: el acto es
**9.713 veces más material que informacional**. **DER.**

---

## II · INSTRUMENTO

### 9. Umbral dinámico
```
δ = K_Δ · (σ_suelo / μ_suelo) · √2          K_Δ = 3
umbral = (1 + δ) · suelo
```
El **√2** es porque hay dos medidas independientes (origen y destino) y las varianzas se suman.
**Guarda obligatoria: abortar si n < N_suelo_min.** K_Δ = 1 daría 9 % de falsos vetos; K_Δ = 3 da 0 %.
**DER + MED.**

### 10. Ruido del suelo
```
error relativo de δ = 1 / √(2(n − 1))
```
n = 10 → 24 % · n = 50 → 10 %. **El suelo se mide RE-COLOCANDO, no re-fotografiando** (regla 413).
**DER + MED.**

### 11. Ventana de promediado
```
POR RUIDO            N ≥ 9 (σ/tol)²
POR ENMASCARAMIENTO  N ≤ 1/β           β = punto de ruptura del estimador
si N_ruido > N_masc  →  no se promedia: se exige que pasen TODAS
```
**La ventana la fija el punto de ruptura.** **DER.**

### 12. Punto de ruptura del percentil
```
β(p, n) = (100 − p)/100 · n            atípicos tolerados
p ≥ 100 (1 − 1/(2n))                   para detectar UNA unidad
```
p98 con n=50 tolera exactamente 1 → detecta el **10 %**. p99 → **100 %**. **MED.**

### 13. Ligaduras
```
ligaduras = d·n − d(d+1)/2             en 3D: 3n − 6     (Maxwell, 1864)
déficit = 6 para todo n                los seis del cuerpo rígido
```
**El `n ≥ 49` NO viene del rango: viene de la precisión exigida.** **DER + LIT.**

---

## III · MÁQUINA

### 14. Campo de desacuerdo
```
D(r) = C · r^α                          [C] = µm·mm^(−α)
```
⚠ **α es un parámetro AJUSTADO, luego las unidades de C cambian en cada ajuste: un umbral fijo sobre
C no es dimensionalmente válido.** El criterio va sobre `D(r₀)` en una separación de referencia.

### 15. Puente con el núcleo gaussiano del gremio
```
D²(r) = 2d [ C(0) − C(r) ]                     función de estructura

núcleo gaussiano    C = σ²exp(−(r/υ)²)   →   α = 1
núcleo exponencial  C = σ²exp(−r/υ)      →   α = 0,5
```
**α ≥ 0,95 exige un campo diferenciable en media cuadrática.** Un campo exponencial da 0,5 y **no pasa
nunca**. **DER + LIT.**

### 16. Regla de decisión del GATE-0
```
VETO        si α < 0,35                        fiable al 98,7 %
PASA        si α ≥ 0,95  Y  D(176 mm) ≤ 35 µm
INTERMEDIO  todo lo demás                      NO basta para lanzar el acto
```
**GATE-0 es un veto fiable y un visto bueno malo (46 %).** Estimador: **Theil-Sen** (ruptura 29,3 %);
con OLS una mota de 50 µm arrastra α de 0,974 a 0,765. **MED.**

### 17. Requisito de correlación · **la ley del mapa**
```
υ ≥ L                  υ/L converge a 0,6
```
**υ es del tamaño de la OPERACIÓN que conformó la pieza.** Fresadora punto a punto: 100-500 mm.
Molde, prensa, embutición, hidroconformado: la pieza entera.
> **Las dos cáscaras deben conformarse en UNA operación con el mismo utillaje.** **DER.**

### 18. Supresión de armónicos
```
multi-paso con n posiciones  →  los armónicos múltiplos de n NO se separan
```
Rejilla cuadrada → sólo n=4 → ciega a 4θ, que es la perpendicularidad X/Y de una fresadora de 3 ejes.
**Un reparto circular no alcanza las esquinas de un campo cuadrado: o el campo es redondo, o no hay
giros.** **DER + MED.**

### 19. Paralaje por altura de asiento
```
r_real = r_aparente · (L_cam − h(R)) / L_cam        h(R) = √(R² − r_asiento²)
```
Hasta **400 µm** en el borde con diámetros de 6-18 mm. Residuo tras corregir: **0,03 µm**.
**La identidad corrige su propia lectura.** **DER + MED.**

---

## IV · CUSTODIA Y ESTRUCTURA

### 20. Pared por carga viva
```
t ≥ √( k · m · g · (L/2) / (E · suelo) )           k ≤ 0,5 (Timoshenko / WRC 107)
```
Acero ≥ 4,0 mm · aluminio ≥ 6,5 · composite ≥ 7,5 (robusto a toda la familia de k). **DER + LIT.**

### 21. Pandeo externo
```
P_cr = 2E / √(3(1−ν²)) · (t/R)²        knockdown por imperfección ≈ 0,2
```
**DER + LIT** (ASME).

### 22. Choque térmico ⚠
```
σ = E α ΔT / (1 − ν)
```
**A ΔT = 60 °C se alcanza la fluencia. Criterio: |ΔT| ≤ 50 °C entre caras, ventana instantánea.**
**DER.**

### 23. Fatiga por ciclado
```
σ_ciclica = P R / (2t) < 0,4 S_y            cada acto = 1 ciclo
```
11,9 MPa contra 82: vida infinita. **DER + LIT** (ASME).

### 24. Permeación de gas por el sello
```
Q = P · A · Δp / L                  [P] = sccm·cm/(s·cm²·atm)
```
EPDM: 15 años para salir de la banda NASA. FKM: 246. **La permeación no es el cuello: lo es la fuga
ALREDEDOR del sello, que es otra magnitud.** **DER + LIT.**

### 25. Tasa de fallo operacional
```
tasa ≤ 3/n           con n actos observados y CERO eventos
```
TUP: 37 ocupantes, 0 muertes → **≤ 8,1 %**. Para afirmar 10⁻³ hacen falta 3.000.
**«Cero muertes en 37» significa «como mucho 1 de cada 12».** **LIT + DER.**

---

## V · OCUPANTE

### 26. Tolerancia al choque — **régimen de IMPACTO (< 2 s)**
```
g ~ t^(−0,461)              R² = 0,968       (Eiband, NASA Memo 5-19-59E, 1959)
```
45 g @ 44 ms · 25 g @ 0,2 s · 10 g @ 1,6 s. Pendiente de subida ≈ **500 G/s**.
**Exponente 0,46 = ENERGÍA constante, no impulso (1,0). El daño humano es limitado por energía.**
⚠ ASTM D3332 usa exponente 1: **se resuelve por alcance — Eiband rige el ocupante, D3332 la carga
inerte, y rige el menor.** **LIT.**

### 27. Tolerancia sostenida — **régimen de TRÁNSITO (> 2 s)** ⚠
```
4,5 g  de pie          9 g  reclinado + traje anti-g          25 g  inmersión líquida
```
> **Eiband NO aplica a un tránsito de minutos.** Confundir los dos regímenes da 45 g donde lo
> correcto son 9. **LIT.**

### 28. Tiempo de tránsito
```
t = 2 √( d / a )              a = g_sostenido · 9,81
```
**El tiempo lo fija el OCUPANTE, no la masa.** La masa fija la **energía**, que escala como **L³**.
**DER.**

### 29. Autonomía de una cabina sellada ⚠
```
t_CO2 = V · (3/760) / (n · 0,5 L/min)          límite NASA: 3 mmHg, media horaria
t_O2  = 0,065 · V · 0,21 / (n · 0,55 L/min)    banda NASA: 145-155 mmHg
```
Con V = 2 m³ por ocupante: **t_CO2 = 15,8 min, INDEPENDIENTE de n** (el volumen escala con los
ocupantes). El CO₂ manda siempre. **DER + LIT.**

### 30. **Acoplamiento soporte vital ↔ aceleración** ⚠ *(el más reciente)*
```
cabina SELLADA viable  ⟺  t_viaje(a) < t_CO2
```
NY–Tokio: a 1 g el viaje dura 35 min y el CO₂ da 16 → **ECLSS obligatorio**. A 9 g dura 11,7 min →
**llega sellada con 4,1 min de margen**.
> **No se puede ir CÓMODO y SELLADO a la vez.** La decisión de soporte vital y la de aceleración
> **no son independientes**, y el marco las trataba en capas separadas. **DER.**

---

## V-ter · LIMBOS

### 39. Definición de limbo ⚠
```
L = [t_inicio , t_fin]   intervalo durante el cual una GARANTÍA del marco
                         queda SUSPENDIDA
```
No es una metáfora: es **un estado con inicio, fin y garantía identificada**, y por tanto medible.
**DER.**

### 40. Riesgo de un limbo ⚠
```
riesgo(L) = duración · P(evento) · (1 − P(mitigación disponible))
```
> **El peligro de un limbo NO es su duración.** Un limbo largo con mitigación es administrativo;
> **uno corto sin mitigación es letal.** **DER.**

### 41. Los seis limbos del acto

| | garantía suspendida | dura | mitigación | clase |
|:--|:--|--:|:--|:--|
| **L1** jurídico | el ocupante está **certificado** | 12,4 min | alta | administrativo |
| **L2** custodia | cabe **intervención externa** | 10,0 min | parcial | **grave** |
| **L3** identidad | la identidad está **confirmada** | 12,4 min | alta | administrativo |
| **L4** jurisdiccional | **alguna estación tiene custodia** | **3,4 min** | **NULA** | **el peor** |
| **L5** irreversibilidad | el acto se puede **cancelar** | 2,4 min | baja | grave |
| **L6** reserva | la capacidad de B está **libre** | variable | alta | económico |

> **El más peligroso es el más corto.** **El orden por duración y el orden por peligro son
> INVERSOS.** **DER + MED.**

### 42. Exposición total del acto
```
E = Σ riesgo(Lᵢ)                  [minutos-equivalentes de riesgo]
```
Medida sobre el acto de 50 min: **E = 12,8**, de los cuales **L2 aporta el 39 % y L4 el 27 %
—el 66 % entre los dos con sólo el 27 % del tiempo—.
**L4 es el único limbo irreducible: sólo baja subiendo la aceleración, y eso sube Eiband.**
**DER + MED.**

### 43. Elasticidad de los limbos ⚠
```
e(L, x) = (∂L/L) / (∂x/x)

L4 = τ = 2√(d/(a·g))      e(L4,d) = +0,50   e(L4,a) = −0,50   e(L4,m) = **0,00**
L5 = 0,70·τ               mismas elasticidades
L2 = prep + τ + apertura  mixta, y **acotada por el reloj de CO₂**
L1 = L3 = τ + T_B(m)      ruta por τ, masa por el régimen de manejo
```
> **El limbo más peligroso es el único que NO depende de la masa.** Un tornillo y un elefante tienen
> exactamente el mismo L4 en la misma ruta. **DER.**

### 44. Umbral de fusión L2–L4 ⚠
```
d_fusión = a·g·(t_CO₂/2)² = 19.837 km
```
Por encima, el tránsito supera el reloj de CO₂, hace falta ECLSS, **y L2 deja de ser 10 min para
pasar a ser todo el tránsito: los dos peores limbos se funden en uno, con mitigación nula.**
Londres–Sídney (17.000 km) queda **justo por debajo**. **DER.**

### 45. Suelo físico de L4
```
L4_mín = 2√(d/(25·g))     25 g = inmersión líquida, el máximo sostenido humano
```
| ruta | 9 g | **suelo (25 g)** |
|:--|--:|--:|
| Londres–Berlín | 3,4 min | **2,1 min** |
| Tierra–Luna | 69,6 min | **41,7 min** |
| **Tierra–Marte** | 13,9 h | **8,3 h** |

> **De 9 g a 25 g, L4 sólo cae un 40 %, y 25 g exige inmersión líquida total.**
> **Para Marte, el mejor caso concebible deja 8,3 horas sin custodia y sin intervención posible.**
> **DER + LIT** (Eiband).

### 46. Partir la ruta · exposición máxima contra tiempo total
```
L4(k tramos) = 2√(d/(k·a·g))      tiempo de vuelo total = k · L4
```
Marte en 4 tramos: **L4 baja de 13,9 a 6,9 h** y el vuelo total sube de 13,9 a **27,7 h**.
> **Se cambia exposición máxima por tiempo total — el mismo intercambio que hace la aviación con
> las escalas.** **DER.**

---

## VI · ESCALA

### 31. Dificultad de certificación
```
Ω ∝ 1/L                    una cabina mayor es MÁS FÁCIL de certificar
α decrece con L            una cabina mayor hace el GATE-0 IMPOSIBLE
```
**Los dos efectos son opuestos y del cruce sale `υ ≥ L` (fórmula 17).** **DER.**

### 32. Masa y energía
```
t_pared ∝ L        M_cáscara ∝ L³        E ∝ M ∝ L³
```
De 30 cm a 3 m: la cáscara pasa de 9 a 888 kg, **×99 de energía para el mismo viaje en el mismo
tiempo**. **DER.**

---

## VII · MÉTODO

### 33. Escala evidencial
```
duda = Π (1 − wᵢ)  sobre líneas INDEPENDIENTES, tope 0,99
MED_AJ 0,95 · MED_PRO 0,85 · DER 0,70 · LIT 0,60 · DEC 0,30
corroboración matemática: factor 0,8 sobre el residuo (NO es independiente)
```

### 34. Regla 4, hasta el fondo
```
capa  = MÍNIMO de sus condiciones
marco = MÍNIMO de las capas
```
**Promediar condiciones deja que la nota la decida qué condiciones metes en la lista.**

### 35. Completitud de una afirmación
```
completa ⟺ enunciada ∧ dimensionada ∧ fechada ∧ falsable ∧ costeada ∧ acotada ∧ RESISTIDA
```
Siete ejes. **Completo y verificado son dos cosas y se reportan las dos.**
