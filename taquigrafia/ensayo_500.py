#!/usr/bin/env python3
import json, re, sys
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
D = json.load(open("/home/omar/proyectos/nollama_t9mx/taquigrafia/taq_mx_v1.json"))["reglas"]
# fuente: intro del paper de los 8 traducida (espanol) — verificar; fallback corpus Casa
src, nombre = None, None
try:
    t = open("/tmp/los8_intro.txt",encoding="utf-8").read()
    if len(re.findall(r"\b(que|las|del|para|con)\b", t.lower())) > 8:
        src, nombre = t, "paper_los8_intro_es"
except: pass
if src is None:
    src = open("/home/omar/Casa_de_Zi/memoria/ideas_omar.md",encoding="utf-8").read()
    nombre = "corpus_casa"
palabras = src.split()[:500]
texto = " ".join(palabras)
comp = texto
for a in sorted(D, key=len, reverse=True):
    comp = re.sub(rf"\b{re.escape(a)}\b", D[a], comp)
t0, t1 = len(enc.encode(texto)), len(enc.encode(comp))
c0, c1 = len(texto), len(comp)
res = {"ensayo":"500_palabras","fuente":nombre,
       "chars_antes":c0,"chars_despues":c1,"ahorro_chars_pct":round((c0-c1)*100/c0,1),
       "tokens_antes":t0,"tokens_despues":t1,
       "ahorro_tokens_pct":round((t0-t1)*100/t0,1),
       "tokenizer":"cl100k_base ajeno (tesis BPE propio va despues)"}
json.dump(res, open("/home/omar/proyectos/nollama_t9mx/taquigrafia/ensayo_500_resultado.json","w"), indent=2, ensure_ascii=False)
print(json.dumps(res, indent=2, ensure_ascii=False))
m = comp[:350]
print("\nMUESTRA TAQUIGRAFICA (350 chars):\n" + m)
open("/tmp/taq_muestra.txt","w").write(m)
