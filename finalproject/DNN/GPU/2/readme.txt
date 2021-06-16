        self.linear = nn.Sequential(
            nn.Linear(60, 100),
            nn.Linear(100, 200),
            nn.Linear(200, 500),
            nn.Linear(500, 1000),
            nn.Linear(1000, 400),
            nn.Linear(400, 200),
            nn.Linear(200, 80),
            nn.Linear(80, 40),
            nn.Linear(40, 20),
            nn.Linear(20, 1),

lr=1e-6