# p09
names =['1','2','3']
for name in names:
    print(name)
background(0,0,255)
size(300,300)
for i in range(len(names)):
    text(names[i],i*100,100)
