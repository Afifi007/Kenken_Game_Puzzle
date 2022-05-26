import test_gen

import sys, pygame as pg

pg.init()
screen_size = 750,750
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 80)
pg.display.set_caption('Kenken')

size_1, number_cage = test_gen.generate(3)
# print(size_1)
print(number_cage)
# print("len(number_cage): ", len(number_cage))
# print("number_cage[0]: ",number_cage[0])
# print("number_cage[0][0]: ",number_cage[0][0])
# print("number_cage[0][1]: ",number_cage[0][1])
# print("number_cage[0][0][0]: ",number_cage[0][0][0])
# print("number_cage[0][0][0][0]: ",number_cage[0][0][0][0])
# print(type(number_cage))

list_num =[]
list_op =[]
list_co=[]
dic_1 = {}
for i in range(len(number_cage)):
  # print(type(number_cage[i]))
  # print(number_cage[i][-1])
  #1) store in lists
  list_num.append(number_cage[i][-1])
  list_op.append(number_cage[i][-2])
  list_co.append(number_cage[i][0])
  # #2)store in dic.
  # dic_1['cells'] = number_cage[i][:-2]
  # dic_1['op'] = number_cage[i][:-2]
  # print(dic_1)

print(list_num)
print(list_op)
print(list_co)
print(len(list_co))


number_grid_9x9 = [
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
]
number_grid_3x3 = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

def draw_background():
  screen.fill(pg.Color("white"))
  pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
  #720/9=80
  #720/8=90
  #720/7=102.857
  #720/6=120
  #720/5=144
  #720/4=180
  #720/3=240
  size = 240
  i = 1
  while (i*size) < 720:
    line_width = 5 if i % 3 > 0 else 10
    pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * size) + 15, 15),pg.Vector2((i * size) + 15 ,735), line_width)
    pg.draw.line(screen, pg.Color("black"), pg.Vector2(15,(i * size) + 15),pg.Vector2(735, (i * size) + 15), line_width)

    i += 1


def draw_numbers(size):
  row = 0
  # offset = 35
  offset = (size/2) -5
  # offset = 115 #(size/2) -5
  n_row = 3
  n_col = 3
  while row < n_row:
    col = 0
    while col < n_col:
      output = number_grid_3x3[row][col]
      # print(str(output))
      n_text = font.render(str(output), True, pg.Color("black"))
      screen.blit(n_text,pg.Vector2((col * size) + offset + 5, (row * size) + offset - 2))
      # screen.blit(n_text,pg.Vector2((col * 80) + offset + 5, (row * 80) + offset - 2))
      col += 1
    row += 1


def game_loop():
  for event in pg.event.get():
    if event.type == pg.QUIT: sys.exit()

  draw_background()
  draw_numbers(240)
  pg.display.flip()


while 1:
  game_loop()