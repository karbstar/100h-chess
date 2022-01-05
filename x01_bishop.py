#!python3

def bishop(square):
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
    inr=f"1{i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"b{i}"
    inr=f"2{i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"c{i}"
    inr=f"3{i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"d{i}"
    inr=f"4{i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"e{i}"
    inr=f"5{i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"f{i}"
    inr=f"6{i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"g{i}"
    inr=f"7{i}"
    poss.append(sen)
    posi.append(inr)
  for i in range(8):
    i=i+1
    sen=f"h{i}"
    inr=f"8{i}"
    poss.append(sen)
    posi.append(inr)
  print(poss)
  print(posi)
  return None



#def main():
#  myList = bishop('f3')
#  #myList.sort()
#  assert myList == ['a8', 'b7', 'c6', 'd1', 'd5', 'e2', 'e4', 'g2', 'g4', 'h1', 'h5']
#  myList = bishop('g7')
#  myList.sort()
#  assert myList == ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'f8', 'h6', 'h8']

#if __name__ == "__main__":
#  main()
