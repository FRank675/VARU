# -*- coding: utf-8 -*-
# TODO: LQD 2019/10/23
# TODO: qq:743701947
from tensorflow.keras.callbacks import Callback
import matplotlib.pyplot as plt
import threading

temp_loss = []
temp_acc = []
temp_val_loss = []
temp_val_acc = []
flag_plot = True


def _thread_plot_all():
    global temp_loss, temp_acc, temp_val_loss, temp_val_acc, flag_plot
    fig = plt.figure('acc---------loss')
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax1.set_title('acc')
    ax1.set_xlabel('epoch')
    ax1.set_ylabel('acc')
    ax2.set_title('loss')
    ax2.set_xlabel('epoch')
    ax2.set_ylabel('loss')
    plt.ion()
    for i in range(100000):
        if flag_plot == True:
            try:
                ax1.lines.remove(lines1[0])
                ax1.lines.remove(lines2[0])
                ax2.lines.remove(lines3[0])
            except Exception as e:
                pass
            lines1 = ax1.plot(temp_acc, 'r-', label='acc')
            lines2 = ax1.plot(temp_val_acc, 'b-', label='val_acc')
            ax1.legend()
            lines3 = ax2.plot(temp_loss, 'r-', label='loss')
            ax2.legend()
            plt.pause(0.5)
    plt.ioff()
    # plt.show()


class SeeDnnTrain(Callback):
    def on_train_begin(self, logs={}):
        global temp_loss, temp_acc, temp_val_loss, temp_val_acc, flag_plot
        temp_loss = []
        temp_acc = []
        temp_val_loss = []
        temp_val_acc = []

    def on_epoch_end(self, epoch, logs={}):
        global temp_loss, temp_acc, temp_val_loss, temp_val_acc, flag_plot
        try:
            temp_loss.append(logs['loss'])
            temp_acc.append(logs['acc'])
            # temp_val_loss.append(logs['val_loss'])
            temp_val_acc.append(logs['val_acc'])

        except Exception as e:
            print(e)

    def on_train_end(self, logs={}):
        global temp_loss, temp_acc, temp_val_loss, temp_val_acc, flag_plot
        flag_plot = False
        temp_loss = []
        temp_acc = []
        temp_val_loss = []
        temp_val_acc = []


lr_see = SeeDnnTrain()


class MyThread(threading.Thread):
    def __init__(self, threadID, name, func):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.func = func

    def run(self):
        print('thread {} is started!'.format(self.threadID))
        self.func()


def visualization_of_deep_learning_training():
    t1 = MyThread(1, 'Thread-1', _thread_plot_all)
    t1.start()
    plt.show()
    
if __name__=='__main__':
    visualization_of_deep_learning_training()