# snake.py
from tkinter import * # เอามาทั้งหมดเลย
from PIL import Image, ImageTk # เอามาแค่บางส่วน
import random

class Snake(Canvas):
    def __init__(self):
        super().__init__(width=600,height=600,background='black',highlightthickness=0)
        self.snake_positions = [(80,80),(120,80),(160,80)]
        
        self.direction = 'Right'
        self.MOVE_INCREMENT = 40 # size of body and food (px)
        self.x_loc = range(0,561,self.MOVE_INCREMENT)
        self.y_loc = range(0,561,self.MOVE_INCREMENT)
        self.food_positions = (random.choice(self.x_loc), random.choice(self.y_loc))

        self.load_assets()
        self.create_objects()
        self.bind_all('<Key>', self.on_key_press)

    def load_assets(self):
        self.snake_body_image = Image.open('body.png')
        self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

        self.food_image = Image.open('food.png')
        self.food = ImageTk.PhotoImage(self.food_image)
    
    def create_objects(self):
        self.create_image(self.snake_positions[0][0],self.snake_positions[0][1],image=self.snake_body,tag='snake')
        self.create_image(self.food_positions[0],self.food_positions[1],image=self.food,tag='food')

    def move_snake(self):
        head_x, head_y = self.snake_positions[0]

        if self.direction == 'Right':
            self.snake_positions[0] = (head_x + self.MOVE_INCREMENT, head_y)
        elif self.direction == 'Left':
            self.snake_positions[0] = (head_x - self.MOVE_INCREMENT, head_y)
        elif self.direction == 'Up':
            self.snake_positions[0] = (head_x, head_y - self.MOVE_INCREMENT)
        elif self.direction == 'Down':
            self.snake_positions[0] = (head_x, head_y + self.MOVE_INCREMENT)
        else:
            print('Stay here!')

        # เปลี่ยนตำแหน่งของงู
        snake_location = self.find_withtag('snake')
        print('Snake Loc: ',snake_location)
        print('X,Y:', self.snake_positions[0])
        self.coords(snake_location, self.snake_positions[0])

        if head_x == self.food_positions[0] and head_y == self.food_positions[1]:
            self.food_positions = (random.choice(self.x_loc), random.choice(self.y_loc))
            food_location = self.find_withtag('food')
            self.coords(food_location, self.food_positions)


    def on_key_press(self,e):
        # e = event = เช็คในเกมว่าเกิดอะไรขึ้นมา มีการคลิกหรือมีการกดคีย์บอร์ดไหม?
        print(e.keysym)
        self.direction = e.keysym
        self.move_snake()


GUI = Tk() #T ใหญ่ k เล็ก
GUI.geometry('600x600')
GUI.title('เกมงู by ลุง')
GUI.resizable(False,False)

snake = Snake()
snake.pack()

GUI.mainloop()