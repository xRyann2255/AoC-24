with open("5.txt", "r") as file:
    f = file.read()

rules = [rule.split("|") for rule in f.split("\n\n")[0].split("\n")]
rules_left, rules_right = [rule[0] for rule in rules], [rule[1] for rule in rules]
updates = [update.split(",") for update in f.split("\n\n")[1].split("\n")]

answer = 0

def valid_update(update):
    for i, page in enumerate(update):
        if page in rules_left:
            checks = [after for j, after in enumerate(rules_right) if page == rules_left[j]]
            for check in checks:
                if check in update and update.index(check) < i:
                    return False
    return True

for update in updates:
    if valid_update(update):
        answer += int(update[len(update) // 2])

print(answer)

# Part 2

answer = 0

for update in updates:
    if not valid_update(update):
        while not valid_update(update):
            for i, page in enumerate(update):
                if page in rules_left:
                    checks = [after for j, after in enumerate(rules_right) if page == rules_left[j]]
                    for check in checks:
                        if check in update and update.index(check) < i:
                            update.remove(page)
                            update.insert(update.index(check), page)
        answer += int(update[len(update) // 2])

print(answer)