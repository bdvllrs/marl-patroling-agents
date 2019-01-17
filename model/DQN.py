import torch.nn as nn
from utils.config import Config

config = Config('./config')


class DQNUnit(nn.Module):

    def __init__(self):
        super(DQNUnit, self).__init__()

        n_actions = 7 if config.env.world_3D else 5
        self.n_agents = config.agents.number_preys + config.agents.number_predators
        self.fc = nn.Sequential(
            nn.Linear(self.n_agents * 6, 3 * self.n_agents),
            nn.ReLU(),
            nn.Linear(self.n_agents * 3, 2 * self.n_agents),
            nn.ReLU(),
            nn.Linear(2 * self.n_agents, n_actions),
        )

    # Called with either one element to determine next action, or a batch
    # during optimization. Returns tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        return self.fc(x)
