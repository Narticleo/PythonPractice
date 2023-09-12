# noise scheduler
import torch
import torch.nn.functional as F
device = "cuda" if torch.cuda.is_available() else "cpu"
def LinearBetaScheduler(timesteps = 500, beta_start = 0.0001, beta_end = 0.02):
    beta = torch.linspace(beta_start, beta_end, timesteps)
    alpha = 1 - beta
    alpha_hat = torch.cumprod(alpha, dim = 0)
    alpha_hat_sqrt = alpha_hat**0.5
    alpha_hat_reci = 1 / alpha_hat
    return beta, alpha, alpha_hat, alpha_hat_sqrt, alpha_hat_reci

def GetIndex(vals, t, x_shape):
    batch_size = t.shape[0]
    out = vals.gather(-1, t.cpu())
    return out.reshape(batch_size, *((1,) * (len(x_shape) - 1))).to(device)

def FowardDiffusionSample(x0, t, device = 'cpu'):
    noise = torch.randn_like(x0)
    alpha_hat_sqrt_t = GetIndex(alpha_hat_sqrt, t, x0.shape)
    alpha_hat_t = GetIndex(alpha_hat, t, x0.shape)
    return alpha_hat_sqrt_t.to(device)*x0.to(device) \
            + ((1 - alpha_hat_t)**0.5).to(device)*noise.to(device), noise.to(device)


beta, alpha, alpha_hat, alpha_hat_sqrt, alpha_hat_reci = LinearBetaScheduler()

