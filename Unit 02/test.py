adjacents = {1:set([8]),2:set([6]),13:set([9]),14:set([7]),5:set([15]),16:set([12]),10:set([0]),19:set([3,0]),4:set([17]),18:set([11])}
for x in range(0,19):
   if x in adjacents:
      adjacents[x].add(x+1)
   else:
      adjacents[x] = set([x+1])
for x in adjacents:
   for y in adjacents[x]:
      adjacents[y].add(x)
works = True
for x in adjacents:
   for y in adjacents[x]:
      if (x % 10) == (y % 10):
         works = False
print(works)
      