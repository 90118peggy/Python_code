import cv2
from PIL import Image

### 先將輸入的圖片切成825小份，並將其存在於資料夾中
#透過預處理圖片我們已經得知圖片是829x256像素

def cut_image(image):
    w, h = image.size
    print(w, h)
    item_w = int(w/825)
    box_list = []
    for i in range(825):
        box = (i*item_w, 0, (i+1)*item_w, h)
        box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    print(len(image_list))
    return image_list

def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('D:/python test/img/'+str(index)+'.png', 'PNG')
        index += 1

if __name__ == '__main__':
    file_path = "C:/Users/Pei/Downloads/new_at.png"
    image = Image.open(file_path)

    image_list = cut_image(image)
    save_images(image_list)

### 接著讀入每張小圖中的藍色的點，紀錄藍色點的位置，將他們收集起來、用matplotlib印出來


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

Img_FOLDER = 'D:/python test/img'

list_y = []

for i in range(825):
    img = cv2.imread('D:/python test/img/'+str(i+1)+'.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([90, 50, 50])
    high_hsv = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lowerb = low_hsv, upperb = high_hsv)
    dst = cv2.GaussianBlur(mask, (3, 3), 0)
    yx = np.column_stack(np.where(mask==255))
    yx = 256-yx
    if yx.size == 0:
        continue
    y = np.max([yx[:, 0]])
    y_new = y*16/256
    list_y.append(y_new)

list_x = np.arange(0, 5.544, 0.00672)
x_major_locator = MultipleLocator(0.1)
y_major_locator = MultipleLocator(0.5)

plt.figure(figsize=(21, 4.8))
plt.plot(list_x, np.array(list_y), label='first', linewidth=2, color='b')
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.hlines(y=14, xmin=3.0, xmax=5, colors='r')
plt.hlines(y=5.9, xmin=3.0, xmax=5, colors='r')
plt.vlines(x=3.09, ymin=0, ymax=16)
plt.vlines(x=4.88, ymin=0, ymax=16)
plt.title('a-t Figure')
plt.xlabel('t(s)')
plt.ylabel('a(m/s^2)')
plt.xlim(0, 5.6)
plt.ylim(0, 16)
plt.grid()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

### 取穩定震盪下的時間區間(3.0-5.0)，搭配看圖並計算波峰時的時間

for x in list_x:
    if (x>3.0 and x<5.0):
        y_value = list_y[list(list_x).index(x)]
        if y_value>13.8:
            print(y_value, x)

print('週期為:', np.round((4.872-3.08448)/6, 2))