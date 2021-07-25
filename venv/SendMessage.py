import Frequency as f
import Encoding as code
import  Sender as send
import AddKey as add

def readInput():
    message = input('\n\n\t\t\tEnter your message: ')
    key = input('\n\n\t\t\tEnter associated key: ')

    return key, message


def sendMessage(key, message, filePath, newFilePath):

    #print('Message = ',message)

    #Compress the message first into binary
    compressedMessage, codes, freq, cntr = code.encode(message)
    print('Compressed message = ',compressedMessage)

    if add.addKey(key, codes, freq, cntr):
        #Then embed the message
        send.embedded(filePath, compressedMessage, newFilePath)
        return True
    else:
        return False

"""
key = "01"
message = "Hello!ThisIsAMessageToBeEmbeddedInAnAudioFile"
if sendMessage(key,message, "60Hz.wav","60HzNew.wav"):
    print('\n\n\tMESSAGE EMBEDDED SUCCESSFULLY...')
else:
    print('Key ',key,' already exists.\nPlease enter again....')
    
    """

"""
key = "02"
message = "AAAAABBBBCCCDDEFFGGGGHHHHIIIII"
if sendMessage(key,message, "50Hz.wav","50HzNew.wav"):
    print('\n\n\tMESSAGE EMBEDDED SUCCESSFULLY...')
else:
    print('Key ',key,' already exists.\nPlease enter again....')

    """

"""
key = "03"
message = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
if sendMessage(key,message, "40Hz.wav","40HzNew.wav"):
    print('\n\n\tMESSAGE EMBEDDED SUCCESSFULLY...')
else:
    print('Key ',key,' already exists.\nPlease enter again....')

    """
key = "04"
message = "In_This_AudioFile_The_Speaker_Is_Speaking_Preamble._This_audio_has_a_brilliant_sound_quality.The_sampling_frequency_is_around_44kHz"
if sendMessage(key,message, "preamble.wav","preambleNew.wav"):
    print('\n\n\tMESSAGE EMBEDDED SUCCESSFULLY...')
else:
    print('Key ',key,' already exists.\nPlease enter again....')