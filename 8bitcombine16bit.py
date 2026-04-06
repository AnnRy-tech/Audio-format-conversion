# Aim: Convert 8 bit samples array to an array of 16 bit samples (constructing by combining to elements from 8 bit sample array)
#Created on:6-4-2026
#Author: Ann Maria Roy

input_array = [215, 255, 217, 255]
output_array = []

for i in range(0, len(input_array), 2):
    combined = (input_array[i+1] << 8) | input_array[i]
    if(combined > 32768):
      combined = combined - 65536
    output_array.append(combined)

#output_array = np.array(output_array, dtype=int)
#np.set_printoptions(threshold=np.inf)

print("Output array (16-bit values):", output_array)
