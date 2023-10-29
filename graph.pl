% Vértices
vert(a).
vert(b).
vert(c).
vert(d).


% Aristas
ari(a, b).
ari(a, c).
ari(a, d).
ari(c, d).

%crear el camino
%un camino d->t implica una arista que los conecta
%y la lista resultante es D,T
path(D,T,[D,T]) :- ari(D,T).
%buscar camino
%para X -> ..... -> Y, tiene que haber conección con un intermediario Z
%es decir de X -> Z , y un camino desde Z a Y 
%X es el inicio del camino o es parte del camino (TRACK)
path(X,Y,[X|TRACK]) :- ari(X,Z), path(Z,Y,TRACK).