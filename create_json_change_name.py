import openpyxl
import json
from COSTANTS import CURRENT_YEAR


def create_json_change_name():
    data = dict()
    wb = openpyxl.load_workbook(f'/Users/marcomelis/Dropbox/Mia/File excel/Fantacalcio/{CURRENT_YEAR}/Associazione giocatori FantaService-PianetaFanta.xlsx')
    ws = wb['Foglio1']
    row_index = 2


    while ws.cell(row_index, 1).value is not None:
        print(f'Row: {row_index}')
        data[ws.cell(row_index, 1).value] = dict()
        data[ws.cell(row_index, 1).value]['nome_PianetaFanta'] = ws.cell(row_index, 3).value
        data[ws.cell(row_index, 1).value]['Ruolo'] = ws.cell(row_index, 5).value
        data[ws.cell(row_index, 1).value]['Squadra'] = ws.cell(row_index, 4).value
        row_index += 1

    # for i in range(2, 583):
    #     data[ws.cell(i, 1).value] = dict()
    #     data[ws.cell(i, 1).value]['nome_PianetaFanta'] = ws.cell(i, 3).value
    #     data[ws.cell(i, 1).value]['Ruolo'] = ws.cell(i, 5).value
    #     data[ws.cell(i, 1).value]['Squadra'] = ws.cell(i, 4).value

    with open(f'resource/change_name/change_name_settembre_{CURRENT_YEAR}.json', 'w') as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)


create_json_change_name()
