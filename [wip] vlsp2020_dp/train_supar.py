import torch
from supar import Parser

# parser = Parser.load('biaffine-dep-en')
from torch import nn


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)

        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)


n_hidden = 128
n_letter = 20
n_categories = 10

names = {
    'en': ['Smith', 'Johnson', 'Williams'],
    'fr': ['Aimée', 'Antoinette', 'Bernadette']
}
rnn = RNN(n_letter, n_hidden, n_categories)

epochs = 100


def train():
    pass


def evaluate():
    pass


for epoch in range(1, epochs + 1):
    train()
    evaluate()
