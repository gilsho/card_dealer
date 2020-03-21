import flask
import random

app = flask.Flask(__name__)

def get_shuffled_deck():
  deck = random.shuffle(range(54))

suits = ['Club', 'Diamond', 'Spade', 'Heart']
cards = ['2', '3', '4', '5',
         '6', '7', '8', '9',
         '10', 'J', 'Q', 'K',
         'A']

def parse_card(card):
  suit = card // 13
  num = card  % 13
  return '{} {}'.format(
    cards[num], suits[suit])

@app.route('/health')
def hello_world():
  return 'Hello, World'

@app.route('/deal/<room>')
def deal_room(room):
  return '<br/>'.join([parse_card(c) for c in range(52)])

@app.route('/deal/<room>/<num>')
def retrieve_hand(room, num):
  return '{}/{}'.format(room, num)

if __name__ == '__main__':
  app.run()