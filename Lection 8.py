def cats_with_hats(num_cats):
    hats = set()
    for round_number in range(1,num_cats + 1):
        for cat_number in range(1,num_cats + 1):
            if cat_number % round_number == 0:
                if cat_number not in hats:
                    hats.add(cat_number)
                else:
                    hats.remove(cat_number)

    return sorted(list(hats))
    
num_cats = 33
cats_with_hats_at_end = cats_with_hats(num_cats)

print("Cats with hats at the end:", cats_with_hats_at_end)