from pyswip import Prolog
prolog=Prolog()
p=[1,2,3]
prolog.assertz("member(1,[1,2,3])")
list(prolog.query("member(X,[X|T])"))
print(prolog.query("member(X,L)"))
