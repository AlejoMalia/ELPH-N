# Datos: fuentes, hashes y cómo rehacerlos

**Los datos brutos no se versionan.** Pesaban 1,2 GB y son reproducibles desde su URL. Lo que sí está en el repositorio son los **subgrafos congelados** en `experiments/*/results/`, con su SHA-256 — que son el registro experimental.

---

## Fuentes utilizadas

### *C. elegans* — conectoma completo
```bash
curl -L -o data/celegans/herm_full_edgelist.csv \
  https://raw.githubusercontent.com/openworm/c302/master/c302/data/herm_full_edgelist.csv
```
`sha256 = 142693f17556148d7f962835b18ac6dd5af18b7467eef61815ebc1dd5474c0ca`
448 neuronas · 4.681 químicas · 2.698 eléctricas. *(Copia congelada en `experiments/fase-V/results/`.)*

### *Drosophila* — FlyWire FAFB v783
```bash
curl -L -o data/flywire/connections.csv.gz \
  https://storage.googleapis.com/flywire-data/codex/data/fafb/783/connections.csv.gz
curl -L -o data/flywire/neuron_annotations.tsv \
  https://raw.githubusercontent.com/flyconnectome/flywire_annotations/main/supplemental_files/Supplemental_file1_neuron_annotations.tsv
```
`connections sha256 = d49dd692e59e153aa3c83f5257bfc0eff51247b86d7bb183386c6d1622c70fc9`
`annotations sha256 = 9a4f8b2f843196074431ebd7cd883536afa1be86c8a4ce90970441e8be81d1be`
139.248 neuronas anotadas · 3,9 M conexiones · **`top_nt` da el signo**.

### Humano — H01 (corteza temporal)
```bash
B=https://huggingface.co/NathanRoll/h01-cortex-snn/resolve/main
curl -L -o data/humano/edges.npz    $B/edges.npz
curl -L -o data/humano/metadata.npz $B/metadata.npz
```
`edges sha256 = d685966d1818b32c89f6bd53c0a56a39c4e046899935c9318b250525d2cbd572`
`metadata sha256 = ce26bffbb2107bb4c6805d0f52a313d59a6b6b52452807907ef3d9f260e87743`

⚠️ **Paquete de terceros**, no release institucional. 16 descargas. Derivado de los shards Avro oficiales de H01, filtrado a confianza ≥ 0,50. **Por eso H-1 y H-2 son [PILOTO], no [MEDIDO].**

### La fuente institucional SÍ es accesible — verificado (H-3)

`gs://h01-release` es público por HTTPS y no exige token. Comprobado **sin descargar el volumen**:

| pieza | ruta | tamaño | veredicto |
|---|---|---|---|
| **Tabla de somas** | `data/20210601/c3/tables/somas.csv` | **6,26 MB** | ✅ **institucional.** 49.379 somas con tipo celular y capa |
| **Sinapsis** | `data/20210601/c3/synapses/exported/` | 2,96 GB Avro | ✅ grafo neurona → neurona |
| **E/I** | `synapses/incoming_{excitatory,inhibitory}/` | volumétrico | ⚠️ **segmentación, no tabla** |

**Lo verificado leyendo cabeceras y un solo shard:**

1. **Los tipos celulares del paquete de terceros SON los institucionales.** Las neuronas de `somas.csv` suman **exactamente 16.087**, el mismo recuento del paquete. Lo propio del paquete no eran los tipos, sino **inferir el signo de ellos**.
2. **El peso continuo existe.** El recuadro delimitador de cada sinapsis da un volumen con **24.152 valores distintos** (p05 = 1.932 · p50 = 15.504 · p95 = 104.652). **El eje de tasa es recuperable.** Los campos de área de contacto y número de vóxeles están en el esquema pero **vacíos**.
3. **El campo de tipo de sinapsis NO es el signo.** Comprobado y descartado: con presináptico INTERNEURON da 84,3 % del valor 1, y con PYRAMIDAL 70,8 %. Ninguna asignación E/I produce eso. La etiqueta de clase tampoco: es el compartimento (axón, dendrita, soma, segmento inicial).
4. **Rendimiento del filtro:** 724 de 998.235 sinapsis del shard 0 son neurona→neurona con soma (**0,073 %**) ⇒ ~109.000 aristas en el volumen completo, comparable a las 116.611 del paquete.

**Lo que falta para [MEDIDO], y su coste real:** el signo por sinapsis está en una **capa volumétrica**, así que exige una consulta de vóxel por sinapsis (~109.000 sobre un volumen fragmentado). **No está bloqueado: es ingeniería, no una descarga.** Y es la única pieza que separa al humano de [MEDIDO], porque la procedencia y el peso continuo ya están resueltos.

**Uniones gap: siguen sin anotarse.** M₃ sigue siendo [FUERA] en humano, igual que en mosca.

---

## Fuentes comprobadas y DESCARTADAS

Siete fuentes de mamífero, seis descartes, **cada uno por un motivo distinto y ninguno requiriendo ejecutar el pipeline**. Se documentan para que nadie repita el recorrido.

| Fuente | ¿Grafo? | ¿Signo? | Motivo del descarte |
|---|---|---|---|
| **MICrONS vía CAVE** | — | — | Exige token de autenticación |
| **Zenodo 16905603** | ❌ | ✅ E/I explícito | `all_input_synapses.csv` **no tiene `pre_pt_root_id`**: registra sinapsis *sobre* las células pero no quién las hace. Detectado con una **petición parcial de 3 KB** en vez de bajar 699 MB |
| **Basil** (2,15 GB) | ✅ `presyn→postsyn` | ❌ | El release solo tiene `clefts/`, `em/`, `nuclei/`, `seg/`. Ninguna anotación de tipo celular |
| **H01 oficial** (GCS) | volumétrico | ❌ | Neuroglancer/Avro, **sin tabla de tipos celulares**. Solo 104 células revisadas |
| **Pinky100** | ✅ soma→soma | ⚠️ **presente pero constante** | **0 de 1.961 aristas con presináptico inhibitorio.** M₁ y M₂ serían la misma red |
| **Motta L4** | ❌ bipartito | ✅ 12,8 % inhib. | Matriz axón→**compartimento**, no neurona→neurona. No cierra el bucle |
| Listas generales (OpenNeuro, CRCNS, DANDI, NWB, HCP) | — | — | Actividad o regiones, no conectividad con signo |

**Modo de fallo que aportó Pinky, ahora en el catálogo de nivel 0:** *la variable presente pero sin varianza*. No es «falta el dato»: está y es inútil.

---

## Regla

> **Antes de descargar nada, comprobar que la fuente tiene las dos piezas: grafo neurona→neurona Y signo con varianza.** Una petición de cabecera o un rango de 3 KB bastan. Es más barato que cualquier prueba pequeña.
