def calculate_volume(w, h, l):
    try:
        w = float(w)
        h = float(h)
        l = float(l)
    except:
        raise Exception('invalid type', 'w, h, l must be numbers')
    if l <= 0 or w <= 0 or h <= 0:
        raise Exception('invalid number', 'dimension must be greater than zero')
    return w * h * l
if __name__ == '__main__':
    try:
        w = input('Width: ')
        h = input('Height: ')
        l = input('Length: ')
        vol = calculate_volume(w, h, l)
        print('Volume is ' + str(vol))
    except:
        print('Invalid input')
