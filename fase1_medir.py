#!/usr/bin/env python3
# NollamaT9MX Fase 1: tokens con tokenizer standard ANTES y DESPUES de taquigrafia
import glob, json, re, sys
try:
    import tiktoken
except ImportError:
    print("FALTA tiktoken"); sys.exit(1)
files = glob.glob("/home/omar/Casa_de_Zi/**/*.md", recursive=True)
texto = "\n".join(open(f,encoding="utf-8",errors="ignore").read() for f in files)[:200000]
if not texto.strip(): print("CORPUS VACIO"); sys.exit(1)
TAQ = [("porque","pq"),("pero","pe"),("para","pa"),("cuando","cn"),("donde","dn"),
       ("tambien","tb"),("hasta","hs"),("desde","ds"),("hacia","ha"),("que","q"),
       ("por","x"),("con","cn"),("los","ls"),("las","ls"),("del","dl"),
       ("una","1a"),("uno","1o"),("como","cm"),("mas","+"),("menos","-")]
compr = texto
for a,b in TAQ:
    compr = re.sub(rf"\b{re.escape(a)}\b", b, compr)
enc = tiktoken.get_encoding("cl100k_base")
t0, t1 = len(enc.encode(texto)), len(enc.encode(compr))
res = {"proyecto":"NollamaT9MX-fase1","corpus":"Casa_de_Zi/*.md (200k chars)",
       "archivos":len(files),"tokens_antes":t0,"tokens_despues":t1,
       "ahorro_tokens_pct":round((t0-t1)*100/t0,1),
       "chars_antes":len(texto),"chars_despues":len(compr),
       "ahorro_chars_pct":round((len(texto)-len(compr))*100/len(texto),1),
       "tokenizer":"cl100k_base (hecho para ingles) — F2 traera BPE propio"}
json.dump(res, open("/home/omar/proyectos/nollama_t9mx/fase1_resultado.json","w"),
          indent=2, ensure_ascii=False)
print(json.dumps(res, indent=2, ensure_ascii=False))
