        self.rnn1 = nn.RNN(input_size=60, hidden_size=1500, num_layers=1, dropout=1, batch_first=False)

        self.rnn2 = nn.RNN(input_size=1500, hidden_size=3000, num_layers=1, dropout=1, batch_first=False)
        self.rnn3 = nn.RNN(input_size=3000, hidden_size=20, num_layers=1, dropout=1, batch_first=False)

lr=1e-6