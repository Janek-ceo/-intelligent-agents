from mesa import Agent, Model
from mesa.time import RandomActivation

class BasicAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy = 10

    def step(self):
        if self.energy > 0:
            self.energy -= 1
            print(f"Agent {self.unique_id} performed action. Energy left: {self.energy}")

class BasicModel(Model):
    def __init__(self, num_agents):
        self.schedule = RandomActivation(self)
        for i in range(num_agents):
            agent = BasicAgent(i, self)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()

if __name__ == "__main__":
    model = BasicModel(5)
    for i in range(10):
        print(f"Step {i}")
        model.step()
