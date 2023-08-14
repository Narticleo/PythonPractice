from torch.utils.tensorboard import SummaryWriter
import numpy as np
import cv2


writer = SummaryWriter("test")
img_path = "train/ants_image/649026570_e58656104b.jpg"
img = cv2.imread(img_path)
img_np = np.array(img)
shape = img_np.shape
writer.add_image("test", img_np.reshape(3, shape[0], shape[1]), 2)

writer.close()
