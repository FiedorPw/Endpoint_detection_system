'''
FF.DETPY.1.2 Każda reguła ma być zdefiniowana jako oddzielna funkcja w języku Python we
wskazanym pliku w OFF.DETPY.1.1 . Format pojedynczej reguły:def nazwa_funkcji_reguly(**kwargs):
# ciało funkcji - właściwa reguła operująca na danych z args
# procesowanie pcap
# for pcap in kwargs[pcap]:
# procesowanie evtx
# for evtx in kwargs[evtx]:
# procesowanie xml
# for xml in kwargs[xml]:
# procesowanie json
# for json in kwargs[json]:
# procesowanie txt
# for txt in kwargs[txt]:
# ostateczna reguła - tj. co ma się wykonać
if condition=True:
action_alert = "..." # akcja: "local", "remote"
description = "Alert ..."
else:
action_alert = None
description = None
return action_alert, description
'''