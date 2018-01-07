def add_to_all(tuple,val):
    for i in range(len(tuple)):
        tuple[i] += 1

# när vi ändrar listor på ett ställe så ändras på alla ställen (uppgift Muterbarhet). när vi ändrar på tal så ändrar vi egentligen deras kopia. Det är därför vi kan ha tal som nycklar fast ej listor.

board = {(1, 2): 'spelare1', (1, 3): 'spelare1', (2, 3):"spelare2"}
for pos in board:
            avstånd = (pos[0] - x)**2 + (pos[1] - y)**2
        minsta_avstånd = min(pos.avstånd)
