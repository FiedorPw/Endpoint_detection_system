'''
REG.DET.1 W ramach środowiska stworzonej aplikacji Analizatora Cyberzagrożeń należy
zintegrować rozwiązanie do detekcji z wykorzystaniem reguł SIGMA.
REG.DET.1.1 Silnik dla reguł SIGMA w języku Python: https://github.com/wagga40/Zircolite
REG.DET.1.2 Integracja taka może opierać się na wskazaniu pojedynczej reguły lub zestawu reguł.
Poza samą detekcją należy pamiętać o integracji związanej prezentacją alertu.
REG.DET.2 Przetestować zintegrowane rozwiązanie dla reguł SIGMA.
REG.DET.2.1 Wykonać na wybranym zestawie danych EVTX/JSON względem znanej reguły SIGMA
dla tego zestawu danych (szukać w podanych źródłach i w Internecie). Można też okroić regułę
SIGMA, aby na posiadanych danych zademonstrować działanie detekcji.
'''