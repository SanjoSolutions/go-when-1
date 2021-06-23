import random


class GoWhen1:
    def __init__(self, number_of_steps_per_episode):
        self.number_of_steps_per_episode = number_of_steps_per_episode
        self.current_step = 0
        self.state = self._generate_state()
        self.reset()

    def reset(self):
        self.current_step = 0
        self.state = self._generate_state()

    def is_done(self):
        return self.current_step >= self.number_of_steps_per_episode

    def request_state(self):
        return self.state

    def act(self, action):
        reward = self._determine_reward(self.state, action)
        self.state = self._generate_state()
        self.current_step += 1
        return reward

    def _determine_reward(self, state, action):
        return 1 if state == action else 0

    def _generate_state(self):
        return random.choice((0, 1))
