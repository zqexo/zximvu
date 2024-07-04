def filter_participants(participants, keywords):
    return [part for part in participants if any(word in part.username for word in keywords)]

def sort_participants(participants):
    return sorted(participants, key=lambda x: x.username)

def get_top_participants(participants, top_n):
    return participants[:top_n]

def print_participants(participants):
    for part in participants:
        print(part)
