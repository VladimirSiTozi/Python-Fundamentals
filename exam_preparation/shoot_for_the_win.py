shooting_targets = [int(num) for num in input().split()]
shots_on_target = 0
shooted_targets = []

while True:
    command = input()
    if command == "End":
        shooting_targets = [str(num) for num in shooting_targets]
        score = ' '.join(shooting_targets)
        print(f"Shot targets: {shots_on_target} -> {score}")
        break
    else:
        command = int(command)

    if command < len(shooting_targets):
        shot = shooting_targets[command]
        shots_on_target += 1

        if command in shooted_targets:
            continue

        shooted_targets.append(command)

        for i, target in enumerate(shooting_targets):
            if target > shot:
                if target == -1:
                    continue
                target -= shot
                shooting_targets[i] = target
            else:
                if target == -1:
                    continue
                target += shot
                shooting_targets[i] = target
    else:
        continue

    shooting_targets[command] = -1