clc
clear
syms x1 x2 x3 x4 real
syms T0 T1 T2 T3 real
x1_dot = x2
x2_dot = (-T0 - T1 + T2 + T3)*0.0566/2/1.43e-5
x3_dot = x4
x4_dot = (-T0 + T1 + T2 - T3)*0.0566/2/1.43e-5
y = [x1]
A = jacobian([x1_dot,x2_dot,x3_dot,x4_dot],[x1,x2,x3,x4])
B = jacobian([x1_dot,x2_dot,x3_dot,x4_dot],[T0, T1 ,T2 ,T3])
C = jacobian([y],[x1,x2,x3,x4])
D = jacobian([y],[T0 ,T1, T2, T3])
A = double(A)
B = double(B)
C = double(C)
D = double(D)'
control_matrix = [B,A*B,A*A*B,A*A*A*B];
% tol = max(size(control_matrix))*eps(norm(control_matrix))
M3Rank_Controllability = rank([control_matrix])

K_non = place(A, B, [-12+2i -12-2i -21+5i  -21-5i])
save('K.out', 'K_non', '-ascii');
%% motor 1
A_cl = A - B*K_non;
G_tf_closed = tf(ss(A_cl, B, C, 0))
G0 = (C*(-A_cl).^-1)*B;
N_x = G0.^-1
