# -*- coding: utf-8 -*-

from logic.lifetime import Calculate

# Weltgröße X, Y
WORLD_SIZE_X = 60
WORLD_SIZE_Y = 118

# anzahl der NPCs
NPCS = 1000

# Namen der NPCs (Ein Zeichen = 1 Name) - kein großes T verwenden
NAMES = 1000 * u"ABCDEFGHIJLMNOPRSUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"

# wie lange zwischen zwei Runden gewartet werden soll -> je niedriger desto schneller läuft es
SLEEP_TIME = 1.0 / 60

ROUNDS = Calculate(centuries=2)
