import json

log = open("visit_log.csv", "r")
purchases = open("purchase_log.txt", "r")

funnel = open("funnel.csv", "w")
funnel.write("user_id,source,category\n")

log.readline()
purchases.readline()

i = 0
while True:
    i = i + 1
    line = log.readline()
    if len(line) == 0:
        break
    line = line.strip("\n").split(",")

    purchases.seek(0)

    while True:
        p = purchases.readline()
        if len(p) == 0:
            print("break")
            break
        dict = json.loads(p)
        if dict['user_id'] == line[0]:
            funnel.write("{},{},{}\n".format(line[0], line[1], dict['category']))
            print("write")
            break

print("done")
funnel.close()
purchases.close()
log.close()
