import torch
import torch.nn as nn


class Brain(nn.Module):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, brain_size):

        super(Brain, self).__init__()

        # save parameters
        self.brain_size = brain_size

        # RNN
        # https://pytorch.org/docs/stable/nn.html#torch.nn.RNN
        self.fc1 = nn.RNN(2, self.brain_size)

        # Linear
        # https://pytorch.org/docs/stable/nn.html#torch.nn.Linear
        self.fc2 = nn.Linear(self.brain_size, 1)

        # Sigmoid
        # https://pytorch.org/docs/stable/nn.html#sigmoid
        self.ac1 = nn.Sigmoid()

    #
    #
    #  -------- Forward -----------
    #
    def forward(self, x):

        # apply RNN with reshape x[n,m] -> x[n,1,m]:
        x, _h = self.fc1(x.view(x.shape[0], 1, -1))

        # apply Linear with reshape x[n,1,m] -> x[n,m]:
        x = self.fc2(x.view(x.shape[0], -1))

        # apply Sigmoid
        x = self.ac1(x)

        return x

    #
    #
    #  -------- Think -----------
    #
    def think(self, data):

        x = torch.cat(
            (torch.FloatTensor([data[0]]), torch.FloatTensor(data[1])))

        x = self.forward(x)

        x = sum(x).item() / len(x)

        if (x > .5):
            return True

        return False
