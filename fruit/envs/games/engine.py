
class BaseEngine(object):
    def get_game_name(self):
        pass

    def clone(self):
        pass

    def get_num_of_objectives(self):
        pass

    def get_num_of_agents(self):
        pass

    def reset(self):
        pass

    def step(self, action):
        pass

    def render(self):
        pass

    def get_state(self):
        pass

    def is_terminal(self):
        pass

    def get_state_space(self):
        pass

    def get_action_space(self):
        pass

    def get_num_of_actions(self):
        pass