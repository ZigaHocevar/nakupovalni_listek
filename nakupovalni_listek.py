#uporabil bom vrsto seznama List
seznam = []

print "Pozdravljeni v nasi Smartninja trgovini!"

while True:
    odgovor = raw_input("Ali zelis dodati se kaksen izdelek v seznam? (da/ne) ")
    if odgovor == "da" or odgovor == "ja":
        izdelek = raw_input("Napisi izdelek, ki ga zelis dodati: ")
    elif odgovor == "ne":
        odgovor_ne = raw_input("Ali ste prepricani, da ste zakljucili z nakupovanjem? (da/ne) ")
        if odgovor_ne == "da" or odgovor_ne == "ja":
            print "Hvala vam za zaupanje, obiscite nas se kdaj"
            break
        else:
            continue
    else:
        break
    dod_izdelek = raw_input("Ali res zelis dodati izbran izdelek na nakupovalni listek? (da/ne) ")
    if dod_izdelek == "da" or dod_izdelek == "ja":
        seznam.append(izdelek)
    else:
        continue

print "Na vasem nakupovalnem listku so naslednji izdelki: "
for item in seznam:
    print item

print "Za vas nakup se vam zahvaljujemo :)"


