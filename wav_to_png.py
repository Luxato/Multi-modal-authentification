#https://stackoverflow.com/questions/50281187/convert-png-back-to-wav


from PIL import Image
import wave, struct, sys, math

##
# Collect input
##
if sys.argv[1][-4:] != '.wav':
    sys.exit("First argument should be a .wav file")

if sys.argv[2][-4:] != '.png':
    sys.exit("Second argument should be a .png file")

##
# Conversion:
##

# Wave file needs to be 16 bit mono
waveFile = wave.open(sys.argv[1], 'r')

if waveFile.getnchannels() != 1:
    sys.exit("ERROR: The wave file should be single channel (mono)")


imageRgbArray = list()

waveLength = waveFile.getnframes()

# Create the image size (based on the length)
imageSize = math.ceil(math.sqrt(waveLength))

# Loop through the wave file
for i in range(waveLength):

    # Try to read frame, if not possible fill with 0x0
    try:
        waveData = waveFile.readframes(1)
        data = struct.unpack("<h", waveData) # This loads the wave bit
        convertedData = int(data[0]) + 32768
    except:
        convertedData = 0
        pass

    bits = 5
    rgbData = tuple([(convertedData>>bits*i)&(2**bits-1) for i in range(3)])
    rgbData = tuple(map(lambda x: x<<3, rgbData))

    # Add the RGB value to the image array
    imageRgbArray.append(rgbData)

# Create new image
im = Image.new('RGB', (int(imageSize), int(imageSize)))

# Add image data
im.putdata(list(sorted(imageRgbArray)))

# Save image
im.save(sys.argv[2])