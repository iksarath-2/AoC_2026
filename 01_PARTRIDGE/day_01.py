# --- Day 1: Secret Entrance ---
#
# The Elves have good news and bad news.
#
# The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.
# 
# The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!
# 
# To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:
# 
# "Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."
# 
# The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.
# 
# The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.
# 
# So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.
# 
# Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.
# 
# So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.
# 
# The dial starts by pointing at 50.
# 
# You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.
# 
# Analyze the rotations in your attached document. What's the actual password to open the door?
#
#
# --- Part Two ---
#
# You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.
# 
# As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:
# 
# "Due to newer security protocols, please use password method 0x434C49434B until further notice."
# 
# You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.
# 
# Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!
# 
# Using password method 0x434C49434B, what is the password to open the door?

import pandas as pd    # for CSV reading

df = pd.read_csv("01_PARTRIDGE/d01_input.txt", header=None, index_col=None)    # read input data into data frame
data = df.to_numpy()    # convert data frame to numpy array
current = 50    # set initial value of the dial (50 as given)
count_part_1 = 0    # initialise 0-count for part 1
count_part_2 = 0    # initialise 0-count for part 2

for row in data:    # for each instruction in the input ("R#" or "L#")
    l = list(str(list(row)).strip("[']"))    # get the instruction as a list 'R','#' or 'L','#'
    i = int(str(list(row)).strip("[']RL"))    # get the number from the instruction as an int
    if l[0] == 'R':    # if the instruction is a right turn (R)
        count_part_2 += (current+i)//100    # count number of times dial passes 0
        current = (current+i)%100    # find which value the dial now points to
    else:    # if the instruction is a left turn (L)
        count_part_2 -= (current-i)//100    # count number of times dial passes 0
        current = (current-i)%100    # find which value the dial now points to
    if current == 0:    # if the dial points at zero *after* the instruction
        count_part_1 += 1    # add one to the 0-count for part 1
    
print("Part 1 answer: " + str(count_part_1))    # print part 1 answer
print("Part 2 answer: " + str(count_part_2))    # print part 2 answer