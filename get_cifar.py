import numpy as np

import os
import urllib
import gzip
import pickle

def unpickle(file):
    fo = open(file, 'rb')
    dict = pickle.load(fo,encoding='bytes')
    fo.close()
    return dict[b'data'], dict[b'labels']

def cifar_generator(filenames, data_dir):
    all_data = []
    all_labels = []
    for filename in filenames:        
        data, labels = unpickle(data_dir + '/' + filename)
        all_data.append(data)
        all_labels.append(labels)

    images = np.concatenate(all_data, axis=0)
    labels = np.concatenate(all_labels, axis=0)
   
    return images,labels


def load(data_dir, subset='train'):
  if subset == 'train':
    return cifar_generator(['data_batch_1','data_batch_2','data_batch_3','data_batch_4','data_batch_5'],data_dir)
  elif subset == 'test':
    return cifar_generator(['test_batch'],data_dir)