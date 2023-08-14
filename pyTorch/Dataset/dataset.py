from torch.utils.data import Dataset
import cv2
import os

class myDataset(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(root_dir, label_dir)
        self.img_path = os.listdir(self.path)
    def __getitem__(self, index):
        img_name = self.img_path[index]
        item_path = os.path.join(self.path, img_name)
        img = cv2.imread(item_path)
        cv2.imshow(f"item{index}",img)
        cv2.waitKey(0)
        label = self.label_dir
        return img, label
    def __len__(self):
        return len(self.img_path)
    
root_dir = "hymenoptera_data/train"
ant_dir = "ants"
bee_dir = "bees"
ant_set = myDataset(root_dir, ant_dir)
bee_set = myDataset(root_dir, bee_dir)
ant_set.__getitem__(0)
bee_set.__getitem__(1)


