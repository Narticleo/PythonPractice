from torchvision import transforms
import cv2


img_path = "train/ants_image/0013035.jpg"
img = cv2.imread(img_path)
pic2tensor = transforms.ToTensor()

img_tensor = pic2tensor(img)
print(img)