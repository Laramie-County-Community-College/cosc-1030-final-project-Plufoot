import random

sim_count = int(input("How many times do you want to run the simulation? "))

three_stats = {
    "3PT attempts": 0,
    "3PT made": 0,
    "3PT missed": 0,
    "Won in OT": 0,
    "Lost in OT": 0
}

foul_stats = {
    "2PT attempts": 0,
    "2PT made": 0,
    "2PT miss": 0,
    "Rebound": 0,
    "Won": 0,
    "Lost": 0,
    "Won in OT": 0,
    "Lost in OT": 0
}

def bucket(percent):
    if random.random() < percent:
        return True
    else:
        return False
    
def ot(stats):
    result = random.randint(0, 1)
    if result == 1:
        stats["Won in OT"] += 1
    else:
        stats["Lost in OT"] += 1

def reb(rebound):
    if time_remaining >= 15 and bucket(rebound) == True:
        return True
    else:
        return False


for three in range(sim_count):
    three_point = random.uniform(0.2, 0.45)
    three_stats["3PT attempts"] += 1
    
    if bucket(three_point) == True:
        three_stats["3PT made"] += 1
        ot(three_stats)
    else:
        three_stats["3PT missed"] += 1


for foul in range(sim_count):
    opfree_throw = random.uniform(0.55, 0.8)
    time_remaining = random.randint(5, 30)
    two_point = random.uniform(0.5, 0.7)
    rebound = random.uniform(0.25, 0.3)

    ft1 = bucket(opfree_throw)
    ft2 = bucket(opfree_throw)

    if ft1 and ft2 == True:
        foul_stats["Lost"] += 1

    elif ft1 and ft2 == False:
        foul_stats["2PT attempts"] += 1
        if bucket(two_point) == True:
            foul_stats["Won"] += 1

        elif reb(rebound) == True:
            foul_stats["Won"] += 1

        else:
            foul_stats["Lost"] += 1

    else:
        foul_stats["2PT attempts"] += 1
        if bucket(two_point) == True:
            foul_stats["2PT made"] += 1
            ot(foul_stats)

        else:
            if reb(rebound) == True:
                foul_stats["2PT miss"] += 1
                foul_stats["Rebound"] += 1
                ot(foul_stats)

            else:
                foul_stats["Lost"] += 1    


foul_wins = foul_stats["Won in OT"] + foul_stats["Won"]
foul_losses = foul_stats["Lost in OT"] + foul_stats["Lost"]

three_wins = three_stats["Won in OT"]
three_losses = three_stats["Lost in OT"]

def win_rate(wins, losses):
    total = wins + losses
    return round(wins / total * 100, 2)


print(f"3 Point Stats: {three_stats}")
print(f"Foul Stats: {foul_stats}")
print("")
print(f"3 Point Win Rate: {win_rate(three_wins, three_losses)}")
print(f"Fouling Win Rate: {win_rate(foul_wins, foul_losses)}")




