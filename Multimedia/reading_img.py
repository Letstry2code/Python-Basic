import cv2

im=cv2.imread('/workspaces/Python-Basic/Multimedia/im 1.png')
print(im.shape)
cv2.imshow('Image Window',im)
cv2.waitKey(0)