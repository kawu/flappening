import pickle

from datetime import datetime

from config import logging


class Logger:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, muted=False):
        super().__init__()

        self.data: dict = {'snapshots': [], 'score': 0}

        self.outpath = logging['record_path']

        self.muted = muted

    #  -------- Destruct -----------
    #
    def __del__(self):
        pass
        # self.write()

    #
    #
    #  -------- Write -----------
    #
    def write(self):

        if (self.muted):
            return

        fileName: str = str(self.data['score']) + '--' +  \
            str(datetime.now()) + '.pkl'

        f = open(self.outpath + fileName, 'wb')

        pickle.dump(self.data, f)

        f.close()

    #
    #
    #  -------- Read -----------
    #
    def read(self, path: str):

        f = open(path, 'rb')

        data = pickle.load(f)

        f.close()

        return data

    #  -------- update -----------
    #
    def update(self, data):
        self.data.update(data)

    #  -------- add Snapshot -----------
    #
    def addSnapshot(self, data):
        self.data['snapshots'].append(data)
