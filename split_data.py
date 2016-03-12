import os
import random
import shutil

TRAINING_DIR = "training"
TEST_DIR = "test"


def split_data(path="raw_texts", split_ratio=0.6):
    """
    Randomly splits the files on the given path by split ratio
    :param path: path to raw dataset
    :param split_ratio: float split ratio
    :return: puts the spliced files under to training/ and test/
    """
    authors = os.listdir(path)

    if os.path.exists(TRAINING_DIR):
        shutil.rmtree(TRAINING_DIR)

    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

    os.mkdir(TRAINING_DIR)
    os.mkdir(TEST_DIR)

    for author in authors:
        articalsDir = os.path.join(path, author)

        articals = os.listdir(articalsDir)

        random.shuffle(articals)

        sizeOfArticals = len(articals)

        for i in range(sizeOfArticals):

            if i < split_ratio * sizeOfArticals:
                shutil.copy2(articalsDir + '/' + articals[i], TRAINING_DIR + "/" + author + "_" + articals[i])
            else:
                shutil.copy2(articalsDir + '/' + articals[i], TEST_DIR + "/" + author + "_" + articals[i])

    training_size = len(os.listdir(TRAINING_DIR))
    test_size = len(os.listdir(TEST_DIR))
    print("Number of training instance = " + str(training_size))
    print("Number of test instance = " + str(test_size))

    print("Split ratio : " + str((training_size / (training_size + test_size))))


split_data()
