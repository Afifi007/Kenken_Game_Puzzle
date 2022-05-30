from turtle import clear, color
import random 
import src.kenken as ken

import sys, pygame as pg

pg.init()
f = 1
width = 750
height = 750
screen_size = width,height

screen = pg.display.set_mode(screen_size)


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
  font_size_2 = int(size / 7)
  font1 = pg.font.SysFont(None, font_size_2)

  offset = 30
  for i in range(0,len(lis_cells)):
      op = lis_op[i]
      op_value = li_num [i]
      x ,y= lis_cells[i][0][0] , lis_cells[i][0][1]
      row = x-1
      col = y- 1
      op_text  =(str(op)+str(op_value))
      n_text = font1.render(op_text, True, pg.Color("black"))
      screen.blit(n_text,pg.Vector2((col * size) + offset, (row * size) + offset))

def draw_background(size):
  screen.fill(pg.Color("white"))
  pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, width-30, height-30), 10)
  #720/9=80
  #720/8=90
  #720/7=102.857
  #720/6=120
  #720/5=144
  #720/4=180
  #720/3=240
  
  i = 1
  while (i*size) < 720:
    line_width = 5
    pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * size) + 15, 15),pg.Vector2((i * size) + 15 ,735), line_width)
    pg.draw.line(screen, pg.Color("black"), pg.Vector2(15,(i * size) + 15),pg.Vector2(735, (i * size) + 15), line_width)

    i += 1


def draw_numbers(size ,li_num,lis_cells):
  font_size_1 = int(size / 6)
  font = pg.font.SysFont(None, font_size_1)
  offset = (size/2)
  for i in range(0,len(lis_cells)):
    len_of_indx = len(lis_cells[i])
    for j in range(len_of_indx):
      op_value = li_num [i][j]
      x ,y= lis_cells[i][j][0] , lis_cells[i][j][1]
      row = x-1
      col = y- 1
      op_text  =str(op_value)
      n_text = font.render(op_text, True, pg.Color("black"))
      screen.blit(n_text,pg.Vector2((col * size) + offset + 5, (row * size) + offset - 2))

def paint_cells(list_cord,n):
  len_of_cord = len(list_cord)
  

  for i in range(len_of_cord):
    len_of_indx = len(list_cord[i])
    for j in range(len_of_indx):
      x ,y= list_cord[i][j][0] , list_cord[i][j][1]
      row = x-1
      col = y-1
      pg.draw.rect(screen, pg.Color(color_list[i]), pg.Rect(15, 15, 720/n, 720/n).move(col*720/n, row * 720/n))


def clear_me(n):
  size_2 = 720/n
  draw_background(size_2)
  pg.display.update()

def game_loop_2(n):
  size, cliques = ken.generate(n)
  size_2 = 720/n
  draw_background(size_2)
  list_num =[]
  list_op =[]
  list_co=[]
  number_cage = cliques
  for i in range(len(number_cage)):
      list_num.append(number_cage[i][-1])
      list_op.append(number_cage[i][-2])
      list_co.append(number_cage[i][0])
  
  paint_cells(list_co,n)
  draw_op(size_2,list_num,list_op,list_co)
  pg.display.flip()
  

  return size, cliques

def game_loop(n,algo, cliques):

  size = 720/n
  for event in pg.event.get():
    if event.type == pg.QUIT: sys.exit()
  
  result = ken.runner(n,algo,cliques)
  my_list = list(result.values())
  my_list_2 = list(result.keys())
  draw_numbers(size ,my_list,my_list_2)

  pg.display.flip()