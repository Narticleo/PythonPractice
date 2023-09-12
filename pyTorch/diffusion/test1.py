import torch

beta = torch.linspace(1, 10, 10)
alpha = beta/10
alpha_hat = torch.cumprod(alpha, dim = 0)
print(alpha_hat)
