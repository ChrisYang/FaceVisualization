import matplotlib.delaunay as triang
import pylab as plt 
import cv2
import numpy as np 

def visualize_link(img,annotation,linetype='-*'):
    '''
    visualize the linked facial landmarks according to their physical locations 
    '''
    # plt.figure()
    plt.imshow(img)#show face image
    x = np.array(annotation[::2])-1#get x y coordinates
    y = np.array(annotation[1::2])-1
    star = linetype#plot style, such as '-*'
    plt.plot(x[0:17],y[0:17],star)# face contour 
    plt.plot(x[17:22],y[17:22],star)
    plt.plot(x[22:27],y[22:27],star)
    plt.plot(x[27:31],y[27:31],star)
    plt.plot(x[31:36],y[31:36],star)
    plt.plot(np.hstack([x[36:42],x[36]]),np.hstack([y[36:42],y[36]]),star)
    plt.plot(np.hstack([x[42:48],x[42]]),np.hstack([y[42:48],y[42]]),star)
    plt.plot(np.hstack([x[48:60],x[48]]),np.hstack([y[48:60],y[48]]),star)
    plt.plot(np.hstack([x[60:68],x[60]]),np.hstack([y[60:68],y[60]]),star)
    plt.axis('off')


def visualize_triang(img,annotation):
    '''
    visualize the facial landmarks by triangularizetion
    '''
    plt.imshow(img)
    x = np.array(annotation[::2])-1
    y = np.array(annotation[1::2])-1
    cens,ege,tri,neig =triang.delaunay(x,y)
    for t in tri:
        ti = [t[0],t[1],t[2],t[0]]
        plt.plot(x[ti],y[ti])


img = cv2.imread("example.jpg")
annotation = np.loadtxt('example.txt')
img[:,:,[0,2]] = img[:,:,[2,0]]
plt.figure(1)
visualize_link(img,annotation)
plt.figure(2)
visualize_triang(img,annotation)
plt.show()
