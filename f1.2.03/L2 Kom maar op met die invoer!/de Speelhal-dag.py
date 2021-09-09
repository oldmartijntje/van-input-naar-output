toegangsticket = float(input("toegangsticket kosten? >>>"))
VIP_VR_GameSeat = float(input("VIP_VR_GameSeat ticket kosten per minuut? >>>"))
minuten = float(input("aantal minuten in VIP_VR_GameSeat? >>>"))
vrienden = float(input("hoeveel makkers heb je? >>>"))
loonkosten = (toegangsticket + VIP_VR_GameSeat * minuten) * vrienden/100
print("Dit geweldige dagje-uit met " + str(vrienden) + " mensen in de Speelhal met " + str(minuten) + " minuten VR kost je maar " + str(loonkosten) + " euro")