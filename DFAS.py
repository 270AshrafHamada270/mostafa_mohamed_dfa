# Define a class to represent a DFA
class DFA:
    def __init__(self, states, alphabet, transition, start_state, accept_states):
        self.states = states # List of states
        self.alphabet = alphabet # Input alphabet
        self.transition = transition # Transition function: (state, symbol) → next_state
        self.start_state = start_state # Start state
        self.accept_states = accept_states # Accept (final) states

# Function to check if two DFAs accept the same language
def are_equivalent(dfa1, dfa2):
    visited = [] # List to store visited state pairs
    queue = [] # Queue for BFS traversal

    start = (dfa1.start_state, dfa2.start_state) # Start from both DFAs' start states
    queue.append(start)
    visited.append(start)

# Breadth-first search through the combined DFA state space
    while queue:
        state1, state2 = queue.pop(0) # Get the next pair of states

        # Check if acceptance status is different between the two DFAs
        is_accepting1 = state1 in dfa1.accept_states
        is_accepting2 = state2 in dfa2.accept_states

        if is_accepting1 != is_accepting2:
            return False # They are not equivalent if one accepts and the other does not

        # Explore all symbols in the shared alphabet
        for symbol in dfa1.alphabet:
            if symbol in dfa2.alphabet:
                next1 = dfa1.transition.get((state1, symbol)) # Next state in DFA1
                next2 = dfa2.transition.get((state2, symbol)) # Next state in DFA2

                if next1 is None or next2 is None:
                    continue # If transition is missing, skip this symbol

                pair = (next1, next2)
                if pair not in visited:
                    visited.append(pair)
                    queue.append(pair) # Add new state pair to the queue

    return True # DFAs are equivalent


# DFA1
dfa1 = DFA(
    states=['q0', 'q1'],
    alphabet=['a', 'b'],
    transition={
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q0',
        ('q1', 'b'): 'q1'
    },
    start_state='q0',
    accept_states=['q0']
)

# DFA2
dfa2 = DFA(
    states=['s0', 's1'],
    alphabet=['a', 'b'],
    transition={
        ('s0', 'a'): 's1',
        ('s0', 'b'): 's0',
        ('s1', 'a'): 's0',
        ('s1', 'b'): 's1'
    },
    start_state='s0',
    accept_states=['s0']
)

# Print result: are the two DFAs equivalent?
result = are_equivalent(dfa1, dfa2)
print(" equal ? ", result)
