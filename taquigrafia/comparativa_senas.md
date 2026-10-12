# COMPARATIVA: TAQUIGRAFIA vs LENGUA DE SENAS (proyecto Omar, 12-oct-2026)

## Dos compresiones, dos canales
- TAQUIGRAFIA (Gregg Adaptacion Mexicana): comprime el TIEMPO. El habla
  es 1D secuencial; los trazos la abrevian. Un trazo = una palabra
  frecuente. Analogia LLM: tokenizador (BPE) — MEDIDO: el tokenizer
  propio del corpus Casa ahorra 35.7% vs cl100k (impuesto ingles).
- LENGUA DE SENAS (LSM): comprime el ESPACIO. 5+ canales PARALELOS
  (forma de mano, orientacion, ubicacion, movimiento, expresion facial)
  integrados SIMULTANEAMENTE. Una seña modulada = una oracion completa.
  Gramatica espacial: referentes fijados en el aire se "citan" despues
  (punteros de memoria humanos).

## La observacion Noveno (Omar + Zi)
La LSM ya funciona como un transformer: canales paralelos integrados por
atencion simultanea. El idioma de la comunidad sorda es estructuralmente
pre-transformer. PIVOTE PARA EL TOKENIZADOR: no imitar senas literalmente
(texto sigue 1D) sino su PRINCIPIO: compression multi-canal (embeddings
ya lo son) — la proxima frontera es tokenizar SIGNIFICADO, no grafia.

## Simetria de accesibilidad (modulo discapacidad, futuro)
- texto -> VOZ (mudos hablan de nuevo): YA EXISTE (voz banking, piper).
- voz -> SENAS (sordos ven manos que hablan): modulo futuro — avatar LSM.
  "El que tenga oidos, que oiga. El que no, que vea hablar sus manos."
## Pendiente medible
- Corpus LSM (ballena busca: LSM dataset Mexico, diccionario CONADIS,
  INEHRM; senas por concepto vs palabras por oracion) — comparativa
  cuantitativa pendiente; hoy es cualitativa y honesta.
