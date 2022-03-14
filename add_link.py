def add_link(ws, json_file):

    range_cell = ("O25", "O26", "O27", "O28", "O29", "O30", "O31", "O32", "O33", "O34")
    k = 0
    match_day = list(json_file.keys())
    members = list(json_file[match_day[0]].keys())

    for i in range(0, 10, 2):
        current = range_cell[i]
        next_cell = range_cell[i + 1]
        ws[current].hyperlink = json_file[match_day[0]][members[k]]['link']
        ws[next_cell].hyperlink = json_file[match_day[0]][members[k + 1]]['link']
        k += 2