# Pythona spēle

## Piece code to move rectangle "cubee"
```
def MoveCube(direction):
    global xx, yy, cubee
    if direction == 'UP':
        yy -= 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
    if direction == 'RIGHT':
        xx += 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
    if direction == 'DOWN':
        yy += 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
    if direction == 'LEFT':
        xx -= 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
```