import json, subprocess, re, os, unicodedata, time
env=open(os.path.expanduser("~/proyectos/QSoy2/docker/.env")).read()
pw=re.search(r"CLICKHOUSE_PASSWORD\s*=\s*(.+)",env).group(1).strip().strip('"\'')
def ch(q,timeout=600):
 r=subprocess.run(["docker","exec","qsoy2_clickhouse","clickhouse-client","--host","127.0.0.1","--password",pw,"--query",q],capture_output=True,text=True,timeout=timeout)
 if r.returncode!=0: raise RuntimeError(r.stderr.strip()[:120])
 return r.stdout.strip()
for col in ("nombre","paterno","materno"):
 print(f"DISTINCT {col} (real):", ch(f"SELECT uniqExact({col}) FROM qsoy.votantes_norm"))
T9={'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
def limpiar(w):
 w=unicodedata.normalize("NFD",w.lower())
 return "".join(c for c in w if not unicodedata.combining(c))
def t9(w): return "".join(T9[c] for c in w if c in T9)
idx={}; entradas=0
for col in ("nombre","paterno","materno"):
 out=ch(f"SELECT {col}, count() FROM qsoy.votantes_norm GROUP BY {col} ORDER BY count() DESC LIMIT 20000 FORMAT TSV")
 for ln in out.splitlines():
  if not ln.strip(): continue
  w,c=ln.rsplit("\t",1); w=limpiar(w.strip())
  if not re.fullmatch(r"[a-zñü]{2,}",w): continue
  s=t9(w)
  if len(s)<2: continue
  idx.setdefault(s,[]).append((int(c),w)); entradas+=1
for s in idx: idx[s].sort(key=lambda x:-x[0])
seqs=len(idx); cands=[len(v) for v in idx.values()]
out=ch("SELECT nombre, count() FROM qsoy.votantes_norm GROUP BY nombre ORDER BY count() DESC LIMIT 1000 FORMAT TSV")
top1=0; tested=0
for ln in out.splitlines():
 if not ln.strip(): continue
 w,_=ln.rsplit("\t",1); w=limpiar(w.strip()); s=t9(w)
 if s in idx and idx[s]:
  tested+=1
  if idx[s][0][1]==w: top1+=1
sample=list(idx.keys())[:10000]; t0=time.perf_counter_ns()
for s in sample: idx.get(s)
dt=(time.perf_counter_ns()-t0)/max(len(sample),1)
res={"proyecto":"nollama_t9mx-ronda2-PADRON-REAL","fuente":"votantes_norm 88M LOCAL — indice LOCAL ONLY, a bitacora solo metricas",
 "entradas":entradas,"secuencias_t9":seqs,"prom_candidatos":round(sum(cands)/seqs,2),
 "max_candidatos":max(cands),"sin_colision":sum(1 for x in cands if x==1),
 "pct_sin_colision":round(sum(1 for x in cands if x==1)*100/seqs,1),
 "top1_top1000":f"{top1}/{tested} ({top1*100/max(tested,1):.1f}%)",
 "latencia_ns":round(dt,1),
 "tam_idx_kb":round(len(json.dumps({s:[w for _,w in v][:8] for s,v in idx.items()}))/1024,1)}
print(json.dumps(res,indent=2,ensure_ascii=False))
open(os.path.expanduser("~/Casa_de_Zi/bitacora/T9_R2_REAL_resultado.json"),"w").write(json.dumps(res,indent=2,ensure_ascii=False))
