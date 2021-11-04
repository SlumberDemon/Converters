sampf = int(input('Enter sampling frequency: ')) # var
sampress = int(input('Enter sampling resolution: ')) # var
bitrate = sampf * sampress # calulate 

print('Bit rate: ',bitrate) # bit rate

duration =  int(input('Enter audio duration: ')) # var
bits = duration * bitrate # calulate #
totalbytes = bits // 8 # calulate

print('Bits: ',bits, 'Bytes: ',totalbytes, 'Bytes') # bits and bytes

channels = int(input('Enter channels: ')) # var
totalbytes = channels * totalbytes # calulate

if totalbytes >= 1000: # check
  totalbytes = totalbytes // 10000 # calulate
  if totalbytes < 1000: # check
    print('File size: ',totalbytes, 'kb') # total bytes
  else: 
    totalbytes = totalbytes / 1000 # calulate
    print('File size: ',totalbytes, 'kb') # total bytes
