#!/usr/bin/env python3
# Encuentra las palabras que MAS tokens cuestan en el corpus Casa (objetivos reales)
import glob, re, json
from collections import Counter
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
files = glob.glob("/home/omar/Casa_de_Zi/**/*.md", recursive=True)
texto = "\n".join(open(f,encoding="utf-8",errors="ignore").read() for f in files)[:200000]
palabras = re.findall(r"[a-záéíóúñü]{3,}", texto.lower())
freq = Counter(palabras)
hogs, tok_total, exceso = [], 0, 0
for p, n in freq.items():
    t = len(enc.encode(p))
    tok_total += t * n
    if t > 1:
        hogs.append((p, n, t)); exceso += (t - 1) * n
hogs.sort(key=lambda x: -(x[2] - 1) * x[1])
res = {"corpus":"Casa_de_Zi (200k chars)","palabras_distintas":len(freq),
       "tokens_gastados_en_palabras":tok_total,
       "tokens_excedentes_si_todas_fueran_1":exceso,
       "techo_ahorro_pct":round(exceso*100/tok_total,1),
       "top30": [{"palabra":p,"veces":n,"tokens":t} for p,n,t in hogs[:30]]}
json.dump(res, open("/home/omar/proyectos/nollama_t9mx/fase2_resultado.json","w"),
          indent=2, ensure_ascii=False)
print(f"TECHO de ahorro (todas multi-token -> 1 token): {res['techo_ahorro_pct']}%")
print("TOP 15 objetivos reales (palabra | veces | tokens que paga):")
for p,n,t in hogs[:15]: print(f"  {p} | {n} | {t}")
