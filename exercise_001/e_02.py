for item in list(range(0, 10, 2)):
    print(f" ---- {item} -----")

list_ran = list(range(0, 100, 5))
print(f"--- {list_ran} min = {min(list_ran)}  max = {max(list_ran)}  sum = {sum(list_ran)}")

list_2 = [item2/5.6 for item2 in range(0, 124, 6)]
print(f" --- {list_2}")

list_mil = list(range(0, 1_000_001))
print(f"--- {list_mil} min = {min(list_mil)}  max = {max(list_mil)}  sum = {sum(list_mil)}")

