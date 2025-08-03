def player(prev_play, opponent_history=[]):
    import random

    # Store opponent moves
    if prev_play:
        opponent_history.append(prev_play)

    # Return 'R' for the first few rounds to collect data
    if len(opponent_history) < 5:
        return "R"

    # Detect repeating patterns (like Quincy)
    seq_len = 5
    if len(opponent_history) > seq_len:
        recent = opponent_history[-seq_len:]
        for i in range(len(opponent_history) - seq_len):
            if opponent_history[i:i+seq_len] == recent:
                next_index = (i + seq_len) % len(opponent_history)
                if next_index < len(opponent_history):
                    predicted = opponent_history[next_index]
                    return counter_move(predicted)

    # Detect Abbey (she plays the move that beats our last move)
    if len(opponent_history) >= 2:
        if opponent_history[-1] == counter_move(opponent_history[-2]):
            # If opponent keeps playing the counter to our last move, flip the logic
            predicted = counter_move(opponent_history[-1])
            return counter_move(predicted)

    # Default to frequency analysis (for Mrugesh)
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1
    predicted = max(freq, key=freq.get)
    return counter_move(predicted)

def counter_move(move):
    return {"R": "P", "P": "S", "S": "R"}[move]
