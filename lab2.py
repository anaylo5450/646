#this will be the code fo the 900 dice rolls and the bar graph for it
import random
import matplotlib.pyplot as plt
def roll_dice(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def getBarPlot(results):
    counts = [0] * 6
    for result in results:
        counts[result - 1] += 1

    plt.bar(range(1, 7), counts)
    plt.xlabel('Dice Face')
    plt.ylabel('Frequency')
    plt.title('Dice Roll Frequencies')
    plt.xticks(range(1, 7))
    plt.show()

results = roll_dice(900)
getBarPlot(results)