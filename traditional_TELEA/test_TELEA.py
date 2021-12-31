import cv2
import os

img_path = r'./test_img/img_3_3.png'
mask_path = r'./test_mask/mask_3_3.png'
save_path = r'./test_output'


src = cv2.imread(img_path)
mask = cv2.imread(mask_path)
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("./test.png", mask)

#src = cv2.resize(src,(500,300),interpolation=cv2.INTER_CUBIC)
#mask = cv2.resize(mask,(500,300),interpolation=cv2.INTER_CUBIC)
res = cv2.inpaint(src, mask, 3, cv2.INPAINT_TELEA)

print("save_path:", os.path.join(save_path, 'out_'+img_path.split('/')[-1]))
cv2.imwrite(os.path.join(save_path, 'out_'+img_path.split('/')[-1]), res)
