def dating(boys: [str], girls: [str]):
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары.")
        return
    boys.sort()
    girls.sort()

    print("Идеальные пары:")
    for idx in range(len(boys)):
        print(boys[idx], "и", girls[idx])


boys = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

boys2 = ["Peter", "Alex", "John", "Arthur", "Richard", "Michael"]
girls2 = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

print("--- Первый набор пар:")
dating(boys, girls)

print("\n--- Второй набор пар:")
dating(boys2, girls2)