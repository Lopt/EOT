# -*- coding: utf-8 -*-

from logic.lifetime import Calculate

# Weltgröße X, Y
WORLD_SIZE_X = 10
WORLD_SIZE_Y = 10

# anzahl der NPCs
NPCS = 1

# Namen der NPCs (Ein Zeichen = 1 Name) - kein großes T verwenden
NAMES = 1000 * u"ABCDEFGHIJLMNOPRSUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"

# wie lange zwischen zwei Runden gewartet werden soll -> je niedriger desto schneller läuft es
SLEEP_TIME = 20.0 / 60
ROUNDS = Calculate(months=1)
TIME_PER_FRAME = Calculate(seconds=30)

HUMAN_LIFETIME = Calculate(days=10)
HUMAN_WALK_FACTOR = 30
HUMAN_FARMING_TIME = Calculate(minutes=15)
HUMAN_CHOPPING_TIME = Calculate(minutes=80)

TREE_GROW_TIME = Calculate(days=14)

FARM_GROW_TIME = Calculate(minutes=120)