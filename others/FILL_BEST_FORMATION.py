def find_team(ws, team_name):

    for row in range(2, 83, 20):
        for column in range(1, 9, 7):
            rif_cell = ws.cell(row, column)
            rif_cell_value = rif_cell.value[1:]
            team_name_cell = ws[rif_cell_value].value
            if team_name == team_name_cell:
                return (rif_cell.row + 2, rif_cell.column)








def fill_best_formation(ws, best_formation, team_name):

    row_team, column_team = find_team(ws, team_name)

    for role in best_formation:
        for player in role:
            ws.cell(row_team, column_team).value = player
            row_team += 1

