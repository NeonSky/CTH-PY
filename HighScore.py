import json
from collections import deque

class HighScore:
    latest_length = 5

    def __init__(self):
        save_file = self.get_file()
        self.score = 0
        try:
            self.save_data = json.loads(save_file.read())
            self.latest_deque = deque(self.save_data['latest'], self.latest_length)
        except ValueError:
            #json savefile was empty, create it and save it
            self.latest_deque = deque([], self.latest_length)
            self.save_data = {
                'latest': [elem for elem in self.latest_deque],
                'high_score': 0
            }
            save_file.write(json.dumps(self.save_data))

        save_file.close()

    def increase_score(self, amount):
        self.score += amount

    def reset_score(self):
        self.score = 0

    def save_score(self):
        #if deque is maximum length, an element from the other side is popped if something is appended
        self.latest_deque.appendleft(self.score)
        is_highscore = self.score > self.save_data['high_score']
        self.save_data = self.save_data = {
                'latest': [elem for elem in self.latest_deque],
                'high_score': self.score if is_highscore else self.save_data['high_score']
        }
        self.write_to_file()


    def get_file(self):
        return ""
        #return open("save.json", 'r+')

    def write_to_file(self):
        save_file = self.get_file()
        save_file.write(json.dumps(self.save_data))
        save_file.close()
