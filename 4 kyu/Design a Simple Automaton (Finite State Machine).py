class Automaton(object):

    def __init__(self):
        self.states = []

    def read_commands(self, commands):
        for command in commands:
            if command is "1":
                if self.states[0]:
                    self.states[0] = False
                    self.states[1] = True
                elif self.states[2]:
                    self.states[2] = False
                    self.states[1] = True
            else:
                if self.states[1]:
                    self.states[1] = False
                    self.states[2] = True
                elif self.states[2]:
                    self.states[2] = False
                    self.states[1] = True
        return self.states[1]



my_automaton = Automaton()

q1 = True
q2 = False
q3 = False

my_automaton.states = [q1, q2, q3]

inp_list = ["1"]

print(my_automaton.read_commands(inp_list))



