def setup():
    size(7680,4320)
    background(167,103,24)
def draw():
    if mousePressed:
        line(mouseX, mouseY, pmouseX, pmouseY)
 
