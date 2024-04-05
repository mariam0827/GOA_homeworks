#1
day = True
lights_on = False
LightInTheRoom = day or lights_on
print("Is there any light in the room?" + str(LightInTheRoom))

#2
PhoneCharged = False
ChargerWorking = False
ChargePhone = PhoneCharged and ChargerWorking
print("can you charge your phone?" + str(ChargePhone))

#3
age = 15
RequieredAge = 18
EnterTheClub = 15 > 18
print("is he allowed to go into the club?" + str(EnterTheClub))

#4
ticketCoast = 10
money = 18.4
buyTheTicket = int(money) > ticketCoast
print("did she buy the ticket?" + str(buyTheTicket))

#5
locationEntered = True
locationFound = True
pathShown = locationEntered and locationFound
print("can she go to to the location?" + str(pathShown))

#6
paint = True
brushes = False
canvas = True
painting = paint and brushes and canvas
print("can she paint right now?" + str(painting))

#7
enoughStrage = True
downloadedSongs = True
newPlaylist = False
downloadNewPL = enoughStrage and downloadedSongs and newPlaylist
print("can he download a new playlist?" + str(downloadNewPL))

#8
present_student1 = False
present_student2 = True
presentation = present_student1 or present_student2
print("is presentation today?" + str(presentation))

#9
pen = True
pencil = False
sketch = pen or pencil
print("can he sketch right now?" + str(sketch))

#10
shoes_ready = True
pants_ready = False
shirt_ready = False
outfit_ready = shoes_ready and pants_ready and shirt_ready
print("is his outfit ready?" + str(outfit_ready))