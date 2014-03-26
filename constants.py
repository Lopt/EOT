# -*- coding: utf-8 -*-

# wie lange ein NPC benötigt, um ein Baum zu fällen
CHOPPING_TIME = 5
# wie lange es dauert, eh ein kleiner Baum (t) ausgewachsen ist (T)
GROW_TIME = 60
# wie lange es dauert, eh ein ausgewachsener Baum sich fortpflanzt
RESEED_TIME = 20

# Erhöhung = Die NPCs benötigen mehr Zeit um von a nach b zu kommen (niedriger als 1 derzeit nicht möglich)
WALK_FACTOR  = 1


# Weltgröße X, Y
WORLD_SIZE_X = 10
WORLD_SIZE_Y = 10

# anzahl der NPCs
NPCS = 3

# Namen der NPCs (Ein Zeichen = 1 Name) - kein großes T verwenden
NAMES = 100 * "ABCDEFGHIJLMNOPRSUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"

# wie lange zwischen zwei Runden gewartet werden soll -> je niedriger desto schneller läuft es
SLEEP_TIME = 0.5

# wie lang es gehen soll (Dauer ~= rounds * sleep_time in sekunden)
ROUNDS = 20000
