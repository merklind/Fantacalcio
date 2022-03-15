def input_day():
    """
    Chiede in input all'utente la giornata di cui eseguire lo scraping

    Return:

    match_day (str): Numero della giromata di cui eseguire lo scraping
    
    """
    print("Inserisci la giornata: ")

    # ask user to digit the day
    match_day = input()

    # return the day digited by the user
    return match_day
