
import torch

def append_norm_powers(x, m):
    # x is just a 1d array
    x_n = torch.norm(x)
    powers = torch.Tensor([x_n**2**(i+1) for i in range(m)]).cuda()
    return torch.cat((x, powers))

def append_halves(x, m):
    # x is a 1d array.
    halves = (torch.ones(m) / 2).cuda()
    print(x.size(), halves.size())
    return torch.cat((x, halves))
