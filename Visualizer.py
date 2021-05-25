import pygame
import  time
from random import randint
from random import seed
pygame.init()

"""
Creating constants that I will be using in my program
"""
LENGTH = 1920
HEIGHT = 1080

LIGHT_YELLOW = (242,208,167)
LIGHT_PINK = (191,122,160)
BROWN = (136,56,45)
LIGHT_BLUE = (0,181,236)
LIME = (204,255,0)
PURPLE = (255,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)


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
The function of this class is to act as an int variable so that we can change values through functions
"""
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



def button_click():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if not(first_node.animation):
            if back_linked_list.isOver(pos):
                click_back()
        if A_star_search_path.isOver(pos):
            pass
        if bubble_sort.isOver(pos):
            bubble_sort.clicked = True
        if linked_list.isOver(pos):
            linked_list.clicked = True
        if maze_generator.isOver(pos):
            pass
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

        #If we are in the bubble sort menu
        if bubble_sort.clicked:
            if not(bubble_back.clicked) and bubble_back.isOver(pos):
                bubble_to_main()
            elif not(little_button.clicked) and little_button.isOver(pos):
                alg.amnt = LITTLE
                all_buttons_true()
                array(bubble_array)
            elif not(medium_button.clicked) and medium_button.isOver(pos):
                alg.amnt = MIDDLE
                all_buttons_true()
                array(bubble_array)
            elif not(a_lot_button.clicked) and a_lot_button.isOver(pos):
                alg.amnt = A_LOT
                all_buttons_true()
                array(bubble_array)
            print(bubble_array)
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
def array(temp_arr):
    for i in range(alg.amnt):
        temp_arr.append(randint(0,10))

def bubble_to_main():
    #Set the size to 0
    bubble_sort.clicked = False
    all_buttons_false()
    alg.counter = 0
    bubble_array = []


def array_drawer():
    for i in range(1,alg.amnt+1):
        if bubble_array[i-1] != 0:
            pygame.draw.rect(win,LIGHT_PINK,(bubble_drawer_x.amnt,BUBBLE_DRAWER_Y,ARRAY_LENGTH,ARRAY_HEIGHT*bubble_array[i-1]),0)
            bubble_drawer_x.amnt+=ARRAY_LENGTH+10
    bubble_drawer_x.amnt = 360


def bubble_sort_window():
    win.fill(DARK_GREEN)
    medium_button.draw(win)
    a_lot_button.draw(win)
    little_button.draw(win)
    bubble_back.draw(win)
    if alg.amnt > 0:
        bubble_sort_alg()

def bubble_sort_alg():
    n = len(bubble_array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            time.sleep(0.1)
            if bubble_array[j] > bubble_array[j+1]:
                bubble_array[j] , bubble_array[j+1] = bubble_array[j+1], bubble_array[j]
            array_drawer()
"""
Creating all the variables and objects that I will be using in my program
"""


run = True

A_star_search_path = button(BROWN,500,600,350,100,'A* Search Path')
bubble_sort = button(BROWN,500,900,350,100,'Bubble Sort')
linked_list = button(BROWN,1000,900,350,100,'linked list')
maze_generator = button(BROWN,1000,600,350,100,'maze generator')


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


bubble_array = []

little_button = button(RED,250,10,350,100,'little')
medium_button = button(RED,610,10,350,100,'medium')
a_lot_button = button(RED,970,10,350,100,'a lot')
bubble_back = button(RED,1330,10,350,100,'back')
"""
Start running to program
"""
while run:
    if linked_list.clicked:
        linked_list_window()
    elif bubble_sort.clicked:
        bubble_sort_window()
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
