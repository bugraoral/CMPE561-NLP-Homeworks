from collections import Counter

from hw1 import file_util

training_labels = file_util.read_line_list("training/_label")
test_labels = file_util.read_line_list("test/_label")

training_counter = Counter(training_labels)
test_counter = Counter(test_labels)

file_util.write_csv("training", training_counter)
file_util.write_csv("test", test_counter)
