import cache
import config
import flask
import random

EXPIRATION_SECONDS = 60 * 15

app = flask.Flask(__name__)

def get_shuffled_deck():
  deck = list(range(52))
  random.shuffle(deck)
  return deck

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
  if cache.mc.get(room):
    return 'Dealing cards in progress.'
  deck = get_shuffled_deck()
  cache.mc.set(room, {
    1: deck[:13],
    2: deck[13:26],
    3: deck[26:39],
    4: deck[39:52], 
  }, time=EXPIRATION_SECONDS)
  return '''Hands are available at the following urls:
    <ul>
      <li><a href='{url1}'>Hand 1</a></li>
      <li><a href='{url2}'>Hand 2</a></li>
      <li><a href='{url3}'>Hand 3</a></li>
      <li><a href='{url4}'>Hand 4</a></li>
    </ul>
    '''.format(
      url1=flask.url_for('.retrieve_hand', room=room, num=1),
      url2=flask.url_for('.retrieve_hand', room=room, num=2),
      url3=flask.url_for('.retrieve_hand', room=room, num=3),
      url4=flask.url_for('.retrieve_hand', room=room, num=4))


@app.route('/deal/<room>/hands/<num>')
def retrieve_hand(room, num):
  deck_by_hand = cache.mc.get(room)
  if not deck_by_hand:
    return 'Error. deck hasn\'t been dealt!'
  hand = deck_by_hand.pop(int(num), None)
  if not hand:
    return 'Error. Hand already dealt.'
  hand.sort()
  cache.mc.set(room, deck_by_hand, time=EXPIRATION_SECONDS)
  return 'Your hand is: <ul>{}</ul>'.format(
    '\n'.join(
      ['<li>{}</li>'.format(parse_card(card)) for card in hand]
    )
  )

if __name__ == '__main__':
  app.run()