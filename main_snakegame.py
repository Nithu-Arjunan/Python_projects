# Step 1 : Generate grid

grid_size = 10
snake = [(0,0)]

direction = {
    "W" : (-1,0), # move up
    "A" : (0,-1), # move left
    "S" : (1,0), # move down
    "D" : (0,1) # move right
}

def draw_grid(snake,food) :
    for i in range(grid_size):
        for j in range(grid_size):
            if (i,j) in snake:
                print("S",end=" ")
            elif (i,j) == food:
                print("F",end = " ")
            else :
                print(".", end =" ")
        print()

#draw_grid(snake,(4,5))

# Generate food randomly

import random

def generate_food(snake):
    while True:
        food = ((random.randint(0,grid_size-1)),(random.randint(0,grid_size-1)))
        if food not in snake :
            return food

food = generate_food(snake)

# Setting up the game 

while True:
    draw_grid(snake,food)
    move = input("Enter your move W/A/S/D").upper()
    if move not in direction:
        print("Wrong move.Please try again")
        continue

    # Calculate the head position 
    head = snake[-1]
    delta = direction[move]
    new_head = (head[0] + delta[0], head[1] + delta[1])

    if (
        new_head[0] < 0 or new_head[0]>=grid_size or
        new_head[1] < 0 or new_head[1]>=grid_size or
        new_head in snake
    ):
        print("Game over")
        break
    
    # Grow snake
    if new_head == food:
        snake.append(new_head)
        food = generate_food(snake)

    else :
        snake.append(new_head)
        snake.pop(0)

