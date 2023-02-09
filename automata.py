def create_dfa(transitions, initial_state, accepting_states):
    def is_accepted(state, word):
        if word == "":
            return state in accepting_states
        else:
            letter = word[0]
            if (state, letter) in transitions:
                return is_accepted(transitions[(state, letter)], word[1:])
            else:
                return False
    return is_accepted

dfa1_transitions = {
    (0, 'a'): 1, (0, 'b'): 2, (0, 'c'): 3,
    (1, 'a'): 2, (1, 'b'): 3, (1, 'c'): 1,
    (2, 'a'): 3, (2, 'b'): 1, (2, 'c'): 3,
}
dfa1_initial_state = 0
dfa1_final_states = [3]

dfa2_transitions = {
    (0, 'a'): 4, (0, 'c'): 1, (1, 'c'): 3,
    (4, 'a'): 4, (4, 'b'): 8, (4, 'c'): 1,
    (6, 'b'): 8, (8, 'b'): 6,
}
dfa2_initial_state = 0
dfa2_final_states = [3, 4, 6, 8]

dfa3_transitions = {
    (0, 'a'): 7, (2, 'b'): 8, (3, 'b'): 8,
    (3, 'c'): 4, (4, 'b'): 8, (4, 'c'): 3,
    (7, 'a'): 7, (7, 'b'): 2, (8, 'b'): 8,
    (8, 'c'): 4,
}
dfa3_initial_state = 0
dfa3_final_states = [7, 8]

dfa4_transitions = {
    (0, 'f'): 10, (10, 'c'): 0,
}
dfa4_initial_state = 0
dfa4_final_states = [10]

dfas = [
    (dfa1_transitions, dfa1_initial_state, dfa1_final_states),
    (dfa2_transitions, dfa2_initial_state, dfa2_final_states),
    (dfa3_transitions, dfa3_initial_state, dfa3_final_states),
    (dfa4_transitions, dfa4_initial_state, dfa4_final_states)
]

end = False
def automata():
    print("Choose a DFA:")
    for i, dfa in enumerate(dfas):
        print(f"{i + 1}. {'Accepts words of the form abc' if i == 0 else 'Accepts words of the form abc' if i == 1 else 'Accepts words of the form abc' if i == 2 else 'Accepts words of the form cfd'}")

    selected_dfa = dfas[int(input("Enter a number: ")) - 1]

    word = input("Enter a word: ")

    dfa = create_dfa(*selected_dfa)

    if dfa(selected_dfa[1], word):
        print("The word is correct.")
    else:
        print("The word is incorrect.")

automata()

while not end:
    answer = input("Do you want to enter another word? Y / N ")

    if answer == "y":
        automata()

    elif answer == "n":
        print("Ah bueno garcias")
        end = True

    else:
        print("Hijole, no se puede mi pana, ingresa Y o N")