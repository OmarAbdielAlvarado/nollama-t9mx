#!/usr/bin/env python3
# FASE 3: A) impuesto ingles  B) taquigrafia de datos (glifos = palabras caras)
import glob, json, re
from collections import Counter
from tokenizers import Tokenizer, models, trainers, AddedToken
import tiktoken
files = glob.glob("/home/omar/Casa_de_Zi/**/*.md", recursive=True)
raw = "\n".join(open(f,encoding="utf-8",errors="ignore").read() for f in files)[:300000]
enc_en = tiktoken.get_encoding("cl100k_base")
tok_cl = len(enc_en.encode(raw))
t_propio = Tokenizer(models.BPE())
t_propio.train_from_iterator([raw], trainers.BpeTrainer(vocab_size=8192, min_frequency=2))
tok_propio = len(t_propio.encode(raw).ids)
palabras = re.findall(r"[a-záéíóúñü]{3,}", raw.lower())
freq = Counter(palabras)
hogs = [(p,n,len(enc_en.encode(p))) for p,n in freq.items() if len(enc_en.encode(p))>1]
hogs.sort(key=lambda x: -(x[2]-1)*x[1])
top = [p for p,n,t in hogs[:100]]
t_dir = Tokenizer(models.BPE())
t_dir.train_from_iterator([raw], trainers.BpeTrainer(vocab_size=8192, min_frequency=2))
t_dir.add_tokens([AddedToken(p, single_word=True) for p in top])
tok_dir = len(t_dir.encode(raw).ids)
res = {"corpus":"Casa_de_Zi 300k chars",
 "A_impuesto_ingles":{"tokens_cl100k":tok_cl,"tokens_bpe_propio":tok_propio,
   "ahorro_pct":impuesto if (impuesto:=round((tok_cl-tok_propio)*100/tok_cl,1)) else 0,
   "nota":"lo que paga el espanol por un tokenizer hecho para ingles"},
 "B_taquigrafia_de_datos":{"glifos":len(top),"tokens_propio":tok_propio,
   "tokens_con_glifos":tok_dir,
   "ahorro_adicional_pct":round((tok_propio-tok_dir)*100/tok_propio,1),
   "primeros10":top[:10]},
 "lectura":"glifos = taquigrafia Gregg digital: 1 trazo por palabra cara"}
json.dump(res, open("/home/omar/proyectos/nollama_t9mx/taquigrafia/fase3_resultado.json","w"), indent=2, ensure_ascii=False)
print(json.dumps(res, indent=2, ensure_ascii=False))
