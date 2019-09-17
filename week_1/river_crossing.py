state_props = ["F", "G", "C", "W", "|"]
start_state = "FGCW|"
end_state = "|FGCW"
left_state = ""
right_state = ""
invalid_states = ("GW", "CG", "WG", "GW", "GCW", "CGW", "CWG", "WCG", "GWC")
previous_state = ""
moves = []

def move_left(move): 
    left_state = move
    #if is_safe(left_state):  
    possible_moves = next_moves(left_state)
    valid_moves = next_valid_moves(possible_moves, left_state)
    for move in possible_moves: 
        moves.append(move)
        # move_right(move)
    

def move_right(move):
    right_state = move
    possible_moves = next_moves(right_state)
    for move in possible_moves: 
        moves.append(move)
        move_left(move)
    return 

# helper function for checking if given state is valid
def is_safe(side_state, move):
    if side_state not in invalid_states:
        moves.append(move)
        return True
    else:
        moves.append(move)
        return False


def reached_end_state(state):
    if state[0] == end_state[0] and all(prop in state for prop in end_state):
        return True
    else:
        return False

def next_moves(state):
    next_moves = ["F"]
    state.replace("F", "")
    if state != "": 
        for prop in state:
            if prop != "|" and prop != "F":
                next_moves.append("F" + prop)
        print(next_moves)
        return next_moves
    else: 
        print(next_moves)
        return next_moves

def next_valid_moves(possible_moves, left_state):
    valid_moves = []
    state = left_state.replace("|", "")
    print(state)
    #check of wanner wij de possible_move uitvoeren de state die hieruit voortkomt nog een valide state is. zo ja, voeg hem toe aan valid_moves
    for prop in possible_moves:
        if prop not in invalid_states:
            print("adding valid move : " + prop)
            valid_moves.append(prop)
    return valid_moves

# start state begins on leftside
move_left(start_state)