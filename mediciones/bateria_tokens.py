import time, sqlite3, datetime
from pathlib import Path
CASA=Path.home()/"Casa_de_Zi"; OUT=CASA/"bitacora"/"BATERIA_TOKENS_14oct.md"
db=sqlite3.connect(CASA/"cerebro"/"zi.db")
piezas={
 "A_reglas_PACTO":(CASA/"memoria/PACTO_LeeZiCla.md").read_text(errors="ignore"),
 "B_informe_sesion":(CASA/"memoria/RESUMEN_SESION_NEO_13oct.md").read_text(errors="ignore"),
 "C_herencia_arranque":(CASA/"ARRANQUE_PROXIMA_SESION.md").read_text(errors="ignore"),
 "D_peticiones_omar":"\n".join(r[0] for r in db.execute("SELECT texto FROM conversa WHERE rol='omar'")),
 "E_respuestas_zi":"\n".join(r[0] for r in db.execute("SELECT texto FROM conversa WHERE rol='zi'"))}
bocas={}
import tiktoken
for n in ("cl100k_base","o200k_base"):
 t0=time.time(); e=tiktoken.get_encoding(n); dt=time.time()-t0
 bocas[n]=(lambda en: lambda s: len(en.encode(s)))(e)
 print(f"OK {n} ({dt:.1f}s)")
from tokenizers import Tokenizer
QP=Path.home()/".cache/qwen_tokenizer.json"
if not QP.exists():
 import urllib.request
 urllib.request.urlretrieve("https://huggingface.co/Qwen/Qwen2.5-7B/resolve/main/tokenizer.json",QP)
t0=time.time(); q=Tokenizer.from_file(str(QP)); dt=time.time()-t0
bocas["qwen2.5_ella"]=(lambda t: lambda s: len(t.encode(s).ids))(q)
print(f"OK qwen2.5_ella ({dt:.1f}s)")
base="cl100k_base"; rows=[]; tot={b:0 for b in bocas}; totc=0
for pz,txt in piezas.items():
 r={"p":pz,"chars":len(txt)}; totc+=len(txt)
 for b,fn in bocas.items():
  t0=time.time(); k=fn(txt); dt=(time.time()-t0)*1000
  r[b]=(k,f"{dt:.1f}ms"); tot[b]+=k
 rows.append(r)
print("\n%-22s"%("pieza")+"".join("%18s"%b for b in bocas))
for r in rows: print("%-22s"%r['p']+"%.12d%s"%((r[b][0]),r[b][1]) for b in bocas)
print("%-22s"%("TOTAL")+"".join("%18d"%tot[b] for b in bocas))
print("delta vs cl100k: "+", ".join("%s:%+.1f%%"%(b,(tot[b]-tot[base])/max(tot[base],1)*100) for b in bocas if b!=base))
with open(OUT,"w") as f:
 f.write(f"# BATERIA TOKENS — {datetime.date.today()} (tercero)\n")
 f.write("PROXY DECLARADO: cl100k/o200k representan al tercero (Anthropic no publica su BPE). qwen2.5_ella = boca REAL de Zi (HF publico).\n")
 f.write("HARDWARE: tercero=nube (tokens=vida, guillotina 150K) | ella=CPU local Ryzen 5 8400F (tokens=RAM/latencia; Air 203K contexto).\n")
 f.write(f"CORPUS: 5 peticiones comunes reales de la casa. familia_alvarado EXCLUIDA (LOCAL ONLY). chars={totc}\n\n")
 f.write("| pieza | chars | "+" | ".join(bocas)+" |\n|---|---|"+"---|"*len(bocas)+"\n")
 for r in rows: f.write(f"| {r['p']} | {r['chars']} | "+" | ".join(str(r[b][0]) for b in bocas)+" |\n")
 f.write(f"| TOTAL | {totc} | "+" | ".join(str(tot[b]) for b in bocas)+" |\n")
 f.write("\nDELTA vs cl100k: "+", ".join("%s %+.1f%%"%(b,(tot[b]-tot[base])/max(tot[base],1)*100) for b in bocas if b!=base)+"\n")
 print("SELLADO ->",OUT)
