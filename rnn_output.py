import tensorflow as tf
import numpy as np
import my_txtutils

INTERNALSIZE = 512
ALPHASIZE = my_txtutils.ALPHASIZE
NLAYERS = 3
# 10 Epoch regulation save files
eu_regs_10 = "checkpoints/rnn_train_1555479917-459000000"
can_regs_10 = "checkpoints2/rnn_train_1555639791-291000000"
eu_can_regs_10 = "checkpoints3/rnn_train_1555802511-753000000"

# 5 Epoch regulation save files
eu_regs_5 = "checkpoints/rnn_train_1555479917-234000000"
can_regs_5 = "checkpoints2/rnn_train_1555639791-147000000"
eu_can_regs_5 = "checkpoints3/rnn_train_1555802511-387000000"

n_count = 0 # counter for spacing
with open('EU_Regulations_5_epochsabc.txt', 'w+') as file_output:
    with tf.Session() as sess:
        input_file = tf.train.import_meta_graph('checkpoints/rnn_train_1555479917-0.meta')
        input_file.restore(sess, eu_regs_5)
        x = my_txtutils.convert_from_alphabet(ord("L")) #
        x = np.array([[x]])  # shape [BATCHSIZE, SEQLEN] with BATCHSIZE=1 and SEQLEN=1

        # initial values
        y = x
        h_in = np.zeros([1, INTERNALSIZE * NLAYERS], dtype=np.float32)  # [ BATCHSIZE, INTERNALSIZE * NLAYERS]
        for i in range(15000): # number of characters to output
            output, h_in = sess.run(['Yo:0', 'H:0'], feed_dict={'X:0': y, 'pkeep:0': 1., 'Hin:0': h_in, 'batchsize:0': 1})
            character = my_txtutils.sample_from_probabilities(output, topn=2) #choose 1 of top 2 characters
            y = np.array([[character]])  # shape [BATCHSIZE, SEQLEN] with BATCHSIZE=1 and SEQLEN=1
            character = chr(my_txtutils.convert_to_alphabet(character))
            file_output.write(character)
            print(character, end="")

            if character == '\n':
                n_count = 0
            else:
                n_count += 1
            if n_count == 100: #if 100 characters pass without a new line, break up the text.
                print("")
                n_count = 0
