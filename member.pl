members(X,[X|_]).
members(X,[X|L]):- member(X,L).

