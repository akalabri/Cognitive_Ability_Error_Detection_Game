import time
import random
from config import *


class Item:
    """
    Represents an item with shape, color, character, position, and an index.
    """
    def __init__(self, shape, color, character, pos, index):
        self.index = index
        self.shape = shape
        self.color = color
        self.character = character
        self.pos_x, self.pos_y = pos

    def __str__(self):
        return f"{self.color} {self.shape} in position {self.index + 1}"

    def draw(self):
        """
        Draw the item based on its shape and color.
        """
        if self.shape == "circle":
            circle_center = (self.pos_x + SIZE / 2, self.pos_y + SIZE / 2)
            radius = SIZE / 2
            pygame.draw.circle(WIN, colors[self.color], circle_center, radius)
        elif self.shape == "triangle":
            v1 = (self.pos_x, self.pos_y + SIZE)
            v2 = (self.pos_x + SIZE / 2, self.pos_y)
            v3 = (self.pos_x + SIZE, self.pos_y + SIZE)
            vertices = [v1, v2, v3]
            pygame.draw.polygon(WIN, colors[self.color], vertices)
        elif self.shape == "square":
            dimension = (self.pos_x, self.pos_y, SIZE, SIZE)
            pygame.draw.rect(WIN, colors[self.color], dimension, SIZE, 5)
        elif self.shape == "diamond":
            v1 = (self.pos_x, self.pos_y + SIZE / 2)
            v2 = (self.pos_x + SIZE / 2, self.pos_y)
            v3 = (self.pos_x + SIZE, self.pos_y + SIZE / 2)
            v4 = (self.pos_x + SIZE / 2, self.pos_y + SIZE)
            vertices = [v1, v2, v3, v4]
            pygame.draw.polygon(WIN, colors[self.color], vertices)
        elif self.shape == "pentagon":
            v1 = (self.pos_x + SIZE / 2, self.pos_y)
            v2 = (self.pos_x + SIZE, self.pos_y + SIZE / 2.5)
            v3 = (self.pos_x + 0.75 * SIZE, self.pos_y + SIZE)
            v4 = (self.pos_x + 0.25 * SIZE, self.pos_y + SIZE)
            v5 = (self.pos_x, self.pos_y + SIZE / 2.5)
            vertices = [v1, v2, v3, v4, v5]
            pygame.draw.polygon(WIN, colors[self.color], vertices)

    def add_char(self):
        """
        Add the character associated with the item to its center.
        """
        self.text = FONT.render(self.character, True, WHITE)
        text_width, text_height = self.text.get_size()
        char_x = self.pos_x + SIZE / 2 - text_width / 2
        char_y = self.pos_y + SIZE / 2 - text_height / 2
        WIN.blit(self.text, (char_x, char_y))


class Set:
    """
    Represents a set of items with random attributes.
    """
    def __init__(self):
        self.num_changes = random.randint(0, 9)
        self.changes_applied = self.num_changes
        self.set = []
        self.set_mod = []
        for i in range(9):
            shape = random.choice(shapes)
            color = random.choice(list(colors))
            char = random.choice(chars)
            pos = pos_1[i + 1]
            pos_mod = pos_2[i + 10]
            self.set.append(Item(shape, color, char, pos, i))
            self.set_mod.append(Item(shape, color, char, pos_mod, i))

    def __str__(self):
        set_description = ""
        for item in self.set:
            set_description += "\n" + item.__str__()
        return f"This set has {len(self.set)} items: {set_description}"

    def draw_set1(self):
        """
        Draw Set 1 with its items and characters.
        """
        for item in self.set:
            item.draw()
            item.add_char()

    def draw_set2(self):
        """
        Draw Set 2 with its items and characters.
        """
        for item in self.set_mod:
            item.draw()
            item.add_char()

    def apply_changes(self):
        """
        Apply random changes to Set 2 items.
        """
        random.shuffle(self.set_mod)
        change_index = 0
        change_type = ["shape", "color", "character"]

        while self.num_changes != 0:
            if self.num_changes == 1:
                item_changes = 1
            else:
                item_changes = random.randint(1, 2)
            selected_changes = random.sample(change_type, item_changes)

            for change in selected_changes:
                if change == "shape":
                    new_shape = random.choice(shapes)
                    while new_shape == self.set_mod[change_index].shape:
                        new_shape = random.choice(shapes)
                    self.set_mod[change_index].shape = new_shape
                elif change == "color":
                    new_color = random.choice(list(colors))
                    while new_color == self.set_mod[change_index].color:
                        new_color = random.choice(list(colors))
                    self.set_mod[change_index].color = new_color
                elif change == "character":
                    new_char = random.choice(chars)
                    while new_char == self.set_mod[change_index].character:
                        new_char = random.choice(chars)
                    self.set_mod[change_index].character = new_char

            self.num_changes -= item_changes
            change_index += 1


class Keys:
    """
    Represents the numeric keys used for answering.
    """
    def __init__(self):
        self.key_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.positions_keys = {}
        self.player_answer = None

    def get_positions(self):
        """
        Calculate positions for the numeric keys.
        """
        for row in range(2):
            for col in range(5):
                position_id = col + row * 5
                x = KEYS_ORIGIN_X + KEY_SIZE * col + OFFSET * (col + 1)
                y = KEYS_ORIGIN_Y + KEY_SIZE * row + OFFSET * (row + 1)
                self.positions_keys[position_id] = (int(x), int(y))

    def draw_keys(self):
        """
        Draw the numeric keys with their labels.
        """
        self.get_positions()
        for i in range(10):
            pos = self.positions_keys[i]
            pos_x = pos[0]
            pos_y = pos[1]
            dimension = (pos_x, pos_y, KEY_SIZE, KEY_SIZE)
            pygame.draw.rect(WIN, GREY, dimension)
            text = FONT.render(str(self.key_nums[i]), True, WHITE)
            num_x = pos_x + KEY_SIZE / 2 - 5
            num_y = pos_y + KEY_SIZE / 2 - 10
            WIN.blit(text, (num_x, num_y))

    def check_click(self):
        """
        Check if a numeric key is clicked and update the player's answer.
        """
        for i in range(10):
            pos = self.positions_keys[i]
            pos_x, pos_y = pos
            rect = pygame.Rect(pos_x, pos_y, KEY_SIZE, KEY_SIZE)
            if rect.collidepoint(pygame.mouse.get_pos()):
                self.player_answer = self.key_nums[i]  # Update player_answer when a key is clicked

class Timer:
    """
    Represents a countdown timer.
    """
    def __init__(self, duration_seconds):
        self.duration_seconds = duration_seconds
        self.start_time = time.time()

    def time_left(self):
        """
        Get the time left on the timer.
        """
        elapsed_time = time.time() - self.start_time
        return max(0, self.duration_seconds - elapsed_time)

    def is_time_up(self):
        """
        Check if the timer has run out.
        """
        return self.time_left() <= 0
