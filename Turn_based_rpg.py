import math
import tkinter as tk
from tkinter import ttk
import random
# ------------ Functions---------------------
def restart_game():
    global user_health, enemy_health, game_running
    user_health = 100
    enemy_health = 100

    user_hp_bar['value'] = 100
    enemy_hp_bar['value'] = 100
    user_emoji_label.config(text="(─‿‿─)")
    enemy_emoji_label.config(text="ᕦ(ò_óˇ)ᕤ")
    enemy_update_health_color()
    user_update_health_color()
    game_running = True
    log.config(state=tk.NORMAL)
    log.delete('1.0', tk.END)
    log.config(state=tk.DISABLED)
    enable_buttons()
    heal_button.config(state=tk.DISABLED)
    restart_button.config(state=tk.DISABLED)
    update_log('Game restarted. This is your chance. Select a move to fight!', 'neutral')

def update_log(message, tag):
    log.config(state=tk.NORMAL)
    log.insert(tk.END, message + "\n", tag)
    log.config(state=tk.DISABLED)
    log.yview(tk.END)

def disable_buttons():
    weak_button.config(state=tk.DISABLED)
    medium_button.config(state=tk.DISABLED)
    heal_button.config(state=tk.DISABLED)
    restart_button.config(state=tk.DISABLED)

def enable_buttons():
    weak_button.config(state=tk.NORMAL)
    medium_button.config(state=tk.NORMAL)
    heal_button.config(state=tk.NORMAL)

def user_update_health_color():
    if user_health > 50:
        user_style.configure("Green.Vertical.TProgressbar", troughcolor='grey', background='green')
        user_hp_bar.config(style="Green.Vertical.TProgressbar")
    elif 20 < user_health <= 50:
        user_style.configure("Yellow.Vertical.TProgressbar", troughcolor='grey', background='yellow')
        user_hp_bar.config(style="Yellow.Vertical.TProgressbar")
    else:
        user_style.configure("Red.Vertical.TProgressbar", troughcolor='grey', background='red')
        user_hp_bar.config(style="Red.Vertical.TProgressbar")

def enemy_update_health_color():
    if enemy_health > 50:
        enemy_style.configure("Green.Vertical.TProgressbar", troughcolor='grey', background='green')
        enemy_hp_bar.config(style="Green.Vertical.TProgressbar")
    elif 20 < enemy_health <= 50:
        enemy_style.configure("Yellow.Vertical.TProgressbar", troughcolor='grey', background='yellow')
        enemy_hp_bar.config(style="Yellow.Vertical.TProgressbar")
    else:
        enemy_style.configure("Red.Vertical.TProgressbar", troughcolor='grey', background='red')
        enemy_hp_bar.config(style="Red.Vertical.TProgressbar")

def player_health_stats():
    if user_health <= 0:
        user_emoji_label.config(text="(ಥ_ಥ)")
        enemy_emoji_label.config(text="ᕙ(☼.☼)ᕗ")
        update_log('The enemy has won! Too bad.', 'enemy')
        weak_button.config(state=tk.DISABLED)
        medium_button.config(state=tk.DISABLED)
        heal_button.config(state=tk.DISABLED)
        restart_button.config(state=tk.NORMAL)

    elif user_health <= 35:
        user_emoji_label.config(text="(;⚆_⚆)")
        update_log("\nYour turn:", 'user')
        user_update_health_color()
        enable_buttons()

    elif user_health >= 35:
        user_emoji_label.config(text="(─‿‿─)")
        update_log("\nYour turn:", 'user')
        user_update_health_color()
        enable_buttons()

    elif user_health == 100:
        user_emoji_label.config(text="(─‿‿─)")
        update_log("\nYour turn:", 'user')
        user_update_health_color()
        enable_buttons()
        heal_button.config(state=tk.DISABLED)

    else:
        user_emoji_label.config(text="(─‿‿─)")
        update_log("\nYour turn:", 'user')
        enable_buttons()

def enemy_health_stats():
    global user_exp
    if enemy_health <= 0:
        user_emoji_label.config(text="\ (•◡•) /")
        enemy_emoji_label.config(text=" (ಥ﹏ಥ) ")
        update_log('You Won! Congratulations!', 'user')
        user_exp += 30
        weak_button.config(state=tk.DISABLED)
        medium_button.config(state=tk.DISABLED)
        heal_button.config(state=tk.DISABLED)
        restart_button.config(state=tk.NORMAL)

    elif enemy_health <= 35:
        enemy_emoji_label.config(text="ᕙ(⇀‸↼‶)ᕗ")
        disable_buttons()
        root.after(1000, enemy_turn)  # Enemy turn after 1 second
        update_log("\nEnemy's turn:", 'enemy')

    elif enemy_health >= 35:
        enemy_emoji_label.config(text="ᕦ(ò_óˇ)ᕤ")
        disable_buttons()
        root.after(1000, enemy_turn)  # Enemy turn after 1 second
        update_log("\nEnemy's turn:", 'enemy')

    else:
        disable_buttons()
        root.after(1000, enemy_turn)  # Enemy turn after 1 second
        update_log("\nEnemy's turn:", 'enemy')

# ------------ GUI Beginning ---------------------
root = tk.Tk()
root.title("Turn-based RPG")
root.geometry("1000x400")
root.resizable(False, False)

# Stil für die EXP-Bar anpassen
user_style = ttk.Style()
user_style.theme_use('classic')  # Setze einen Standard-Stil
user_style.configure("Blue.Vertical.TProgressbar", troughcolor='grey', background='cyan', thickness=1)

# HP-Bar
user_hp_bar = ttk.Progressbar(root, length=160, mode='determinate', maximum=100)
user_hp_bar.pack(side=tk.LEFT, padx=30, pady=10, anchor='n')

# EXP-Bar mit Stil anwenden
user_exp_bar = ttk.Progressbar(root, length=160, mode='determinate', maximum=100)
user_exp_bar.place(x=30, y=31)
user_exp_bar.config(style="Blue.Vertical.TProgressbar")

enemy_style = ttk.Style()
enemy_style.theme_use('classic')
enemy_hp_bar = ttk.Progressbar(root, length=160, mode='determinate', maximum=100)
enemy_hp_bar.pack(side=tk.RIGHT, padx=30, pady=10, anchor='n')

# Example to set the initial health and exp values
user_health = 100
enemy_health = 100
user_exp = 0

user_hp_bar['value'] = user_health
user_exp_bar['value'] = user_exp
enemy_hp_bar['value'] = enemy_health

# Create a frame for the user below the HP bars
user_emoji_frame = tk.Frame(root)
user_emoji_frame.place(x=30, y=80)

# Add an emoji to a label and pack it within the frame
user_emoji_label = tk.Label(user_emoji_frame, text="(─‿‿─)", font=("Helvetica", 36))
user_emoji_label.pack()

# Create a frame for the enemy below the HP bars
enemy_emoji_frame = tk.Frame(root)
enemy_emoji_frame.place(x=790, y=80)

# Add an emoji to a label and pack it within the frame
enemy_emoji_label = tk.Label(enemy_emoji_frame, text="ᕦ(ò_óˇ)ᕤ", font=("Helvetica", 36))
enemy_emoji_label.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=10)

weak_button = tk.Button(button_frame, text="Weak Attack", command=lambda: user_move('weak'))
weak_button.pack(side=tk.LEFT, padx=10)

medium_button = tk.Button(button_frame, text="Medium Attack", command=lambda: user_move('medium'))
medium_button.pack(side=tk.LEFT, padx=10)

heal_button = tk.Button(button_frame, text="Heal", command=lambda: user_move('heal'))
heal_button.pack(side=tk.LEFT, padx=10)

restart_button = tk.Button(button_frame, text="Restart Fight!", command=restart_game)
restart_button.pack(side=tk.LEFT, padx=10)

# Log window
log = tk.Text(root, state=tk.DISABLED, width=75, height=15)
log.pack(pady=10)
# ------------ GUI End ---------------------
# ------------ Attacks and Game Loop ---------------------
move_dic = {
    'weak': list(range(16, 25)),
    'medium': list(range(10, 35)),
    'heal': list(range(15, 21)),
    'crit': list(range(30, 40))
}

crit_chance = 0.05
miss_chance = 0.01
game_running = True
# ------------ Player Function ---------------------
def user_move(move):
    global user_health, enemy_health, game_running
    if not game_running:
        return

    if move == 'weak':
        weak_atk = random.choice(move_dic['weak'])
        if random.random() < crit_chance:
            weak_atk *= 2
            update_log(f'Critical hit! You hit the enemy with {weak_atk} damage!', 'user')
        elif random.random() < miss_chance:
            weak_atk = 0
            update_log(f'Oh no...You missed you the attack!', 'user')
        else:
            update_log(f'You hit the enemy with {weak_atk} damage!', 'user')
        enemy_health -= weak_atk
        enemy_hp_bar['value'] = enemy_health
        enemy_health = min(100, max(enemy_health, 0))
        update_log(f"The enemy's current health is now {enemy_health}.", 'neutral')
        enemy_update_health_color()

    elif move == 'medium':
        med_atk = random.choice(move_dic['medium'])
        if random.random() < crit_chance:
            med_atk *= 2
            update_log(f'Critical hit! You hit the enemy with {med_atk} damage!', 'user')
        elif random.random() < miss_chance:
            med_atk = 0
            update_log(f'Oh no...You missed you the attack!', 'user')
        else:
            update_log(f'You hit the enemy with {med_atk} damage!', 'user')
        enemy_health -= med_atk
        enemy_hp_bar['value'] = enemy_health
        enemy_health = min(100, max(enemy_health, 0))
        update_log(f"The enemy's current health is now {enemy_health}.", 'neutral')
        enemy_update_health_color()

    elif move == 'heal':
        heal = random.choice(move_dic['heal'])
        user_health += heal
        user_hp_bar['value'] = user_health
        user_health = max(0, min(user_health, 100))
        user_emoji_label.config(text="(~˘▾˘)~")
        update_log(f"You've healed yourself by {heal} points!", 'user')
        update_log(f"Your current health is now {user_health}.", 'neutral')
        user_update_health_color()

    #else:
    #    update_log('You missed!', 'user')

    user_hp_bar['value'] = user_health
    user_update_health_color()
    enemy_health_stats()

# ------------ Enemy Function ---------------------
def enemy_turn():
    global user_health, enemy_health, game_running
    if not game_running:
        return

    if enemy_health < 35:
        moves = ['weak', 'medium', 'heal']
        chance = [0.3, 0.2, 0.5]
    else:
        moves = ['weak', 'medium', 'heal']
        chance = [0.6, 0.3, 0.1]

    enemy_move = random.choices(moves, chance)[0]
    if enemy_move == 'weak':
        weak_atk = random.choice(move_dic['weak'])
        if random.random() < crit_chance:
            weak_atk *= 2
            update_log(f'Critical hit! The enemy did {weak_atk} damage!', 'enemy')
        elif random.random() < miss_chance:
            weak_atk = 0
            update_log(f'The enemy missed the attack. Lucky you!', 'enemy')
        else:
            update_log(f'The enemy hit you with {weak_atk} damage!', 'enemy')
        user_health -= weak_atk
        user_hp_bar['value'] = user_health
        user_health = min(100, max(user_health, 0))
        update_log(f"Your current health is now {user_health}.", 'neutral')
        user_update_health_color()

    elif enemy_move == 'medium':
        med_atk = random.choice(move_dic['medium'])
        if random.random() < crit_chance:
            med_atk *= 2
            update_log(f'Critical hit! The enemy did {med_atk} damage!', 'enemy')
        elif random.random() < miss_chance:
            med_atk = 0
            update_log(f'The enemy missed the attack. Lucky you!', 'enemy')
        else:
            update_log(f'The enemy hit you with {med_atk} damage!', 'enemy')
        user_health -= med_atk
        user_hp_bar['value'] = user_health
        user_health = min(100, max(user_health, 0))
        update_log(f"Your current health is now {user_health}.", 'neutral')
        user_update_health_color()

    elif enemy_move == 'heal':
        heal = random.choice(move_dic['heal'])
        enemy_health += heal
        enemy_hp_bar['value'] = enemy_health
        enemy_health = max(1, min(enemy_health, 100))
        enemy_emoji_label.config(text="~(˘▾˘~)")
        update_log(f"The enemy healed itself by {heal} points!", 'enemy')
        update_log(f"The enemy's current health is now {enemy_health}.", 'neutral')
        enemy_update_health_color()

    #else:
    #   update_log('The enemy missed the attack!', 'enemy')
    enemy_hp_bar['value'] = enemy_health
    enemy_update_health_color()
    player_health_stats()

# ------------ Log Window Stuff ---------------------
# Configure tags for different colors
log.tag_configure('user', foreground='blue')
log.tag_configure('enemy', foreground='red')
log.tag_configure('neutral', foreground='black')

# Add initial message to the log
update_log("You have entered a dark cavern. Something in this room is approaching you. Select your move!", 'neutral')
restart_button.config(state=tk.DISABLED)
heal_button.config(state=tk.DISABLED)
user_update_health_color()
enemy_update_health_color()

# Start the Tkinter main loop
root.mainloop()

# ziele:
# mehr gegner
# level ups
# neue attacken nach 100 exp
# shop alle 5 runden