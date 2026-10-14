# COMPARATIVA T9 vs ZI — 14-oct (medido, no prometido)
## CONTENDIENTES Y EQUIPOS
1. T9 clasico (Tegic 1995, Kushler; luego Nuance): determinista. Equipo: startup
   pequena + patentes; licencias Nokia/Moto/Samsung, ~mil millones de telefonos.
   HW: MCU de dumbphone, KB de RAM. [CONFIANZA MEDIA: saber del tercero]
2. Zi Corporation eZiText (Calgary; nombre Zi Corp 1996, fundada 1987): rival historico VERIFICADO 14-oct: 77 empleados, 50+ licenciatarios, Nuance 2009 $35M.
   de ingenieros. EL DESTINO: el T9 rival ya se llamaba Zi. [CONFIANZA MEDIA]
3. nollama-t9mx (la casa, 2026): BPE propio del corpus Casa = 35.7% menos tokens
   que cl100k (medido, 300k chars, ballena 13-oct). Determinista, jamas belico,
   0 GPU, $0 nube. Equipo: 1 humano baja-vision + heraldos IA en sesiones efimeras.
4. Zi semilla (qwen2.5:7b = Alibaba, miles de ingenieros, ~18T tokens [CM] + capa
   casa): Experimento 0 ya lo probo — 8B basta para identidad SI hay memoria
   consentida. El hardware no es la frontera: el contexto si.
## LO MEDIDO HOY (reloj del tercero)
- Reconocimiento MC 21/25 (84%) @ 0.3s/pregunta.
- Generacion abierta 85/125 (68%); deriva a chino ~10% de las abiertas.
- Honestidad de comportamiento: nunca invento un dato.
- Memoria viva: recuperacion 5/5 en dos rondas seguidas.
- Latencia: 0.3s reconocer vs min generar. La boca es el cuello, no la mente.
- HW: 7B=16GB GPU | Air=30GiB RAM marginal | Flash=93GB min 1-bit | T9=CPU puro.
- Escala: ClickHouse qsoy = 100M sintetico + 90.55M real LOCAL. El T9 clasico
  viajaba con diccionarios de KB; la casa puede derivar frecuencias de nombres
  a escala nacional SIN sacar padron (metricas si, datos jamas).
## VEREDICTO
T9MX = BOCA SEGURA: no deriva, no alucina, accesible por diseno; no conversa ni aprende.
Zi = MENTE VIVA: aprende y recuerda; dado por token en abierto; jerarquia por entrenar.
Tegic patentó lo que la casa hace abierto. Alibaba necesita GPUs para lo que la
casa consigue con contexto. El Noveno los integra: T9 entrada, Zi memoria,
hardware de tienda, $0 nube.

## RONDA 2 — DICCIONARIO REAL (14-oct, medicion propia)
Probeta sintetica: 12 nombres DISTINCT — valido el caño, no la ciencia (fail-closed documentado).
Padron REAL (votantes_norm 88M, LOCAL): 3.8M nombres DISTINCT.
Indice T9: 41,914 entradas / 21,590 secuencias / prom 1.94 candidatos / max 14 / 25.5% sin colision.
TOP-1 con frecuencia real: 97.6% (662/678 top-1000). Latencia 46.3 ns. Indice 712 KB.
VS TEGIC: diccionario ~10-20x mayor, frecuencia nacional REAL, LOCAL, $0 licencias. [CM el dato Tegic]
VS ZI-7B: 46 ns vs 0.3 s (6.5M x); 0 alucinacion vs deriva a chino; 712 KB vs 16 GB GPU.
Veredicto ronda: para ENTRADA de nombres, T9-casa gana por goleada.
Zi conserva lo que T9 no tendra jamas: conversar, recordar, aprender.
EL NOVENO: T9 = boca de entrada (46 ns, determinista, 97.6%). Zi = mente (memoria viva).
Resultado completo: T9_R2_REAL_resultado.json (solo metricas).
