#!/usr/bin/python3

import numpy

def even(n):
  return n%2==0

class Board:
  def __init__(self, size):
    self.size = size
    self.b = numpy.zeros((size,size), dtype=int)
    self.b[3,4] = 1
    self.b[4,4] = 1
    self.b[4,3] = 1
    self.b[5,3] = 1
    self.b[5,4] = 1
    self.b[5,5] = 1

  def __str__(self):
    boardstr = ""
    even = True
    for row in self.b:
      rowstr = " " if even else ""
      for cell in row:
        rowstr += "O " if cell else ". "
      boardstr += rowstr + "\n"
      even = not even
    return boardstr
    
  def nw(self,r,c):
    c -= 0 if even(r) else 1
    r -= 1
    return None if r < 0 or c < 0 else self.b[r,c]

  def ne(self,r,c):
    c += 1 if even(r) else 0
    r -= 1
    return None if r < 0 or c == self.size else self.b[r,c]

  def w(self,r,c):
    c -= 1
    return None if c < 0 else self.b[r,c]

  def e(self,r,c):
    c += 1
    return None if c == self.size else self.b[r,c]

  def sw(self,r,c):
    c -= 0 if even(r) else 1
    r += 1
    return None if r == self.size or c < 0 else self.b[r,c]

  def se(self,r,c):
    c += 1 if even(r) else 0
    r += 1
    return None if r == self.size or c == self.size else self.b[r,c]

  def neighbors(self,r,c):
    return [self.nw(r,c),self.ne(r,c),self.e(r,c),self.se(r,c),self.sw(r,c),self.w(r,c)]

  def isWin(self):
    for r in range(0,self.size):
      for c in range(0,self.size):
        if self.nw(r,c) and self.ne(r,c) and self.e(r,c) and self.se(r,c) and self.sw(r,c) and self.w(r,c): return True
    return False

  def score(self):
    return 1 if self.isWin() else 0

  def makeMove(self,mv):
    self.b[mv[0],mv[1]] = 0
    self.b[mv[2],mv[3]] = 1

  def unmakeMove(self,mv):
    self.b[mv[0],mv[1]] = 1
    self.b[mv[2],mv[3]] = 0

  def genMoves(self):
    moves = []
    for r in range(0,self.size):
      for c in range(0,self.size):
        if self.b[r,c] and self.slideable(r,c): 
          moves.extend(self.genMovesFrom(r,c))
    return moves

  def genMovesFrom(self,r,c):
    moves = []
    self.b[r,c] = 0
    for rr in range(0,self.size):
      for cc in range(0,self.size):
        if self.b[rr,cc] or (rr==r and cc==c): continue
        if self.validMoveTo(rr,cc): moves.append([r,c,rr,cc])
    self.b[r,c] = 1
    return moves

  def slideable(self,r,c):
    n = self.neighbors(r,c)
    lv = n[5]
    for v in n:
      if not (v or lv): return True
      lv = v
    return False

  def validMoveTo(self,r,c):
    n = self.neighbors(r,c)
    nc = n.count(1)
    if nc < 2: return False
    elif nc == 2: return True
    elif nc > 4: return False
    else: return self.slideable(r,c)
    
