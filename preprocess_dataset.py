import glob, os, random
from shutil import copy2

base_path = 'data/Cropped_Images/'
test_path = 'data/test/'
train_path = 'data/train/'
classes_list = glob.glob(os.path.join(base_path, '*'))

for cls in classes_list:

    _, cls_name = os.path.split(cls)

    img_list = glob.glob(os.path.join(cls, '*.jpg'))
    split = int(len(img_list) * 0.9)
    random.shuffle(img_list)
    train = img_list[:split]
    test = img_list[split:]

    new_train_path = os.path.join(train_path, cls_name)
    new_test_path = os.path.join(test_path, cls_name)

    for file in train:
        _, file_name = os.path.split(file)
        new_file_path = os.path.join(new_train_path, file_name)
        copy2(file, new_file_path)


    for file in test:
        _, file_name = os.path.split(file)
        new_file_path = os.path.join(new_test_path, file_name)
        copy2(file, new_file_path)




