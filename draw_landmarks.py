import numpy as np 
import pylab as plt
import cv2
from matplotlib.font_manager import FontProperties
font0 = FontProperties()
# font0.set_size('small')
data = np.loadtxt('result.txt')
img = cv2.imread('pic.jpg')
img[:,:,[0,2]] = img[:,:,[2,0]]
print data.shape
fig,ax = plt.subplots()
plt.imshow(img)
ax.scatter(data[0::2],data[1::2],s=100,color='cyan')
for k in xrange(49):
	ax.annotate(str(k+1),(data[2*k],data[2*k+1]),color = 'green',horizontalalignment='center',verticalalignment='center',fontproperties=font0)
# plt.gca().invert_yaxis()
plt.axis('off')
plt.show()

