from turtle import clear, color
import test_gen
import random 

import sys, pygame as pg

pg.init()
f = 1
screen_size = 750,750
screen = pg.display.set_mode(screen_size)
font = pg.font.SysFont(None, 30)
font1 = pg.font.SysFont(None, 20)
pg.display.set_caption('Kenken')



color_list = [
  "#2E5894",
  "#3DDC84",
  "cyan",
  "#87A96B",
  "#28B9BC",
  "#6ACB25",
  "#CB25B5",
  "#C46210",
  "#AB274F",
  "#3B7A57",
  "#8F9779",
  "#FFE4C4",
  "#FE6F5E",
  "#A2A2D0",
  "#DE5D83",
  "#A9B2C3",
  "#A67B5B",
  "#ACE1AF",
  "#F7E7CE",
  "#98817B",
  "#A7D8DE",
  "#9400D3",
  "#8806CE",
  "#E48400",
  "#555555",
  "#DA3287",
  "#B94E48",
  "#8CBED6",
  "#8FBC8F",
  "#8B008B",
  "#BDB76B",
  "#F56FA1",
  "#996666",
  "#DFFF00",
  "#703642",
  "#FFEF00",
  "#A9B2C3",
  "#E97451",
  "#7BB661",
  "#D891EF",
  "#006A4E",
  "#E3DAC9",
  "#7366BD",
  "#064E40",
  "#0018A8",
  "#FAF0BE",
  "#660000",
  "#BF4F51",
  "#BFFF00",
  "#967117",
  "#DA1884",
  "#FEFEFA",
  "#007FFF",
]


def draw_op(size ,li_num,lis_op,lis_cells):

  offset = (size/2)
  for i in range(0,len(lis_cells)):
      op = lis_op[i]
      op_value = li_num [i]
      #print('op + value',str(op)+str(op_value))
      x ,y= lis_cells[i][0][0] , lis_cells[i][0][1]
      row = x-1
      col = y- 1
      op_text  =(str(op)+str(op_value))
      #op_text = font.render(str(op)+str(op_value), True, (0,0,0))
      n_text = font1.render(op_text, True, pg.Color("black"))
      text_rect = n_text.get_rect()
      text_rect.center = ((col * size) + offset + 5, (row * size) + offset - 2)
      screen.blit(n_text,text_rect)

number_grid_9x9 = [
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
  # [1,2,3,4,5,6,7,8,9],
]
number_grid_3x3 = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

def draw_background(size):
  screen.fill(pg.Color("white"))
  pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
  #720/9=80
  #720/8=90
  #720/7=102.857
  #720/6=120
  #720/5=144
  #720/4=180
  #720/3=240
  
  i = 1
  while (i*size) < 720:
    line_width = 5 if i % 3 > 0 else 10
    pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * size) + 15, 15),pg.Vector2((i * size) + 15 ,735), line_width)
    pg.draw.line(screen, pg.Color("black"), pg.Vector2(15,(i * size) + 15),pg.Vector2(735, (i * size) + 15), line_width)

    i += 1


def draw_numbers(size,n_row,n_col):
  row = 0
  # offset = 35
  offset = (size/2) +10
  # offset = 115 #(size/2) -5
  
  while row < n_row:
    col = 0
    while col < n_col:
      output = number_grid_9x9[row][col]
      # print(str(output))
      n_text = font.render(str(output), True, pg.Color("black"))
      screen.blit(n_text,pg.Vector2((col * size) + offset + 5, (row * size) + offset - 2)) #draw @ center
      # screen.blit(n_text,pg.Vector2((col * 80) + offset + 5, (row * 80) + of
      col += 1
    row += 1  


def paint_cells(list_cord,n):
  len_of_cord = len(list_cord)
  

  for i in range(len_of_cord):
    # color_nom = 0
    len_of_indx = len(list_cord[i])
    for j in range(len_of_indx):
    # if len_of_indx =1:
      x ,y= list_cord[i][j][0] , list_cord[i][j][1]

      row = x-1
      col = y-1

      pg.draw.rect(screen, pg.Color(color_list[i]), pg.Rect(15, 15, 720/n, 720/n).move(col*720/n, row * 720/n))


def game_loop(n):
  size = 720/n
  for event in pg.event.get():
    if event.type == pg.QUIT: sys.exit()
  
  draw_background(size)
  list_num =[]
  list_op =[]
  list_co=[]
  size_1, number_cage = test_gen.generate(n)
  for i in range(len(number_cage)):
      list_num.append(number_cage[i][-1])
      list_op.append(number_cage[i][-2])
      list_co.append(number_cage[i][0])
  # draw_numbers(size , 9,9)
  
  paint_cells(list_co,n)
  draw_op(size,list_num,list_op,list_co)  

  pg.display.flip()


# while 1:
# game_loop(n)