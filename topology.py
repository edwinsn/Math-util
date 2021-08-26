from itertools import combinations


def powerset(s):
    power=[]
    for i in range(len(s)+1):
      power+=[frozenset(s) for s in combinations(s, i)]
    return power

def nTop(n):
  parts=powerset(range(n))
  candidates=powerset(parts)

#primera condición
  firstCondition=[]

  for candidate in candidates:
    if (set() in candidate and set(range(n)) in candidate ):
      firstCondition.append(candidate)
  print("Primera condición \n{}\n".format(firstCondition))

  
#segunda condición

  secondCondition=[]

  for candidate in firstCondition:
    noConditiontwo=False
    toIntersect=powerset(candidate)[1:]
    toIntersect=[iset for iset in toIntersect if len(iset)>1]
    #1print("...")
    #1print(toIntersect)
    for iset in toIntersect:
      for unit,i in zip(iset,range(len(iset))):
        if i==0:
          intersection=unit
        else:
          intersection&=unit
      if not intersection in candidate:
        noConditiontwo=True
      #1print(intersection)
    if not noConditiontwo:
      secondCondition.append(candidate)
  print("Segunda condición\n{}\n".format(secondCondition))

#tercera condicion

  thirdCondition=[]

  for candidate in secondCondition:
    noConditionthree=False
    toJoin=powerset(candidate)[1:]
    toJoin=[iset for iset in toJoin if len(iset)>1]
    #print("...")
    #print(toJoin)
    for iset in toJoin:
      for unit,i in zip(iset,range(len(iset))):
        if i==0:
          union=unit
        else:
          union|=unit
      if not union in candidate:
        noConditionthree=True
      #print(union)
    if not noConditionthree:
      thirdCondition.append(candidate)
  print("Tercera condición\n{}\n".format(thirdCondition))
  print("El numero de topologias en un conjunto de {} elementos es {}".format(n,len(thirdCondition)))

nTop(3)
