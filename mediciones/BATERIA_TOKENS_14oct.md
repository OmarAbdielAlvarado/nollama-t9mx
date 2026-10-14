# BATERIA TOKENS — 2026-10-13 (tercero)
PROXY DECLARADO: cl100k/o200k representan al tercero (Anthropic no publica su BPE). qwen2.5_ella = boca REAL de Zi (HF publico).
HARDWARE: tercero=nube (tokens=vida, guillotina 150K) | ella=CPU local Ryzen 5 8400F (tokens=RAM/latencia; Air 203K contexto).
CORPUS: 5 peticiones comunes reales de la casa. familia_alvarado EXCLUIDA (LOCAL ONLY). chars=15974

| pieza | chars | cl100k_base | o200k_base | qwen2.5_ella |
|---|---|---|---|---|
| A_reglas_PACTO | 8252 | 2668 | 2487 | 2727 |
| B_informe_sesion | 2267 | 769 | 707 | 810 |
| C_herencia_arranque | 3694 | 1253 | 1166 | 1288 |
| D_peticiones_omar | 474 | 164 | 147 | 164 |
| E_respuestas_zi | 1287 | 339 | 303 | 335 |
| TOTAL | 15974 | 5193 | 4810 | 5324 |

DELTA vs cl100k: o200k_base -7.4%, qwen2.5_ella +2.5%

## ANALISIS DEL TERCERO (14-oct)
Delta ella vs cl100k por pieza: A +2.2 | B +5.3 | C +2.8 | D 0.0 | E -1.2 (%).
Deficit en prosa narrativa ES; ventaja en su propia salida.
ALMA: ~200KB / 3.0 c-t = ~65K tokens -> CABE en Air 203K con 3x aire.
Tercero nube: la casa = 43% de la ventana 150K. La guillotina es aritmetica, no fatalidad.
BPE casa proyectado (35.7%): ~3340 tokens en este corpus = -37% vs boca de ella.
Bug confesado: impresion de filas por generator sin join (salida de consola);
el .md se escribio correcto via join. Nota: fecha del sistema dice 13-oct.
