# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('456.png')
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

img_rbb = cv2.merge([r,b,b])
cv2.imwrite('rbb.png',img_rbb)
cv2.imshow('RBB',img_rbb)
cv2.imshow('opencv04',img)
cv2.waitKey(0)
cv2.destroyAllWindows()