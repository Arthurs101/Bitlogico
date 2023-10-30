%crear las personas
% m: masculino , f:femenino
m(beto).
m(arturo).
m(luis).
m(arturoJR).
m(claudio).
m(donald).
m(diego).
m(mario).
m(josue).


f(sipriana).
f(roberta).
f(nubia).
f(daniela).
f(nehsi).
f(catalina).

%crear relaciones de progenitor p (padre,hijo)
p(beto,arturo).
p(beto,luis).
p(beto,catalina).

p(sipriana,arturo).
p(sipriana,luis).
p(sipriana,catalina).

p(roberta,nubia).

p(catalina,neshi).
p(catalina,daniela).

p(daniela,josue).

p(neshi,mario).

p(arturo,arturoJR).
p(arturo,claudio).
p(arturo,diego).
p(arturo,donald).

p(nubia,arturoJR).
p(nubia,claudio).
p(nubia,diego).
p(nubia,donald).

%papá , tiene qye tener paterninad y ser masculino (X padre, Y hijo ) 
father(X,Y):- p(X,Y) , m(X).

%mamá , tiene que tener paterninad y ser masculino (X padre, Y hijo ) 
mother(X,Y):- p(X,Y) , f(X).

%hermano , mismo padre y masculino (X persona, Y objetivo) y que no sean iguales
brother(X,Y):- p(Z,X) , p(Z,Y) , m(Y) , X \== Y.

%hermana , mismo padre y femenino (X persona, Y objetivo) y que no sean iguales
sister(X,Y):- p(Z,X) , p(Z,Y) , f(Y) , X \== Y.

%tio X persona , Y objetivo ; Y -> sea hermano de padre de X
uncle(X,Y):- p(Z,X) , brother(Z,Y).

%tia X persona , Y objetivo ; Y -> sea hermana de padre de X
aunt(X,Y):- p(Z,X) , sister(Z,Y).

%abuelo X persona , Y objetivo ; Y -> sea padre de padre de X (ya sea de la mamá o papá)
granddad(X,Y):- p(Z,X) , father(Y,Z).

%abuelo X persona , Y objetivo ; Y -> sea madre de padre de X (ya sea de la mamá o papá)
grandmother(X,Y):- p(Z,X) , mother(Y,Z).

%sobrino X persona , Y objetivo ; Y -> sea hijo de primo/prima de X (ya sea de la mamá o papá)
nephew(X,Y):- (uncle(X,Z), p(Z,W),p(W,Y) , m(Y)) ; (aunt(X,Z) , p(Z,W),p(W,Y) , m(Y)).

%sobrina X persona , Y objetivo ; Y -> sea hija de primo/prima de X (ya sea de la mamá o papá)
niece(X,Y):- (uncle(X,Z), p(Z,W),p(W,Y) , f(Y)) ; (aunt(X,Z) , p(Z,W),p(W,Y) , f(Y)).