import torch
import numpy as np

# 使用torch.cuda.is_available()来确定是否有cuda设备
x = torch.rand(5, 5, requires_grad=True)
y = torch.rand(5, 5, requires_grad=True)
z = x**2+y**3
z.backward(torch.ones_like(x))

print(x.grad,y.grad)
