def change_team_name(data: dict, match_day):
    new_dict = {f'Giornata{match_day}': {}}
    # list with default change from fantacalcio names to our surname
    default_change = (("Fc Nando Kill-bisk", "Bisca"), ("SSC Otto", "Pietro"), ("ZEON CAVALLO", "Zone"), ("G.S. Ambrosiana", "Zino"),
        ("Mastini napoleta...", "Milo"), ("AZTECHI MILANO", "Michelone"), ("Patchester United", "Sangio"), ("Maori's club", "Melis"),
        ("Gramentela", "Gracis"), ("f.c. panda", "Carlo"))

    # loop through fake name and our surname to perform the change
    for fake_name in data['Giornata' + match_day].keys():
        for true_name in default_change:
            if fake_name == true_name[0]:
                new_dict['Giornata'+ match_day][true_name[1]] = data['Giornata' + match_day][fake_name]

    return new_dict
