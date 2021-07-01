#Importing all the modules that will be used in my program
import pygame,sys, random
import  time
from random import randint
from random import seed
#Initializing pygame
pygame.init()




#These are the number of columns rows used for the maze generation algorithm
COLS = 60
ROWS = 36

#These are the dimensions of the pygame window
LENGTH = 1920
HEIGHT = 1080

W = 15
grid = []
unvisited = []


#These are constants that I have defined. They are different colours that will be used throughout the program

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
DARK_GREEN = (53,98,68)
RED = (255,0,0)

#Node width and height
NODE_WIDTH = 100
NODE_HEIGHT = 50


#different lengths of array
LITTLE = 5
MIDDLE = 7
A_LOT = 10

#Arrow height and array
ARROW_HEIGHT = 50
ARROW_LENGTH = 100


BUBBLE_DRAWER_Y = 400

ARRAY_LENGTH = 100
ARRAY_HEIGHT = 65

CONNECTOR_LENGTH = 400

CURR_PLACE = (10,10)





win = pygame.display.set_mode((LENGTH, HEIGHT))

"""
This is a basic binary tree node, used for the binary search algorithm
"""

class tree_node():
    def __init__(self,amnt=None,right=None,left=None,parent=None):
        self.amnt = amnt
        self.right = right
        self.left = left
        self.parent = parent


"""
This class holds the number and the position of a specific number in an array. This class is create for the bubble sort function.
"""
class array_attribute():
    def __init__(self,amnt,x,y):
        self.amnt = amnt
        self.x = x
        self.y = y

"""
The purpose of this is to hold a block so that I can change it from different functions as it is pass-by-reference
"""
class block_holder():
    def __init__(self,block):
        self.block = block

"""
This is the block for the maze generator.
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

""""
I created this class so I can use a counter as an object, since the variables are pass-by-reference.
"""
class counter():
    def __init__(self,amnt):
        self.amnt = amnt

"""
This class is the node for the linked list animation.
"""
class node():
    def __init__(self,amnt):
        self.amnt = amnt
        self.animation = False



"""
This is the class used to create all the buttons
"""
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
When the animation is finished this function is used to draw the final node.
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
This function handles the edge case should there only be one node node or more. The reason behind the creation of this function is to omit extra lines of code.
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
The purpose of this function is to create an animation of the node when the person wants to add another node to the list.
"""
def _linked_list_node_animation():
    if first_node.amnt == 1:
        _node_edge_cases(10,500,100,100)
    else:
        _node_edge_cases(200 * (first_node.amnt -1),500,100,100)

"""
This function is used once the animation is finished. It draws the arrow.
"""
def perm_arrow():
    if first_node.amnt > 0:
        for i in range(1,first_node.amnt+1,1):
            if i == 2:
                pygame.draw.rect(win,BLACK,(110,525,ARROW_LENGTH,ARROW_HEIGHT),0)
            elif i > 2 :
                pygame.draw.rect(win,BLACK,((i-2)*200+100,525,ARROW_LENGTH,ARROW_HEIGHT),0)
"""
This function is used to draw the arrow to the linkedlist. It displays the animation
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
This draws the linked list window with all the buttons.
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
When the person clicks back everything is reset.
"""
def click_back():
    bin_tree.clicked = False
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


"""
This function checks if the cursor over the button. When the cursor is over the button then it changes the colour of the button.
"""
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
        if bin_tree.isOver(pos):
            bin_tree.color = (0, 0, 0)
        else:
            bin_tree.color = BROWN
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

        if bin_tree.clicked:
            if not(back_tree_node.clicked) and back_tree_node.isOver(pos):
                back_tree_node.color = BROWN
            else:
                back_tree_node.color = WHITE
            if not(add_tree_node.clicked) and add_tree_node.isOver(pos):
                add_tree_node.color = BROWN
            else:
                add_tree_node.color = WHITE
            if not(remove_button.clicked) and remove_button.isOver(pos):
                remove_button.color = BROWN
            else:
                remove_button.color = WHITE
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

"""
This function is used to check if the buttons are clicked or not. If they are certain actions are performed.
"""
def button_click():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if not(first_node.animation):
            if back_linked_list.isOver(pos):
                click_back()
        if bin_tree.isOver(pos):
            bin_tree.clicked = True
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

        if bin_tree.clicked:
            if remove_button.isOver(pos):
                if not(remove_tree_node(int(input("Please type the number that you would like to remove: ")))):
                    print("The number that you have typed does not exist in the binary tree!")
            if back_tree_node.isOver(pos):
                bin_tree.clicked = False
                first_tree_node.right = None
                first_tree_node.left = None
                first_tree_node.amnt = None
            if add_tree_node.isOver(pos):
                amnt_add = int(input("Please type in the number that you would like: "))
                if amnt_add < 10000 and amnt_add>=0:
                    if not(add_node(amnt_add)):
                        print("The number already exists")
                else:
                    print("The number that you entered is does not meet the requirements! Please enter a number between 0-9999 (inclusive)")
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

"""
The purpose of this function is to make all the buttons in the bubble sort window false. This is so that the user cannot click them while the animation is happening.
"""
def all_buttons_false():
    little_button.clicked = False
    medium_button.clicked = False
    a_lot_button.clicked = False
    bubble_back.clicked = False



"""
array function fills the array with random numbers based on which button the user clicked.
"""
def array():
    loc = 360
    for i in range(alg.amnt):
        bubble_array[i] = array_attribute(randint(0,10),loc,BUBBLE_DRAWER_Y)
        loc+=ARRAY_LENGTH+10

"""
When the user wants to go back to the main menu and clicks the back button this function is called to reset everything.
"""
def bubble_to_main():
    #Set the size to 0
    bubble_sort.clicked = False
    all_buttons_false()
    alg.amnt = 0

"""
This function creates a visual representation of an array on the screen
"""
def array_drawer():
    for i in range(alg.amnt):
        pygame.draw.rect(win,LIGHT_PINK,(bubble_array[i].x,bubble_array[i].y,ARRAY_LENGTH,bubble_array[i].amnt*ARRAY_HEIGHT),0)

"""
When the preson clicks the bubble sort button this function is called. This function acts as a conductor.
"""
def bubble_sort_window():
    win.fill(DARK_GREEN)
    medium_button.draw(win)
    a_lot_button.draw(win)
    little_button.draw(win)
    bubble_back.draw(win)
    pygame.display.set_caption('Bubble Sort')
    array_drawer()
    pygame.display.update()


"""
This function sorts the array using the bubble sort algorithm
"""
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
"""
Below are all the functions related to the maze generator algorithm
"""

"""
The purpose of the wall_removal function is to remove the wall if the distance between them has an absolute value of 1.
It takes in two parameters; two block objects.
"""
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
Given the x and y coordinates, this function will return the index of the cooresponeding block. If such a block does not exist, the function returns None.
"""
def give_index(x,y):
    if x < 0 or y < 0 or x > COLS -1 or y > ROWS - 1:
        return None
    else:
        return x + y * COLS


"""
Should the person click back or create in while the maze is being generated, this function will be called and reset everything.
"""

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



"""
This window creates the display for the maze window
"""
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


"""
All these functions will be related to the tree node
"""

"""
The tree_window function creates a display for the binary tree.
"""
def tree_window():
    win.fill(BLACK)
    back_tree_node.draw(win)
    add_tree_node.draw(win)
    remove_button.draw(win)
    t = first_tree_node
    draw_tree(910,150,t)
    pygame.display.update()

"""
The purpose of this function is to display the binary tree. It is a recursive function.
It takes in three parameters:
    - first: the x-coordinate
    - seceond: the y-coordinate
    - t: the node to draw
    
It is a void function.
"""
def draw_tree(first,second,t):
    if t.amnt != None:
        pygame.draw.rect(win,YELLOW,(first,second,100,100),0)
        myfont = pygame.font.SysFont('Comic Sans MS',30)
        textSurface = myfont.render(str(t.amnt),False,BLACK)
        win.blit(textSurface,(first+20,second+20))
    if t.right != None:
        pygame.draw.line(win,WHITE, [first+100,second+100],[first+150,second+150],10)
        draw_tree(first+150,second+150,t.right)
    if t.left != None:
        pygame.draw.line(win,WHITE,[first,second+100],[first-50,second+150],10)
        draw_tree(first-150,second+150,t.left)


"""
The purpose of the function is the remove a node from the binary tree. The function takes in 
an int as a parameter. If the given value does not exist then, the function returns False,
in which case the user is informed that the node does not exist. However, if the node does exist,
it is removed from the binary tree.
"""
def remove_tree_node(num):

    t = first_tree_node
    while t != None:
        if t.amnt == None:
            break
        if t.amnt < num:
            t = t.right
        elif t.amnt > num:
            t = t.left
        elif t.amnt == num:


            if t.right != None and t.left != None:
                holder = t.left
                while holder.right != None:
                    holder = holder.right
                if holder == t.left:
                    t.amnt = holder.amnt
                    if holder.left != None:
                        holder.left.parent = t
                    t.left = holder.left
                else:
                    holder.parent.right = holder.left
                    t.amnt = holder.amnt

            elif (t.right != None and t.left == None):
                t.amnt = t.right.amnt
                t.left = t.right.left
                if t.right.right!= None:
                    t.right.right.parent = t
                t.right = t.right.right

            elif (t.left != None and t.right == None):
                holder = t.left
                while holder.right != None:
                    holder = holder.right
                if holder == t.left:
                    t.amnt = t.left.amnt
                    if t.left.left!= None:
                        t.left.parent = t.left
                    t.left = t.left.left
                else:
                    holder.parent.right = holder.left
                    t.amnt = holder.amnt
            elif t.right == None and t.left == None:
                if t == first_tree_node:
                    first_tree_node.amnt = None
                elif t == t.parent.right:
                    t.parent.right = None
                elif t == t.parent.left:
                    t.parent.left = None
            return True
    return False

"""
The purpose of the function is to add a node to the binary tree. It takes in an int value as a parameter.
If a node with the given value already exists then, it returns False, in which case the user is
informed via the terminal window that the node with that value already exists. If a node with the
given value does not exist then, it is added to the tree.
"""
def add_node(temp):
    if first_tree_node.amnt == None:
        first_tree_node.amnt = temp
        return True
    temp_node = first_tree_node
    p = None
    while temp_node != None:
        if temp_node.amnt > temp:
            p = temp_node
            temp_node  = temp_node.left
        elif temp_node.amnt < temp:
            p = temp_node
            temp_node = temp_node.right
        else:
            return False
    if p.amnt < temp:
        p.right = tree_node(temp)
        p.right.parent = p
    elif p.amnt > temp:
        p.left = tree_node(temp)
        p.left.parent = p
    return True


"""
This function is used to recreate the main menu when teh person clicks the back button
"""
def redrawWindow():
    win.fill(LIGHT_PINK)
    temp_font = pygame.font.SysFont('comicsans',200)
    _message_to_screen("Pick the Algorithm!",LIGHT_YELLOW,temp_font)
    bin_tree.draw(win)
    bubble_sort.draw(win)
    linked_list.draw(win)
    maze_generator.draw(win)
    pygame.display.set_caption('Algorithm Visualizer')


"""
This function is used when the person program starts up. It is only used to display the "Pick the Algorithm!"
"""
def _message_to_screen(msg,color,test_font):
    screen_text = test_font.render(msg,True,color)
    text_rect = screen_text.get_rect(center = (LENGTH/2,100))
    win.blit(screen_text,text_rect)
run = True

# All the buttons for the main window
bin_tree = button(BROWN,500,600,350,100,'Binary Tree')
bubble_sort = button(BROWN,500,900,350,100,'Bubble Sort')
linked_list = button(BROWN,1000,900,350,100,'linked list')
maze_generator = button(BROWN,1000,600,350,100,'maze generator')


#All the buttons for the linked list window
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

first_tree_node = tree_node()
back_tree_node = button(WHITE,10,10,350,100,'Back')
add_tree_node = button(WHITE,1550,10,350,100,'Add')
remove_button = button(WHITE,785,10,350,100,'Remove')

# Nested for loop used to initialize the block and grid array with all the blocks and the ones that are unvisited
for j in range(ROWS):
    for i in range(COLS):
        block = Block(i,j)
        grid.append(block)
        unvisited.append(block)

n = 0
current = block_holder(grid[n])

while run:
    if linked_list.clicked:
        linked_list_window()
    elif bubble_sort.clicked:
        bubble_sort_window()
    elif maze_generator.clicked:
        maze_window(current)
    elif bin_tree.clicked:
        tree_window()
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
