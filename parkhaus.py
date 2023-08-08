def status_anzeigen (anzahl_parkplaetze_belegt, eingang_frei, ausgang_frei, vermietet):

    parkplaetze_gesamt = 500
    parkplaetze_belegt_maximum = parkplaetze_gesamt // 100 * 95
                                        # 330               >   475      -> False
                                        # 488               >   475      -> True
    auslastung_ueber_95_prozent = anzahl_parkplaetze_belegt > parkplaetze_belegt_maximum

                                #   True    and      True     : True
                                #   True    and      False     : False
                                #   False    and      True     : False
                                #   False    and      False     : False

                                #   True    or      True     : True
                                #   True    or      False     : True
                                #   False    or      True     : True
                                #   False    or      False     : False
    ein_oder_ausfahrt_blockiert = not (eingang_frei and ausgang_frei)

    if auslastung_ueber_95_prozent and not ein_oder_ausfahrt_blockiert and not vermietet:
        print("Parkhaus belegt")
    elif not auslastung_ueber_95_prozent and not ein_oder_ausfahrt_blockiert and not vermietet:
        print("Parkhaus frei")
    else:
        print("Parkhaus gesperrt")



# Funktionsaufrufe (zum Testen)
status_anzeigen(330, True, True, False)    # Parkhaus frei
status_anzeigen(330, True, False, False)    # Parkhaus gesperrt
status_anzeigen(330, False, True, False)    # Parkhaus gesperrt
status_anzeigen(488, True, True, False)    # Parkhaus belegt 