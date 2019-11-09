import sympy as sym
import numpy as np

sym.init_printing

Pi = sym.S.Pi # 円周率
E = sym.S.Exp1 # 自然対数の底
I = sym.S.ImaginaryUnit # 虚数単位
oo = sym.oo # 無限大

(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

O = np.array(list(map(int, input("Oベクトルの成分を入力してください\n").split(' '))))
A = np.array(list(map(int, input("Aベクトルの成分を入力してください\n").split(' '))))
B = np.array(list(map(int, input("Bベクトルの成分を入力してください\n").split(' '))))

F = eval((input("積分する関数を入力してください\nf(x,y,z) = ")))

R = (A-O)*t

DR = np.array([float(sym.diff(R[0], t)), float(sym.diff(R[1], t)), float(sym.diff(R[2], t))])
DR_length = np.linalg.norm(DR)

X = R[0]
Y = R[1]
Z = R[2]

result_OA = sym.integrate(F.subs([(x, X), (y, Y), (z, Z)])*DR_length, (t, 0, 1))

print("経路OAでの積分結果は",result_OA,"です。")

R1 = (B - O) * t
R2 = (A - B) * t

DR1 = np.array([float(sym.diff(R1[0], t)), float(sym.diff(R1[1], t)), float(sym.diff(R1[2], t))])
DR1_length = np.linalg.norm(DR1)

X1 = R1[0]
Y1 = R1[1]
Z1 = R1[2]

result_OB = sym.integrate(F.subs([(x, X1), (y, Y1), (z, Z1)])*DR1_length, (t, 0, 1))

DR2 = np.array([float(sym.diff(R2[0], t)), float(sym.diff(R2[1], t)), float(sym.diff(R2[2], t))])
DR2_length = np.linalg.norm(DR2)

X2 = 1
Y2 = R2[1]
Z2 = R2[2]

result_BA = sym.integrate(F.subs([(x, X2), (y, Y2), (z, Z2)])*DR2_length, (t, 0, 1))

result_OBA = result_OB + result_BA

print("経路OBAでの積分結果は",result_OBA,"です。")
