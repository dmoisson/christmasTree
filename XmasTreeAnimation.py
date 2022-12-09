from tree import RGBXmasTree
from time import sleep
from random import randrange

tree = RGBXmasTree()
tree.color = (0,0,0)
tree.brightness = 0.1

def colorByHeight(c1, c2, c3, c4):
    tree[3].color = c1

    tree[2].color = c2
    tree[4].color = c2
    tree[9].color = c2
    tree[10].color = c2
    tree[21].color = c2
    tree[22].color = c2
    tree[13].color = c2
    tree[18].color = c2

    tree[1].color = c3
    tree[5].color = c3
    tree[8].color = c3
    tree[11].color = c3
    tree[17].color = c3
    tree[14].color = c3
    tree[23].color = c3
    tree[20].color = c3

    tree[0].color = c4
    tree[6].color = c4
    tree[7].color = c4
    tree[12].color = c4
    tree[15].color = c4
    tree[16].color = c4
    tree[19].color = c4
    tree[24].color = c3


def colorByHeightAtOnce(c1,c2,c3,c4):
    tree.value = [c4,c3,c2,c1,c2,c3,c4,c4,c3,c2,c2,c3,c4,c2,c3,c4,c4,c3,c2,c4,c3,c2,c2,c3,c4]

"""
      3
      
    2   4
    
  1       5
  
0           6
"""


"""
tree[0].color = c4
    tree[1].color = c3
    tree[2].color = c2
    tree[3].color = c1
    tree[4].color = c2
    tree[5].color = c3
    tree[6].color = c4
    tree[7].color = c4
    tree[8].color = c3
    tree[9].color = c2
    tree[10].color = c2
    tree[11].color = c3
    tree[12].color = c4
    tree[13].color = c2
    tree[14].color = c3
    tree[15].color = c4
    tree[16].color = c4
    tree[17].color = c3
    tree[18].color = c2
    tree[19].color = c4
    tree[20].color = c3
    tree[21].color = c2
    tree[22].color = c2
    tree[23].color = c3
    tree[24].color = c4







maxBrigthness = 1

def fade():
    for i in range(10):
        tree.brightness = i/10 * maxBrigthness
    for i in range(11):
        tree.brightness = (1 - i/10) * maxBrigthness

colors = [
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (0,1,1),
    (1,0,1),
    (1,1,1)
    ]

for color in colors:
    for pixel in tree:
      pixel.color = color
      #fade()
      
      
tree.color = (0,0,0)
"""
def random():
  while True:
    c1 = randrange(10)/10
    c2 = randrange(10)/10
    c3 = randrange(10)/10
    p = randrange(25)
    tree[p].color = (c1,c2,c3)
    sleep(0.3)

c1 = c2 = c3 = c4 = (0,0,0)
while True:
  for i in range(0,100,5):
    x = 100 - i
    y = 33 - i
    z = 66 - i
    if y  < 0:
        y = 0 - y
    if z < 0:
        z = 0 - z
    c4 = c3
    c3 = c2
    c2 = c1
    c1 = (x/100,y/100,z/100)
    colorByHeightAtOnce(c1,c2,c3,c4)
  for i in range(0,100,5):
    x = i
    y = i + 67
    z = i + 33
    if y  > 100:
        y = 200 - y
    if z > 100:
        z = 200 -z
    c4 = c3
    c3 = c2
    c2 = c1
    c1 = (x/100,y/100,z/100)
       
    colorByHeightAtOnce(c1,c2,c3,c4)

print(c1)
