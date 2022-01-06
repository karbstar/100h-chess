#!python3

def bishop(pla):
  """
  input:
  str square: the coordinate of the square that the bishop is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the bishop can move to:
  """
  poss=[]
  posi=[]
  for i in range(8):
    i=i+1
    sen=f"a{i}"
    inr=f"1 {i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"b{i}"
    inr=f"2 {i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"c{i}"
    inr=f"3 {i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"d{i}"
    inr=f"4 {i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"e{i}"
    inr=f"5 {i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"f{i}"
    inr=f"6 {i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"g{i}"
    inr=f"7 {i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"h{i}"
    inr=f"8 {i}"
    poss.append(sen)
    posi.append(inr)

  ind=poss.index(pla)
  plar=posi[ind]
  bisx=int(plar[0])
  bisy=int(plar[2])
  ad=0
  con=True
  movsi=[]
  while con==True:
    ad=ad+1
    bisxn=bisx+ad
    bisyn=bisy+ad
    mv=f"{bisxn} {bisyn}"
    movsi.append(mv)
    if bisxn==8 or bisyn==8:
      break
  inds=[]
  movss=[]
  n=0
  lis=[ ]
  for i in range(len(movsi)):
    y=movsi[i]
    x1=posi.index(y)
    lis.append(x1)
  movs=[]
  for i in range(len(lis)):
    y=lis[i]
    x1=poss[y]
    movs.append(x1)
  ad=0
  movsi2=[]
  while con==True:
    ad=ad+1
    bisxn=bisx-ad
    bisyn=bisy-ad
    mv=f"{bisxn} {bisyn}"
    movsi.append(mv)
    
    if bisxn==1 or bisyn==1:
      break
  lis=[ ]
  for i in range(len(movsi)):
    y=movsi[i]
    x1=posi.index(y)
    lis.append(x1)
  movs2=[]
  for i in range(len(lis)):
    y=lis[i]
    x1=poss[y]
    movs2.append(x1)
  
  ad=0

  while con==True:
    ad=ad+1
    bisxn=bisx-ad
    bisyn=bisy+ad
    mv=f"{bisxn} {bisyn}"
    movsi.append(mv)
    if bisxn==1 or bisyn==8:
      con=False
  lis=[ ]
  for i in range(len(movsi)):
    y=movsi[i]
    try:
      x1=posi.index(y)
    except:
      x1=None
    if x1 != None:
      x1=posi.index(y)
      lis.append(x1)
  movs2=[]
  for i in range(len(lis)):
    y=lis[i]
    x1=poss[y]
    movs2.append(x1)
  while con==True:
    ad=ad+1
    bisxn=bisx+ad
    bisyn=bisy-ad
    mv=f"{bisxn} {bisyn}"
    movsi.append(mv)
    print(movsi)
    if bisxn==8 or bisyn==1:
      break
  lis=[ ]
  for i in range(len(movsi)):
    y=movsi[i]
    try:
      x1=posi.index(y)
    except:
      x1=None
    if x1 != None:
      x1=posi.index(y)
      lis.append(x1)
  movs2=[]
  for i in range(len(lis)):
    y=lis[i]
    o=lis[i]
    x1=poss[y]
    movs2.append(x1)
  print(movs2)


#def main():
  myList = bishop('f3')
  assert myList == ['a8', 'b7', 'c6', 'd1', 'd5', 'e2', 'e4', 'g2', 'g4', 'h1', 'h5']
#  myList = bishop('g7')
#  myList.sort()
#  assert myList == ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'f8', 'h6', 'h8']

if __name__ == "__main__":
#  main()
  x='d3'
  bishop(x)