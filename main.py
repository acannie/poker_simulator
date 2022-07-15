from enum import Enum
import random

from card import Card

SUITS = ["♠", "♥", "♣", "♦"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
PLAYER_NUM = 6
HAND_NUM = 2
FLOP_NUM = 5
COMBINATION_RANK_NUM = 5


def init_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(Card(suit, rank))
    random.shuffle(deck)
    return deck


def init_hands(deck):
    hands = []
    for i in range(PLAYER_NUM):
        hands.append([])
        for j in range(HAND_NUM):
            card = deck.pop(0)
            hands[i].append(card)
    return hands


def init_flop(deck):
    flop = []
    for i in range(FLOP_NUM):
        card = deck.pop(0)
        flop.append(card)
    return flop


def judge(hands, flop):
    for hand in hands:
        flophand = flop + hand


def main():
    deck = init_deck()
    hands = init_hands(deck)
    flop = init_flop(deck)
    ranking = judge(hands, flop)
    print(ranking)


if __name__ == "__main__":
    main()
