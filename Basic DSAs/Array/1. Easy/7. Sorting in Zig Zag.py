def sortInWave(arr):
    arr.sort()
    for i in range(1, len(arr), 2):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return arr



arr = [3, 1, 4, 2, 5]
wave_form = sortInWave(arr)
print(wave_form)
