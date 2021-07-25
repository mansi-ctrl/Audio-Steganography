import SendMessage as sendMessage
import  ExtractMessage as extractMessage
filePath = "StarWars3.wav"
newFilePath = "250Hz_30sec_2.wav"


def main():
    key, message = sendMessage.readInput()
    if sendMessage.sendMessage(key, message, filePath, newFilePath):
        print('\n\n\tMESSAGE EMBEDDED SUCCESSFULLY...')
    else:
        print('Key ', key, ' already exists.\nPlease enter again....')
        main()

key = "121"
message = "aaaabbbccdee"
if sendMessage.sendMessage(key,message, filePath, newFilePath):
    print('\n\n\tMESSAGE EMBEDDED SUCCESSFULLY...')
    extractMessage.extractMessage(key,newFilePath)
else:
    print('Key ',key,' already exists.\nPlease enter again....')
    #main()
