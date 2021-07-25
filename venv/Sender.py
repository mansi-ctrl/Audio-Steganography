
# We will use wave package available in native Python installation to read and write .wav audio file
import wave

def embedded(filePath, message, newFilePath):
    # read wave audio file
    song = wave.open(filePath, mode='rb')

    # The "secret" and compressed text message
    #message ='1001011011111110000'
    #print('\n\n\n\t\tSecret compressed message = ',message)

    # Read frames and convert to byte array
    l = list(song.readframes(song.getnframes()))
    frame_bytes = bytearray(l)


    # Append dummy data to fill out rest of the bytes.
    # Receiver shall detect and remove these characters.
    x = int((len(frame_bytes)-(len(message)*8*8))/8)
    message = message + x*'#'
    #print('\n\n\tSecret message changed = ',message)

    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in message])))

    #print('length of l = ',x,' and length of bits = ',len(bits),' and length of string = ',len(string))

    #for i in range(len(l)):
    #    print('\n i = ',l[i],' and bit = ',bits[i])

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)


    # Write bytes to a new wave audio file
    with wave.open(newFilePath, 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()