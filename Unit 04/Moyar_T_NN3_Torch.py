import torch
import random
import re
import sys

ins = torch.tensor([[random.uniform(-1.7,1.7),random.uniform(-1.7,1.7)] for i in range(20000)])
expected = torch.tensor([[float((tpl[0]**2 + tpl[1]**2) < 1)] for tpl in ins])
nodeCts = [len(ins[0]), 8, 5, 1]
netSpec = [torch.nn.Sigmoid() if i%2 else torch.nn.Linear(nodeCts[i//2], nodeCts[1+i//2],bias=i<1) for i in range(2*len(nodeCts)-2)]

mynn = torch.nn.Sequential(*netSpec, torch.nn.Linear(1,1,bias=False))
criterion = torch.nn.MSELoss()

optimizer = torch.optim.SGD(mynn.parameters(), lr=1)
for epoch in range(200000):
    y_pred = mynn(ins)
    loss = criterion(y_pred, expected)
    if not epoch%50 or epoch<10:
        print('epoch: ', epoch,' loss: ', loss.item())
    if loss.item() < 0.004:
       optimizer.lr = 0.01
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


nodeCts[0] += 1
print("Layer counts: " + str(nodeCts)[:-1] + ", 1]")
print("Weights: ")
toreturn = []
for k,v in mynn.state_dict().items():
   if "bias" not in k:
      if len(toreturn) != 0:
         print(toreturn)
      toreturn = []
      toreturn += v.tolist()
   else:
      v = v.tolist()
      for x in range(len(toreturn)):
         toreturn[x].append(v[x])
print(toreturn)
print("[1]")
