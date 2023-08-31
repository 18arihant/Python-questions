# 1299. Replace Elements with Greatest Element on Right Side

class solution():
    def replaceElements(self, arr):
        temp = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > temp:
                arr[i], temp = temp, arr[i]
            else:
                arr[i] = temp    
        return arr

a=solution()
print(a.replaceElements([17,18,5,4,6,1]))