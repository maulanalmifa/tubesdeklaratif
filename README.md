# tubesdeklaratif
Combining Prolog with Python

<h4>Instalasi</h4>
1. Pertama, pastikan anda sudah menginstall SWI-Prolog dan Python dengan arsitektur yang sama (64bit/32bit)

2. Buka CMD dan pastikan anda berada di direktori C:\>

3. Ketik ```python3 -m venv pyswip_env```
dan ```pyswip_env\Scripts\activate```

4. Pastikan command `swipl` sudah masuk PATH

5. Install PySwip dengan cara ketik di CMD ```python -m pip install pyswip```

6. Lakukan test menggunakan kode berikut ini

```
from pyswip import Prolog
prolog = Prolog()
prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")
list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
for soln in prolog.query("father(X,Y)"):
print(soln["X"], "is the father of", soln["Y"])
```
