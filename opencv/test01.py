"""# 导入cv2模块
import cv2
# 给出本地图片的地址
img_dir="D:/360Downloads/test.jpg"
# 创建numpy类型的ndarray对象，存放多维数组的对象
img=cv2.imread(img_dir)
# <class 'numpy.ndarray'>
print(type(img))
# 水平翻转
flip_horizontal=cv2.flip(img,1)
# 垂直翻转
flip_vertical=cv2.flip(img,0)
# 水平加垂直翻转
flip_hv=cv2.flip(img,-1)
# 保存水平翻转图片
cv2.imwrite("save_dir.jpg",flip_horizontal)
# 保存垂直翻转图片
cv2.imwrite("save_dir02.jpg",flip_vertical)
# 保存水平加垂直翻转图片
cv2.imwrite("save_dir03.jpg",flip_hv)"""


