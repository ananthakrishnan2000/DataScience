print("SJC23MCA-2020 - A S Ananthakrishnan")
print("batch : 2023-25")
import numpy as np
even_numbers = np.arange(2, 31, 2)
slice_result = even_numbers[2:9:2]
last_3_elements = even_numbers[-3:]
alternate_elements = even_numbers[::2]
last_3_alternate_elements = alternate_elements[-3:]
print("Original array:", even_numbers)
print("Elements from index 2 to 8:",slice_result)
print("last 3 elements of the array:",last_3_elements)
print("Alternate elements of array:",alternate_elements)
print("last 3 alternate elements:",last_3_alternate_elements)