gender = input("Sukupuolesi (nainen/mies)?")
hg_value = int(input("Hemoglobiinsi (g/l)?"))

if gender == "nainen":
    #testataan naisen ohjearvot
    if hg_value < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hg_value <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif gender == "mies":
    #tee sama miehen arvoilla
    if hg_value < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hg_value <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    pass
    #TODO: tulosta virheilmoitus(?)