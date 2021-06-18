import pygame,sys, random
import  time
from random import randint
from random import seed
pygame.init()

"""
Creating constants that I will be using in my program
"""


COLS = 60
ROWS = 36

LENGTH = 1920
HEIGHT = 1080

W = 15
grid = []
unvisited = []
LIGHT_YELLOW = (242,208,167)
LIGHT_PINK = (191,122,160)
BROWN = (136,56,45)
LIGHT_BLUE = (0,181,236)
LIME = (204,255,0)
PURPLE = (92,60,146)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
GREEN = (7,123,138)

RED = (255,0,0)
NODE_WIDTH = 100
NODE_HEIGHT = 50

LITTLE = 5
MIDDLE = 7
A_LOT = 10

ARROW_HEIGHT = 50
ARROW_LENGTH = 100


BUBBLE_DRAWER_Y = 400

ARRAY_LENGTH = 100
ARRAY_HEIGHT = 65

CONNECTOR_LENGTH = 400

CURR_PLACE = (10,10)


DARK_GREEN = (53,98,68)

"""
Creating the window
"""
win = pygame.display.set_mode((LENGTH, HEIGHT))
"""
What this class will do is that it will hold the location of that specific array
on the window and it will have the amount as well.
"""

class tree_node():
    def __init__(self,):
        self.amnt = None
        self.right = None
        self.left = None
        self.x = None
        self.y = None

class array_attribute():
    def __init__(self,amnt,x,y):
        self.amnt = amnt
        self.x = x
        self.y = y


class block_holder():
    def __init__(self,block):
        self.block = block
"""
The function of this class is to act as an int variable so that we can change values through functions
"""
class Block:
    def __init__(self, x, y):
        self.x , self.y = x,y
        self.walls = [True,True,True,True]
        self.visited = False
        self.col = 10

    def show(self,win):
        x = self.x*W
        y = self.y*W

        if self.visited:
            pygame.draw.rect(win,WHITE,(self.x*W+510,self.y*W+360,W,W))
        if self.walls[0]:
            pygame.draw.line(win,(0,0,0),(x+510,y+360),(x+W+510,y+360))
        if self.walls[1]:
            pygame.draw.line(win,(0,0,0),(x+W+510,y+360),(x+W+510,y+W+360))
        if self.walls[2]:
            pygame.draw.line(win,(0,0,0),(x+W+510,y+W+360),(x+510,y+W+360))
        if self.walls[3]:
            pygame.draw.line(win,(0,0,0),(x+510,y+W+360),(x+510,y+360))


    def highlight(self,win):
        x = self.x * W
        y = self.y * W
        if self.visited:
            pygame.draw.rect(win,RED,(self.x * W+510,self.y * W+360, W ,W))

    def checkNeighbours(self):
        neighbours = []
        x,y = self.x,self.y
        if give_index(x,y-1):
            top = grid[give_index(x,y-1)]
            neighbours.append(top)
        if give_index(x+1,y):
            right = grid[give_index(x+1,y)]
            neighbours.append(right)
        if give_index(x-1,y):
            left = grid[give_index(x-1,y)]
            neighbours.append(left)
        if give_index(x,y+1):
            bottom = grid[give_index(x,y+1)]
            neighbours.append(bottom)
        if len(neighbours)>0:
            return random.choice(neighbours)
        else:
            return None
class counter():
    def __init__(self,amnt):
        self.amnt = amnt


class node():
    def __init__(self,amnt):
        self.amnt = amnt
        self.animation = False




class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

"""
This function is used to draw the main menu.
"""
def redrawWindow():
    win.fill(LIGHT_PINK)
    temp_font = pygame.font.SysFont('comicsans',200)
    _message_to_screen("Pick the Algorithm!",LIGHT_YELLOW,temp_font)
    A_star_search_path.draw(win)
    bubble_sort.draw(win)
    linked_list.draw(win)
    maze_generator.draw(win)
    pygame.display.set_caption('Algorithm Visualizer')

"""
When the animation is finished this function will be called and the node will appear permanently
"""

def linked_list_final_node():
    if first_node.animation:
        for i in range(first_node.amnt-1):
            if i>0:
                pygame.draw.rect(win,WHITE,(i*200,500,100,100),0)
            else:
                pygame.draw.rect(win,WHITE,(10,500,100,100),0)
    else:
        for i in range(first_node.amnt):
            if i>0:
                pygame.draw.rect(win,WHITE,(i*200,500,100,100),0)
            else:
                pygame.draw.rect(win,WHITE,(10,500,100,100),0)
"""
This is a helper function that will display the text given by the user to the screen
"""
def _message_to_screen(msg,color,test_font):
    screen_text = test_font.render(msg,True,color)
    text_rect = screen_text.get_rect(center = (LENGTH/2,100))
    win.blit(screen_text,text_rect)

"""
This function is a helper function for the _linked_list_node_animation()
"""
def _node_edge_cases(x,y,l,w):

    if temp_x.amnt < x:
        pygame.draw.rect(win, WHITE, (temp_x.amnt, temp_y.amnt, l, w), 0)
        linked_list_final_node()
        pygame.display.update()
        temp_x.amnt += 5
    else:
        if temp_y.amnt < y:
            pygame.draw.rect(win, WHITE, (temp_x.amnt, temp_y.amnt, l, w), 0)
            linked_list_final_node()
            pygame.display.update()
            temp_y.amnt += 5
        else:
            temp_y.amnt = 0
            temp_x.amnt = 0
            first_node.animation = False
            next_stop.animation = True
"""
This function performs the animation for the node
"""
def _linked_list_node_animation():
    if first_node.amnt == 1:
        _node_edge_cases(10,500,100,100)
    else:
        _node_edge_cases(200 * (first_node.amnt -1),500,100,100)

"""
When the animation is finished this function permanatnly draw the arrow
"""
def perm_arrow():
    if first_node.amnt > 0:
        for i in range(1,first_node.amnt+1,1):
            if i == 2:
                pygame.draw.rect(win,BLACK,(110,525,ARROW_LENGTH,ARROW_HEIGHT),0)
            elif i > 2 :
                pygame.draw.rect(win,BLACK,((i-2)*200+100,525,ARROW_LENGTH,ARROW_HEIGHT),0)
"""
This function performs the animation of making the arrow
"""
def draw_arrow(amount):
    if temp_x_connector.amnt < amount:
        pygame.draw.rect(win,BLACK,(temp_x_connector_first.amnt,temp_y_connector_first.amnt,ARROW_LENGTH,ARROW_HEIGHT),0)
        pygame.display.update()
        temp_x_connector.amnt+=5
    else:
        temp_x_connector.amnt += 100
        temp_x_connector_first.amnt = temp_x_connector.amnt
        next_stop.animation = False

"""
This function is called when the user wants to open the linked list window.
"""
def linked_list_window():
    win.fill(LIGHT_BLUE)
    back_linked_list.draw(win)
    add_linked_list.draw(win)
    remove_linked_list.draw(win)
    pygame.display.set_caption('Linked List')
    if first_node.animation:
        if first_node.amnt > 1:
            if next_stop.animation:
                if first_node.amnt == 2:
                    perm_arrow()
                    linked_list_final_node()
                    draw_arrow(temp_x_connector_first.amnt+90)
                else:
                    perm_arrow()
                    linked_list_final_node()
                    draw_arrow(200*(first_node.amnt-1))
            else:
                perm_arrow()
                _linked_list_node_animation()
        else:
            perm_arrow()
            _linked_list_node_animation()
    perm_arrow()
    linked_list_final_node()

"""
This function is for when the user clicks back when he is in the linked list window
"""
def click_back():
    A_star_search_path.clicked = False
    bubble_sort.clicked = False
    linked_list.clicked = False
    maze_generator.clicked = False
    add_linked_list.clicked = False
    first_node.amnt = 0
    temp_y.amnt = 0
    temp_x.amnt = 0
    temp_y_connector_first.amnt = 525
    temp_x_connector_first.amnt = 110
    temp_x_connector.amnt = 110
    temp_y_connector.amnt = 525



def over():
    if event.type == pygame.MOUSEMOTION:
        if linked_list.clicked == True:
            if back_linked_list.isOver(pos):
                back_linked_list.color = (0, 0, 0)
            else:
                back_linked_list.color = LIME
            if add_linked_list.isOver(pos):
                add_linked_list.color = (0, 0, 0)
            else:
                add_linked_list.color = LIME
            if remove_linked_list.isOver(pos):
                remove_linked_list.color = (0,0,0)
            else:
                remove_linked_list.color = LIME
        if A_star_search_path.isOver(pos):
            A_star_search_path.color = (0, 0, 0)
        else:
            A_star_search_path.color = BROWN
        if bubble_sort.isOver(pos):
            bubble_sort.color = (0, 0, 0)
        else:
            bubble_sort.color = BROWN

        if linked_list.isOver(pos):
            linked_list.color = (0, 0, 0)
        else:
            linked_list.color = BROWN
        if maze_generator.isOver(pos):
            maze_generator.color = (0, 0, 0)
        else:
            maze_generator.color = BROWN

        if A_star_search_path.clicked:
            if not(back_tree_node.clicked) and back_tree_node.isOver(pos):
                back_tree_node.color = BROWN
            else:
                back_tree_node.color = WHITE
            if not(add_tree_node.clicked) and add_tree_node.isOver(pos):
                add_tree_node.color = BROWN
            else:
                add_tree_node.color = WHITE
        if bubble_sort.clicked:
            if not(little_button.clicked) and little_button.isOver(pos):
                little_button.color = BLACK
            else:
                little_button.color = RED
            if not(medium_button.clicked) and medium_button.isOver(pos):
                medium_button.color = BLACK
            else:
                medium_button.color = RED
            if not(a_lot_button.clicked) and a_lot_button.isOver(pos):
                a_lot_button.color = BLACK
            else:
                a_lot_button.color = RED

            if not(bubble_back.clicked) and bubble_back.isOver(pos):
                bubble_back.color = BLACK
            else:
                bubble_back.color = RED



        if maze_generator.clicked:
            if maze_back.isOver(pos):
                maze_back.color = YELLOW
            else:
                maze_back.color = WHITE

            if create.isOver(pos):
                create.color = YELLOW
            else:
                create.color = WHITE


def button_click():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if not(first_node.animation):
            if back_linked_list.isOver(pos):
                click_back()
        if A_star_search_path.isOver(pos):
            A_star_search_path.clicked = True
        if bubble_sort.isOver(pos):
            bubble_sort.clicked = True
        if linked_list.isOver(pos):
            linked_list.clicked = True
        if maze_generator.isOver(pos):
            maze_generator.clicked = True
        if not(first_node.animation) and first_node.amnt < 10:
            if add_linked_list.isOver(pos):
                first_node.amnt+=1
                first_node.animation = True
        if not(first_node.animation):
            if remove_linked_list.isOver(pos):
                if first_node.amnt >=1:
                    temp_y.amnt = 0
                    temp_x.amnt = 0
                    first_node.amnt-=1
                    if first_node.amnt >1:
                        temp_x_connector.amnt -= 200
                        temp_x_connector_first.amnt = temp_x_connector.amnt
                    else:
                        temp_x_connector.amnt = 110
                        temp_x_connector_first.amnt = temp_x_connector.amnt

        if A_star_search_path.clicked:
            if back_tree_node.isOver(pos):
                A_star_search_path.clicked = False
            if add_tree_node.isOver(pos):
                add_node(int(input("Please type in the number that you would like: ")))
        #If we are in the bubble sort menu
        if bubble_sort.clicked:
            if not(bubble_back.clicked) and bubble_back.isOver(pos):
                bubble_to_main()
            elif not(little_button.clicked) and little_button.isOver(pos):
                all_buttons_true()
                alg.amnt = LITTLE
                array()
                bubble_sort_alg()
            elif not(medium_button.clicked) and medium_button.isOver(pos):
                all_buttons_true()
                alg.amnt = MIDDLE
                array()
                bubble_sort_alg()
            elif not(a_lot_button.clicked) and a_lot_button.isOver(pos):
                all_buttons_true()
                alg.amnt = A_LOT
                array()
                bubble_sort_alg()
            all_buttons_false()

        if maze_generator.clicked:
            if maze_back.isOver(pos):
                maze_generator.clicked = False
                create.clicked = False
                disable()
            if create.isOver(pos):
                disable()
                create.clicked = True


def disable():
    del unvisited[:]
    del grid[:]
    for j in range(ROWS):
        for i in range(COLS):
            block = Block(i, j)
            unvisited.append(block)
            grid.append(block)
    n = 0
    current.block = grid[n]


def maze_window(current):
    win.fill(BLACK)
    maze_back.draw(win)
    create.draw(win)
    if create.clicked:

        for block in grid:
            block.show(win)
        current.block.visited = True
        for block in unvisited:
            if block == current:
                unvisited.remove(block)
        current.block.highlight(win)
        check = False
        for x in unvisited:
            if not (x.visited):
                check = True
                break
        if check:
            next_block = current.block.checkNeighbours()
            if isinstance(next_block, Block) and not next_block.visited:
                wall_removal(current.block, next_block)
                next_block.visited = True
            current.block = next_block
        pygame.display.update()




def give_index(x,y):
    if x < 0 or y < 0 or x > COLS -1 or y > ROWS - 1:
        return None
    else:
        return x + y * COLS

"""
This function sets the value of all the buttons to be true so that they cannot be clicked while the animation
is taking place.
"""
def all_buttons_true():
    little_button.clicked = True
    medium_button.clicked = True
    a_lot_button.clicked = True
    bubble_back.clicked = True
"""
When we are done with the animation we will call this function to reset all of them to false so that
we can run the program again.
"""
def all_buttons_false():
    little_button.clicked = False
    medium_button.clicked = False
    a_lot_button.clicked = False
    bubble_back.clicked = False


def array():
    loc = 360
    for i in range(alg.amnt):
        bubble_array[i] = array_attribute(randint(0,10),loc,BUBBLE_DRAWER_Y)
        loc+=ARRAY_LENGTH+10


def bubble_to_main():
    #Set the size to 0
    bubble_sort.clicked = False
    all_buttons_false()
    alg.amnt = 0


def array_drawer():
    for i in range(alg.amnt):
        pygame.draw.rect(win,LIGHT_PINK,(bubble_array[i].x,bubble_array[i].y,ARRAY_LENGTH,bubble_array[i].amnt*ARRAY_HEIGHT),0)


def bubble_sort_window():
    win.fill(DARK_GREEN)
    medium_button.draw(win)
    a_lot_button.draw(win)
    little_button.draw(win)
    bubble_back.draw(win)
    pygame.display.set_caption('Bubble Sort')
    array_drawer()
    pygame.display.update()



def bubble_sort_alg():
    n = alg.amnt
    for i in range(n-1):
        for j in range(0,n-i-1):
            if bubble_array[j].amnt > bubble_array[j+1].amnt:

                if bubble_array[j].x > bubble_array[j+1].x:
                    first = bubble_array[j].x
                    while bubble_array[j+1].x < first:
                        bubble_array[j+1].x+=5
                        bubble_array[j].x-=5
                        bubble_sort_window()
                        array_drawer()
                        pygame.display.update()
                else:
                    first = bubble_array[j+1].x
                    while bubble_array[j].x<first:
                        bubble_array[j].x+=5
                        bubble_array[j+1].x-=5
                        bubble_sort_window()
                        array_drawer()
                        pygame.display.update()

                bubble_array[j] , bubble_array[j+1] = bubble_array[j+1], bubble_array[j]


def wall_removal(a,b):
    x = a.x - b.x
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False
    y = a.y-b.y
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False

"""
All these functions will be related to the tree node
"""
def a_star_window():
    win.fill(BLACK)
    back_tree_node.draw(win)
    add_tree_node.draw(win)


def draw_tree():
    temp_node = first_tree_node

    pygame.display.update()

def add_node(temp):
    temp_node = first_tree_node
    while True:
        if temp.amnt == None:
            first_tree_node.amnt = temp
        else:
            if temp_node.amnt < temp:
                if temp_node.right != None:
                    temp_node = temp_node.right
                else:
                    if temp_node.x + 150 < 1080 and temp_node.y + 150 < 1920:
                        tree = tree_node()
                        tree.amnt = temp
                        tree.x = temp_node.x+50
                        tree.y = temp_node.y+50
                        temp_node.right = tree
                    
            elif temp.amnt > temp:
                if temp_node.left != None:
                    temp_node = temp_node.left
                else:
                    tree = tree_node()
                    tree.amnt = temp
                    temp_node.left = tree
"""
Creating all the variables and objects that I will be using in my program
"""


run = True

A_star_search_path = button(BROWN,500,600,350,100,'A* Search Path')
bubble_sort = button(BROWN,500,900,350,100,'Bubble Sort')
linked_list = button(BROWN,1000,900,350,100,'linked list')
maze_generator = button(BROWN,1000,600,350,100,'maze generator')


#A_star_back = button()

remove_linked_list = button(LIME,785,950,350,100,'Remove')

back_linked_list = button(LIME,10,950,350,100,'Back')
add_linked_list = button(LIME,1550,950,350,100,'Add')

first_node = node(0)

temp_y = counter(0)
temp_x = counter(0)


temp_x_connector_first = counter(110)
temp_y_connector_first = counter(525)



temp_x_connector =  counter(110)
temp_y_connector = counter(525)

next_stop = node(200)


arrow_counter = counter(110)

next_stop.animation = True

alg = counter(0)

bubble_drawer_x = counter(360)


bubble_array = [None]*A_LOT

little_button = button(RED,250,10,350,100,'little')
medium_button = button(RED,610,10,350,100,'medium')
a_lot_button = button(RED,970,10,350,100,'a lot')
bubble_back = button(RED,1330,10,350,100,'back')


maze_back = button(WHITE,10,10,350,100,'Back')
create = button(WHITE,1550,10,350,100,'Create')

"""
All these variables will be related to the tree node
"""
first_tree_node = tree_node()
back_tree_node = button(WHITE,10,10,350,100,'Back')
add_tree_node = button(WHITE,1550,10,350,100,'Add')

"""
"""
for j in range(ROWS):
    for i in range(COLS):
        block = Block(i,j)
        grid.append(block)
        unvisited.append(block)
n = 0
current = block_holder(grid[n])
"""
Start running to program
"""
while run:
    if linked_list.clicked:
        linked_list_window()
    elif bubble_sort.clicked:
        bubble_sort_window()
    elif maze_generator.clicked:
        maze_window(current)
    elif A_star_search_path.clicked:
        a_star_window()
    else:
        redrawWindow()
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        button_click()
        over()
