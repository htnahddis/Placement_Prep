class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def meeting_room(start, end):
    meetings = [Meeting(start[i], end[i]) for i in range(len(start))]

    # Sort meetings by end time
    meetings.sort(key=lambda x: x.end)
    
    count = 1  # At least one meeting can be held
    last_end_time = meetings[0].end
    
    for i in range(1, len(meetings)):
        if meetings[i].start >= last_end_time:
            count += 1
            last_end_time = meetings[i].end

    return count

# Example usage
start = [0, 1, 2, 4, 6, 7]
end = [1, 3, 4, 5, 8, 9]
print(meeting_room(start, end))  # Output: 4