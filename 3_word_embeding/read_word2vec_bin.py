# coding: utf-8
import struct
import sys

def load_word2vec(vecotr_path="word2vec/vectors.bin"):

    FILE_NAME =vecotr_path
    FLOAT_SIZE = 4
    vectors = dict()

    with open(FILE_NAME, 'rb') as f:

        c = None
        header = ""
        while c != "\n":
            c = f.read(1)
            header += c

        total_num_vectors, vector_len = (int(x) for x in header.split())
        num_vectors = total_num_vectors


        while len(vectors) < num_vectors:

            word = ""
            while True:
                c = f.read(1)
                if c == " ":
                    break
                word += c

            binary_vector = f.read(FLOAT_SIZE * vector_len)
            vectors[word] = [ struct.unpack_from('f', binary_vector, i)[0]  for i in xrange(0, len(binary_vector), FLOAT_SIZE) ]


    for item in vectors:
        print item,":",vectors[item]
    return vectors
load_word2vec()
