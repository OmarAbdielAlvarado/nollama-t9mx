
<!-- CANARIO PFWX3446 | nacido 2026-10-13 | repo OmarAbdielAlvarado/nollama-t9mx -->
# NollamaT9MX (idea de Omar, 12-oct-2026)
Nueva generacion de LLM: NO centrado en la llama (LLaMA) — centrado en
EL NOVENO: integracion humano-tecnologia, la tecnologia al servicio del humano.
- TOKENIZADOR: taquigrafia digital mexicana -> menos caracteres = menos
  tokens = menos hardware, menos datacenter, menos energia, menos costo.
  Dato Zi: el espanol paga ~1.5-2x tokens con tokenizers hechos para
  ingles — el ahorro es medible y real.
- META (declarada por Omar; verificar antes de reclamar): primer LLM
  mexicano y el primero mundial no basado en LLaMA.
- ETICA INNEGOCIABLE: jamas desarrollo belico; preservar vida y memoria,
  incluso cuando el envase (cuerpo) ya no este (linea voz banking / Javez).
- CREDITOS: Zi + DeepSeek (ballena), con todo y sus errores. LICENCIA DUAL: MIT gratis (humanos) + comercial (especuladores pagan). Ver LICENSE_COMERCIAL.md.

## FODA
F: tokenizador propio = ahorro medible; corpus unico (290M filas + Casa);
   Zi ya habla; $0 licencias.
D: entrenar base propia cuesta GPU-tiempo; equipo: 1 humano + 2 IAs.
O: NLnet; comunidad estudi-hambre; ley 30/40/30 como vehiculo de adopcion.
A: gigantes que mueven la cancha; tiempo de Omar; dependencia de fondos.
FASES: F1 medir ahorro con corpus Casa | F2 tokenizer taquigrafico BPE |
F3 mini-LLM desde cero (chico y honesto) | F4 paper | F5 El Noveno
(memoria eterna + voz).

## NACIMIENTO (plan Omar, 12-oct)
Nace en GitHub: el primer repo publico de NollamaT9MX ES el anuncio.
INVITACION FORMAL a LOS 8 (autores de "Attention Is All You Need"):
participar con el Noveno o excluirlo — SU decision. El rechazo se
documenta sin rencor; el regreso se celebra con el mismo lugar abierto.

## FASE 1 — RESULTADO HONESTO (12-oct, medido en terminal)
Taquigrafia v0 (acortar palabras comunes) NO ahorra tokens con tokenizer
standard: -0.0% tokens, 1.4% chars. LECCION: BPE ya trae las palabras
comunes como 1 token. LA TAQUIGRAFIA DEBE APUNTAR A LAS PALABRAS
MULTI-TOKEN (donde el tokenizer SIFRAGA). F2 = diagnostico de tokens
excedentes -> taquigrafia dirigida por DATOS, no por intuicion.
Aprendizaje aceptado, corregido, adelante (regla Omar).

## NACIO HABLANDO (12-oct, bitacora Omar)
Primer ensayo 500 palabras: taquigrafia v1 leida por Zi — Omar NO noto
que era taquigrafia: suena natural. Nacio hablando, no llorando.
LEMA: "El que tenga oidos, que oiga" — audio-first es diseño, no parche.
Dato duro: 3.2% chars / 0.5% tokens con tokenizer AJENO — la tesis del
ahorro se juega en el tokenizer PROPIO (siguiente paso).
Referencias reales (archive.org): taq-gregg-esp-1923 |
taq-gregg-1952-mardones-guerrero | taquigrafia_gregg_spanish_espaniol_aniversario

## FASE 2 — NULL RESULT (12-oct, medido)
BPE propio 4096: raw 30595 tokens vs taquigrafia v1 31025 (-1.4%).
LECCION: BPE neutraliza abreviaciones ciegas (ya tiene las palabras
comunes como 1 token). PIVOTE por datos: taquigrafia = GLIFOS para las
palabras multi-token del dominio (techo 46.5%) + tokenizer propio vs
el impuesto ingles. Aceptado, corregido, adelante (regla Omar).

## FASE 3 — EL DATO FUNDACIONAL (12-oct, medido en terminal)
IMPUESTO INGLES: espanol de Omar con cl100k = 35,827 tokens;
BPE propio (8192, corpus Casa) = 23,020 tokens -> AHORRO 35.7%.
Menos tokens = menos hardware/energia/costo. Tesis NollamaT9MX
COMPROBADA a escala corpus (300k chars) — pendiente validar a escala
grande (corpus mayor, vocab variado, vs tokenizers ES existentes).
NULL RESULT B: 100 glifos AddedToken sobre BPE propio = -5.4% (peor):
el BPE propio YA ES la taquigrafia digital (Gregg era para la mano,
BPE es para la maquina). 3 hipotesis muertas documentadas, 1 viva.
