#!/usr/bin/python3

from board import Board
import numpy
import sys

ply = 0
pv = []
winpaths = []
nodes = 0

def doSearch(depth):
  search(depth,True)
  print()

def search(depth, isRoot):
  global ply, pv, winpaths, nodes
  nodes += 1
  if not depth:
    if b.isWin():
      winpaths.append(pv[:])
    return
  mvs = b.genMoves()
  mvnum = 0
  for mv in mvs:
    if isRoot: 
      mvnum += 1
      sys.stdout.write("\rsearching move {0}/{1}, nodecount={2}, winpaths={3} ".format(mvnum,len(mvs),nodes,len(winpaths)))
      sys.stdout.flush()
    b.makeMove(mv)
    if ply >= len(pv): pv.append(mv)
    else: pv[ply] = mv
    ply += 1
    #wplen = len(winpaths)
    search(depth-1,False)
    #if isRoot and len(winpaths) > wplen: print(len(winpaths)-wplen)
    ply -= 1
    b.unmakeMove(mv)
  

b = Board(9)
print(b)


doSearch(4)
print("nodes = {0}".format(nodes))
print("winpaths = {0}".format(len(winpaths)))

pick = input("type 'p' to step through all winpaths, otherwise press enter to quit: ")
if pick == 'p':
  for wp in winpaths:
    print("******************************")
    bb = Board(9)
    print(wp)
    print(bb)
    for mv in wp:
      bb.makeMove(mv)
      print(bb)
    input("(press enter for next winpath)")
