#dit berekent de prijs per pizza
def calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna):
    price = 0
    #grootte van pizza
    if dough == "small":
        price += 1
    if dough == "medium":
        price += 1.5
    if dough == "large":
        price += 2
    #als humongous gekozen is, kies large
    if dough == "humongous":
        price += 2
    #aantal pepperoni
    if pepperoni == "small":
        price += 0.4
    if pepperoni == "medium":
        price += 0.6
    if pepperoni == "large":
        price += 0.9
    if pepperoni == "humongous":
        price += 9
    #aantal kaas
    if cheese == "small":
        price += 0.2
    if cheese == "medium":
        price += 0.3
    if cheese == "large":
        price += 0.45
    if cheese == "humongous":
        price += 4.5
        #aantal pineapple
    if pineapple == "small":
        price += 0.2
    if pineapple == "medium":
        price += 4
    if pineapple == "large":
        price += 16
    if pineapple == "humongous":
        price += 256
        #aantal ham
    if ham == "small":
        price += 0.2
    if ham == "medium":
        price += 4
    if ham == "large":
        price += 16
    if ham == "humongous":
        price += 256
        #aantal tomaten saus
    if tomatosauce == "small":
        price += 0.1
    if tomatosauce == "medium":
        price += 0.2
    if tomatosauce == "large":
        price += 0.3
    if tomatosauce == "humongous":
        price += 0.5
        #aantal tonijn
    if tuna == "small":
        price += 1.2
    if tuna == "medium":
        price += 1.5
    if tuna == "large":
        price += 1.9
    if tuna == "humongous":
        price += 19
    return price
#dit is de setup zodat de rest werkt
import os.path
loop = True
round = 1
round2 = 1
totalcosts = 0
import os
#dit is een loop die je blijft vragen of je meer wilt bestellen en of je de menu kaart wilt zien
while loop == True:
    menukaart = input("wilt u het menu zien? >>>")
    if menukaart == "ja" or menukaart == "Ja":
        print("----------------------------------------------------------")   
        print("|             |  small  |  medium  |  large  | humongous | humangous==10*large") 
        print("|    Dough    |   €1    |   €1.5   |    €2   |           |") 
        print("|  Pepperoni  |  €0.4   |   €0.6   |   €0.9  |     €9    |")
        print("|   Cheese    |  €0.2   |   €0.3   |  €0.45  |    €4.5   |")
        print("|  pinapple   |  €0.2   |    €4    |   €16   |    €256   |")
        print("|    ham      |  €0.2   |    €4    |   €16   |    €256   |")
        print("| tomatosauce |  €0.1   |   €0.2   |  €0.3   |    €0.5   |")
        print("|    tuna     |  €1.2   |   €1.5   |  €1.9   |    €19    |")
        print("----------------------------------------------------------")   
    pizzaAmount = int(input("hoeveel pizza's wilt u? >>>"))
    if pizzaAmount >= 0:
        #dit blijft herhalen tot het zoveel keer heeft herhaald als het aantal pizza's
        while round <= pizzaAmount:
            round += 1
            #dit bekijkt of het al de 2e ronde is, want als je al een ronde bent geweest kan je de input skippen om de zelfde configuratie als de vorige pizza te nemen
            if round > 2:
                again = input("wilt u dezelfe pizza als de vorige bestelling? >>>")
                if again == "ja" or again == "Ja":
                    print("okay")
                #hier vul je in welke topping je wilt als je een andere pizza wilt
                else:
                    print("zeg niks als u het pebaalde ding niet wilt")
                    print("Voor pizza nummero " + str(round -1) + ", welke size wilt u van:")
                    dough = input("Dough >>>")
                    pepperoni = input("Pepperoni >>>")
                    cheese = input("Cheese >>>")
                    pineapple = input("Pineapple >>>")
                    ham = input("Ham >>>")
                    tomatosauce = input("tomatocause >>>")
                    tuna = input("Tuna >>>")
            #dit is voor de 1e pizza, waarbij je invult wat je wilt
            else:
                print("zeg niks als u het pebaalde ding niet wilt")
                print("Voor pizza nummero " + str(round -1) + ", welke size wilt u van:")
                dough = input("Dough >>>")
                pepperoni = input("Pepperoni >>>")
                cheese = input("Cheese >>>")
                pineapple = input("Pineapple >>>")
                ham = input("Ham >>>")
                tomatosauce = input("tomatocause >>>")
                tuna = input("Tuna >>>")
            #hier kijk je of de order.txt bestaat, en zo niet, dan maakt het een nieuwe order.txt
            if os.path.isfile("order.txt"):
                print("yes")
                f = open("order.txt", "a")
            else:
                print("no")
                f = open("order.txt", "x")
            #hier kijk je of de individualpizzacosts.txt bestaat, en zo niet, dan maakt het een nieuwe individualpizzacosts.txt
            if os.path.isfile("individualpizzacosts.txt"):
                print("yes")
                file2 = open("individualpizzacosts.txt", "a")
            else:
                print("no")
                file2 = open("individualpizzacosts.txt", "x")
            #het aanroepen van de functie om de prijs van de pizza te berekenen
            costPerPizza = calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna)
            #het uploaden naar een file
            file2.write(str(costPerPizza));
            #kijken of er dingen niet zijn gekozen
            if dough != "small" or dough != "medium" or dough != "large" or dough != "humongous":
                dough = "NONE"
            if dough == "humongous":
                dough = "large"
            if pepperoni != "small" or pepperoni != "medium" or pepperoni != "large" or pepperoni != "humongous":
                pepperoni = "NONE"
            if cheese != "small" or cheese != "medium" or cheese != "large" or cheese != "humongous":
                cheese  = "NONE"
            if pineapple != "small" or pineapple != "medium" or pineapple != "large" or pineapple != "humongous":
                pineapple = "NONE"
            if ham != "small" or ham != "medium" or ham != "large" or ham != "humongous":
                ham = "NONE"
            if tomatosauce != "small" or tomatosauce != "medium" or tomatosauce != "large" or tomatosauce != "humongous":
                tomatosauce = "NONE"
            if tuna != "small" or tuna != "medium" or tuna != "large" or tuna != "humongous":
                tuna = "NONE"
            f.write(dough + "\n" + pepperoni + "\n" + cheese + "\n" + pineapple + "\n" + ham + "\n" + tomatosauce + "\n" + tuna)
            totalcosts += costPerPizza
            #sluiten van de files
            f.close()
            file2.close()
        #het afrekenen
        print("bij elkaar word dit een bedrag van: €" + str(totalcosts))
        receipt = input("wilt u het bonnetje? >>>")
        if receipt == "ja" or receipt == "Ja":
            print("okay")
            while round2 <= pizzaAmount:
                round2 += 1
                #hier kijk je of de receipt.txt bestaat, en zo niet, dan maakt het een nieuwe receipt.txt
                if os.path.isfile("receipt.txt"):
                    print("yes")
                    receipt = open("receipt.txt", "a")
                else:
                    print("no")
                    receipt = open("receipt.txt", "x")
                #openen van andere files
                file1 = open("order.txt", "r")
                file2 = open("individualpizzacosts.txt", "r")
                #data opslaan
                lines1 = file1.readlines()
                lines2 = file2.readlines()
                file1.close()
                file2.close()
                #bonnetje schrijven naar file
                receipt.write("-------------------------------------\n")
                receipt.write("|Pizza  size|"+lines1[0]+ "|\n")
                receipt.write("| Pepperoni |"+lines1[1]+ "|\n")
                receipt.write("|  Cheese   |"+lines1[2]+ "|\n")
                receipt.write("| Pineapple |"+lines1[3]+ "|\n")
                receipt.write("|    Ham    |"+lines1[4]+ "|\n")
                receipt.write("|Tomatosauce|"+lines1[5]+ "|\n")
                receipt.write("|   Tuna    |"+lines1[6]+ "|\n")
                receipt.write("-------------------------------------\n")
                receipt.write("|   Price   |"+lines2[0]+ "|\n")
                receipt.write("\n")
                #files verwijderen
                del lines1[0]
                del lines1[1]
                del lines1[2]
                del lines1[3]
                del lines1[4]
                del lines1[5]
                del lines1[6]
                del lines2[0]
                #heropenen en herschrijven van files
                file1 = open("order.txt", "w+")
                file2 = open("individualpizzacosts.txt", "w+")
                for line in lines1:
                    file1.write(line)
                for line in lines2:
                    file2.write(line)
                receipt.close()
            if os.path.isfile("receipt.txt"):
                print("yes")
                receipt = open("receipt.txt", "a")
            else:
                print("no")
                receipt = open("receipt.txt", "x")
            print(receipt.readlines())
            receipt.close()
        else:
            print("okay")
        #zet de loop uit
        loop = False
        #os.remove("order.txt")
        #os.remove("individualpizzacosts.txt")
    else:
        print("je moet er sowieso 1 kopen")

pizzaType = input("what pizza would you like?")