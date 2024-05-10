from PyQt5 import QtGui, QtCore
import gui.methods as methods

IMAGE_WIDTH = 661

RESTARAUNTS_ARRAY = []
RESTARAUNTS_PHOTOS_ARRAY = []

class Restaraunt:
    name = ""
    arrImagesLink = [""]
    bookingBackgroundImageLink = ""
    floorsNumber = 1
    title = ""
    description = ""

    def getImage(self, index) -> str | list[str]:
        """
        return image path if index >= 0
        return array of all images path if index == -1
        """
        if len(self.arrImagesLink) != 0:
            if index == -1: return self.arrImagesLink
            else: return self.arrImagesLink[index]


#Restaraunt 1
jungle = Restaraunt()
jungle.name = "jungle"
jungle.description = "Ресторан в джунглях"
jungle.title = "Крипер Джонс"
jungle.floorsNumber = 2
jungle.bookingBackgroundImageLink = ""
jungle.arrImagesLink = [
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/jungle_1.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/jungle_2.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/jungle_3.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/jungle_4.png", IMAGE_WIDTH)
]
RESTARAUNTS_ARRAY.append(jungle)
for photo in jungle.arrImagesLink:
    RESTARAUNTS_PHOTOS_ARRAY.append(photo)

#Restaraunt 2
mountain = Restaraunt()
mountain.name = "mountain"
mountain.description = "Ресторан в горах у реки модерн"
mountain.title = "Гига Крипер"
mountain.floorsNumber = 2
mountain.bookingBackgroundImageLink = ""
mountain.arrImagesLink = [
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/mountain_1.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/mountain_2.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/mountain_3.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/mountain_5.png", IMAGE_WIDTH)
    ]
RESTARAUNTS_ARRAY.append(mountain)
for photo in mountain.arrImagesLink:
    RESTARAUNTS_PHOTOS_ARRAY.append(photo)

#Restaraunt 3
nether = Restaraunt()
nether.name = "nether"
nether.description = "Ресторан в адской крепости"
nether.title = "Creeper Devil"
nether.floorsNumber = 2
nether.bookingBackgroundImageLink = ""
nether.arrImagesLink = [
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/nether_1.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/nether_3.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/nether_2.png", IMAGE_WIDTH),
    methods.changeImageSize("NtiWorks/Kursovaya/Application/resources/photos/nether_4.png", IMAGE_WIDTH)
]
RESTARAUNTS_ARRAY.append(nether)
for photo in nether.arrImagesLink:
    RESTARAUNTS_PHOTOS_ARRAY.append(photo)