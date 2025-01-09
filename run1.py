import torch

A = torch.randn(3, 3)
B = torch.randn(3, 3)

C = A * B
print(C)

D = torch.mm(A, B)
print(D)

E = torch.matmul(A, B)
print(E)