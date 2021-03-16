w1, w2, w3 = 0.3, 0.2, 0.5
kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]
weights = [w1, w2, w3]
def crop_yield(region, weights):
    result = 0
    for x, w in zip(region, weights):
        result += x * w
    return result
print(crop_yield(kanto, weights))


for x, w in zip(kanto, weights):
    print(x*w," x :",x," w :",w)
import urllib.request

urllib.request.urlretrieve(
    'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv',
    'climate.txt')
import numpy as np
arr2 = np.array([[1, 2, 3, 4],

                 [5, 6, 7, 8],
                 [9, 1, 2, 3]])
arr3 = np.array([[11, 12, 13, 14],
                 [15, 16, 17, 18],
                 [19, 11, 12, 13]])
arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 1, 2, 3]])
arr4 = np.array([4, 5, 6, 7]) # it will replicate it self if ypu add arr 1 and arr4
print(arr1+arr4)
