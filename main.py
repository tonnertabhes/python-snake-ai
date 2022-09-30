from tkinter import *
from random import randint
import time

snake_pos = [[250, 250]]
food_pos = [randint(1, 49) * 10, randint(1, 49) * 10]
direction = "DOWN"
score = 0
high_score = 0
game_over = False
menu = True
difficulty = 120

window = Tk()
window.title("Snake Game")
window.geometry("500x500")
window.resizable(width=False, height=False)
canvas = Canvas(window, width=500, height=500, bg="#000")
canvas.pack()


def key_pressed(e):
    global direction
    global game_over
    global snake_pos
    global food_pos
    global score
    global menu
    
    if e.keysym == "Escape" and menu == False and game_over == True:
        menu = True
        draw_menu()
        update()
        return
    
    if e.keysym == "Return" and game_over == True:
        snake_pos = [[250, 250]]
        food_pos = [randint(1, 49) * 10, randint(1, 49) * 10]
        direction = "DOWN"
        score = 0
        game_over = False
        window.after(30, update)
        canvas.delete("gameover")
        draw_food()
        draw_score()
        return
    
    if e.keysym == "Up" and direction != "DOWN":
        direction = "UP"
        return direction
        
    if e.keysym == "Down" and direction != "UP":
        direction = "DOWN"
        return direction
        
    if e.keysym == "Left" and direction != "RIGHT":
        direction = "LEFT"
        return direction
        
    if e.keysym == "Right" and direction != "LEFT":
        direction = "RIGHT"
        return direction


def move_snake():
    global snake_pos
    global game_over
        
    if direction == "DOWN":
        newpos = [[snake_pos[0][0], snake_pos[0][1] + 10]]
        if newpos[0] not in snake_pos:
            for i in snake_pos:
                newpos.append(i)
            if newpos[0] == food_pos:
                snake_pos = newpos
                return snake_pos
            newpos.pop()
            snake_pos = newpos
            return snake_pos
        game_over = True
    
    if direction == "UP":
        newpos = [[snake_pos[0][0], snake_pos[0][1] - 10]]
        if newpos[0] not in snake_pos:
            for i in snake_pos:
                newpos.append(i)
            if newpos[0] == food_pos:
                snake_pos = newpos
                return snake_pos
            newpos.pop()
            snake_pos = newpos
            return snake_pos
        game_over = True
    
    if direction == "LEFT":
        newpos = [[snake_pos[0][0] - 10, snake_pos[0][1]]]
        if newpos[0] not in snake_pos:
            for i in snake_pos:
                newpos.append(i)
            if newpos[0] == food_pos:
                snake_pos = newpos
                return snake_pos
            newpos.pop()
            snake_pos = newpos
            return snake_pos
        game_over = True
        
    if direction == "RIGHT":
        newpos = [[snake_pos[0][0] + 10, snake_pos[0][1]]]
        if newpos[0] not in snake_pos:
            for i in snake_pos:
                newpos.append(i)
            if newpos[0] == food_pos:
                snake_pos = newpos
                return snake_pos
            newpos.pop()
            snake_pos = newpos
            return snake_pos
        game_over = True
        

def draw_food():
    canvas.delete("food")
    canvas.create_rectangle(food_pos[0], food_pos[1], food_pos[0] - 10, food_pos[1] - 10, fill="purple", tags="food")

def draw_snake():
    global food_pos
    global snake_pos
    global score
    global high_score
    
    canvas.delete("snake")
    if snake_pos[0] == food_pos:
        food_pos = [randint(1, 49) * 10, randint(1, 49) * 10]
        score += 1
        draw_score()
        if score >= high_score:
            high_score = score
            draw_high_score()
        draw_food()
    for i in snake_pos:
        canvas.create_rectangle(i[0], i[1], i[0] - 10, i[1] - 10, fill="red", tags="snake")

def draw_score():
    canvas.delete("score")
    canvas.create_text(30, 15, fill="#FFF", text="Score: " + str(score), tags="score")
    
def draw_high_score():
    canvas.delete("highscore")
    canvas.create_text(45, 30, fill="#FFF", text="High Score: " + str(high_score), tags="highscore")

def draw_menu():
    global game_over
    game_over = False
    canvas.delete("score")
    canvas.delete("highscore")
    canvas.delete("snake")
    canvas.delete("food")
    canvas.delete("gameover")
    canvas.create_text(250, 150, font=("Arial", 50), text="Main Menu", fill="#FFF", tags='menu')
    canvas.create_text(250, 190, font=("Arial", 10), text="Select Difficulty (Use Number Keys)", fill="#FFF", tags='menu')
    canvas.create_text(250, 250, font=("Arial", 10), text="1 - Easy\n2 - Medium\n3 - Hard", fill="#FFF", tags='menu')

def select_difficulty(e):
    global menu
    global difficulty
    if menu == True:
        if e.keysym == "1":
            difficulty = 90
            reset()
        if e.keysym == "2":
            difficulty = 60
            reset()
            return
        if e.keysym == "3":
            difficulty = 30
            reset()
            return
            
def draw_game_over():
    canvas.create_text(250, 250, fill="#FFF", text="GAME OVER", width=500, font=("Arial", 25), tags="gameover")
    canvas.create_text(250, 280, fill="#FFF", text="Press Enter to play again.", tags="gameover")
    canvas.create_text(250, 300, fill="#FFF", text="Press Esc to change difficulty.", tags="gameover")
            
def reset():
    global menu
    global game_over
    global snake_pos
    global food_pos
    global direction
    global score
    
    menu = False
    game_over = False
    snake_pos = [[250, 250]]
    food_pos = [randint(1, 49) * 10, randint(1, 49) * 10]
    direction = "DOWN"
    score = 0
    time.sleep(0.05)
    canvas.delete("menu")
    canvas.delete("gameover")
    draw_food()
    draw_score()
    draw_high_score()
    update()  

def update():
    global game_over

    #Checking state of game
    if menu == True:
        draw_menu()
        return
    if game_over == True:
        draw_game_over()
        return
    
    #Checking to see if snake is within game boundaries
    if snake_pos[0][0] >= 500 or snake_pos[0][0] <= 0:
        game_over = True
    if snake_pos[0][1] >= 500 or snake_pos[0][1] <= 0:
        game_over = True
        
    #Updating frame
    draw_snake()
    move_snake()
    window.after(difficulty, update)

window.bind("<Up>", key_pressed)
window.bind("<Down>", key_pressed)
window.bind("<Left>", key_pressed)
window.bind("<Right>", key_pressed)
window.bind("<Return>", key_pressed)
window.bind("<Escape>", key_pressed)
window.bind(1, select_difficulty)
window.bind(2, select_difficulty)
window.bind(3, select_difficulty)

draw_score()
draw_high_score()
draw_food()
window.after(difficulty, update())
window.mainloop()

