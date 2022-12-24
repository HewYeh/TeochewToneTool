# Teochew Tone Tool V1

def main():
    ToneCategoryDict =  {"1":"陰", "2":"陰", "3":"陰", "4":"陰", "5":"陽", "6":"陽", "7":"陽", "8":"陽"}
    ToneContourDict =   {"1":"平", "2":"上", "3":"去", "4":"入", "5":"平", "6":"上", "7":"去", "8":"入"}
    ToneNameToNumberDict = {"陰平":"1", "陰上":"2", "陰去":"3", "陰入":"4", "陽平":"5", "陽上":"6", "陽去":"7", "陽入":"8"}

    while True:
        expectedToneName = ""
        firstCharacterTone = input("Input the tone of the first character (1-8): ")
        if firstCharacterTone == "0":
            break
        secondCharacterTone = input("Input the tone of the second character (1-8): ")
        expectedToneName += ToneCategoryDict[firstCharacterTone]
        expectedToneName += ToneContourDict[secondCharacterTone]
        expectedToneNumber = ToneNameToNumberDict[expectedToneName]

        print("\n〈The expected tone is tone", expectedToneNumber +".〉\n")
        print("The first character is tone", firstCharacterTone, "which contributes the",ToneCategoryDict[firstCharacterTone],"tone category")
        print("The second character is tone", secondCharacterTone, "which contributes the", ToneContourDict[secondCharacterTone],"tone contour")
        print("The expected tone is then", expectedToneName, "i.e., tone", expectedToneNumber+"\n\n")

    print("End of Program\n")
if __name__ == "__main__":
    main()