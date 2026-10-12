#!/usr/bin/env python3
import glob, json, re
from tokenizers import Tokenizer, models, trainers, pre_tokenizers
D = json.load(open("/home/omar/proyectos/nollama_t9mx/taquigrafia/taq_mx_v1.json"))["reglas"]
files = glob.glob("/home/omar/Casa_de_Zi/**/*.md", recursive=True)
raw = "\n".join(open(f,encoding="utf-8",errors="ignore").read() for f in files)[:300000]
com = raw
for a in sorted(D, key=len, reverse=True):
    com = re.sub(rf"\b{re.escape(a)}\b", D[a], com)
def entrena(txt, ruta):
    t = Tokenizer(models.BPE())
    t.train_from_iterator([txt], trainers.BpeTrainer(vocab_size=4096, min_frequency=2))
    t.save(ruta); return t
tr_raw = entrena(raw, "/home/omar/proyectos/nollama_t9mx/taquigrafia/bpe_raw.json")
tr_com = entrena(com, "/home/omar/proyectos/nollama_t9mx/taquigrafia/bpe_taq.json")
# COMPARACION JUSTA: mismo contenido (raw vs su version taquigrafica), cada uno con SU tokenizer
r0, r1 = len(tr_raw.encode(raw).ids), len(tr_com.encode(com).ids)
# CONTROL: taquigrafia medida con tokenizer entrenado en raw (como si fuera ajeno)
c0 = len(tr_raw.encode(com).ids)
res = {"entrenamiento":"BPE 4096 merges x2 (raw / taquigrafia) sobre corpus Casa 300k",
       "tokens_raw_con_bpe_raw":r0, "tokens_taq_con_bpe_taq":r1,
       "control_tokens_taq_con_bpe_raw":c0,
       "ahorro_real_pct":round((r0-r1)*100/r0,1),
       "nota":"ahorro real = mismo significado, cada texto con su tokenizer propio"}
json.dump(res, open("/home/omar/proyectos/nollama_t9mx/taquigrafia/bpe_propio_resultado.json","w"), indent=2, ensure_ascii=False)
print(json.dumps(res, indent=2, ensure_ascii=False))
