import torch
import torch.nn as nn

# ensure brains are created identically every run
torch.manual_seed(42)


class Brain(nn.Module):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, brain_size):

        super(Brain, self).__init__()

        # save parameters
        self.brain_size = brain_size

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

        # apply Linear:
        x = self.fc2(x)

        # apply Sigmoid:
        x = self.ac1(x)

        return x

    #
    #
    #  -------- Think -----------
    #
    def think(self, data):

        with torch.no_grad():

            x = torch.FloatTensor(data)

            x = self.forward(x)

            if (x > .5):
                return True

            return False
