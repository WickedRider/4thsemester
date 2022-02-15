A = [1,2,3,4;5,6,7,8];
B = randi([2,9], size(A));
save("teste1", "A", "B");

%clear("A");
%load teste1.mat;


C1 = [1 2;3 4];
C2 = [5 6;7 8];
Ccil = cat(2, C1, C2);

%1.8 -> primeira linha de A e ultima linha de B
Cp = [A(1,:); B(end,:)];
Cp;

%1.9 -> Soma A e B
clear("C1");
C1 = A+B;

%1.9.3 -> Multiplicacao de A pela transposta de B
C3 = A*B';

%1.9.4 -> Multiplicacao elemento a elemento
C4 = A.*B;

%1.9.5 -> Divisao a direita de A e B
C5 = A/B;
%para quadradas -> A/B = A*inv(B)

%1.9.6 -> Divisao a direita elemento a elemento
C6 = A./B;

%C3^2
%C3.^2
%


%2 sin(2.pi.t) + sin(pi.t)
%2.1 -> Vetor T : permite valores [-10, 10], assume valores de 0.01
%correr uma linha -> selecionar linha + F7

t=-10:0.01:10;
n=numel(t);

disp("A dimensao do vetor tempo e: ") %Print

disp(["Dimensao", num2str(n)])

%2.2 -> Graficamente
f = sin(2*pi*t) + sin(pi*t);

plot(t,f), xlabel("t [s]"), ylabel("f(t)"), title("f(t) = sin(2*pi*t) + sin(pi*t)"),

%variavel simbolica
syms tsym
ft = sin(2*pi*tsym) + sin(pi*tsym);
f1 = subs(ft,tsym,5:0.01:5);
plot(-5:0.01:5, f1), xlabel("t [s]"), ylabel("f(t)"), title("f(t) = sin(2*pi*t) + sin(pi*t)"),

%4 -> f(x,y) = sin(xy) + cos(x)
x = -4:0.05:4;
y=x;
[X,Y]=meshgrid(x,y);

Z=sin(X.*Y)+cos(X);
figure; mesh(X,Y,Z);

%{
A funcao mesh faz um grafico dos valores de Z definidos pela altura sobre
o plano X-Y 
Representa os contornos em cores sem preenchimento
%}

xlabel("X"), ylabel("Y"), zlabel("f(x,y)"), title("Grafico de f(x,y)")

%Calculo simbolico
syms X Y
Z=sin(X.*Y)+cos(X);

figure; fmesh(Z, [-4, 4]);
%{
A funcao fmesh grafica a funcao Z sobre o intervalo [min, max]
Nao e necessaria a definicao previa de XY nem o calculo dos valores em Z
%}
xlabel("X"), ylabel("Y"), zlabel("Z"), title("Grafico de f(x,y)")

%5 -> Coeficientes de grau 2 (polinomios)

y1 = [0 0.7 2.4 3.1 4.2 4.8 5.7 5.9 6.2 6.3 6.4];
x1 = 0:10;

%a funcao polyfit(x,y,n) encontra os coeficientes de um polinomio de
% grau n que melhor ajusta os dados em y pelo metodo dos min quadrados
p=polyfit(x1, y1, 2);

% a funcao polyval(p,x) avalia o polinomio p em cada ponto de x
x2 = 0:0.2:10;
y2 = polyval(p,x2);
figure; plot(x1,y1,"*r",x2,y2,"-b"), legend ("dados originais", "ajuste Polinomial", "Location", "northwest")

% 6 -> Factorial nao recursivo
function fato = fatorial1(n)

fato = 1;
for i=2:n
    fato=i*fato;

end
end
