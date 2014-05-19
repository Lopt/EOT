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
SLEEP_TIME = 60.0 / 60

ROUNDS = Calculate(centuries=2)
