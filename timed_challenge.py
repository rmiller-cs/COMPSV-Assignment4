# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
# 1. Rotate Right
# Rotate the values in a collection to the right by k steps.
# Input: [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate_right(list, steps):
    max = len(list) - 1
    end = (max - steps)
    current = (max - (steps - 1))
    new_list = []

    while current != end:

        if current == max:
            current == 0
        else:
            current = current + 1
        new_list.append(list[current])

    return new_list

cool_list = [1, 2, 3, 4, 5]

print(rotate_right(cool_list, 2))

# I was not able to complete my implementation in the time limit.
# I tried to use a list for my implementation, since it is easy to read specific elements of a list.
# I could simply iterate over the first list, starting at where the step count would place the first element of the list.
# I could then add each element to a new list and simply return that list.
# The time limit added onto the stress of my initial implementation not working. I could not figure out what was going wrong.
# My code either looped or did not provide the correct output. I believe it has something to do with the while loop.
# The time constraints meant I had to make my code simpler and had to use the first working idea I could come up with.
# The solution could be more refined, but the time constraints meant I had to give up on that.