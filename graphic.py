height = int(input('Enter image height: ')) # var
width = int(input('Enter image width: ')) # var
pixels = height * width # calulate 

print('Pixels: ',pixels) # pixels

bitDepth =  int(input('Enter image depth: ')) # var
bits = pixels * bitDepth # calulate
totalbytes = bits // 8 # calulate

print('Bits: ',bits, 'Bytes: ',totalbytes, 'Bytes') # bits and bytes

if totalbytes >= 1000: # check
  totalbytes = totalbytes // 10000 # calulate
  if totalbytes < 1000: # check
    print('File size: ',totalbytes, 'kb') # total bytes
  else: 
    totalbytes = totalbytes / 1000 # calulate
    print('File size: ',totalbytes, 'kb') # total bytes
