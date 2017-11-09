import os, sys

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

subjects = ['bee', 'beetle', 'butterfly', 'cicada', 'cockroach', 'dragonfly', 'fly', 'grasshopper', 'mantis', 'wasp']
labels = list(subjects)

def get_filename(x, path):
    filename = ""
    if (x < 10):
        filename = "0" + str(x)
    else:
        filename = str(x)
    return path + filename + ".JPG"

def insect_identifier(filename, subject):
    # Read in the image_data
    image_data = tf.gfile.FastGFile(filename, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("output_graph/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        save_name = "" + subject + ".csv"
        res = open(save_name,'w+')
        res.close()
        res = open(save_name,'a+')
        i = 0
        for node_id in top_k:
            i = i + 1
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            # print('%s (score = %.5f)' % (human_string, score))
            if(human_string == subject):
                res.write(str(i) + "," + str(score) + "\n")

        res.close()

def process(subject):
    path = "test/" + subject + "/test"
    for x in range(1, 16):
        insect_identifier(get_filename(x, path), subject)

for label in labels:
    process(label)
