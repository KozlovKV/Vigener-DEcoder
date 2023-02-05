def isRusChr(char):
    return ord('а') <= ord(char) <= ord('ё')


def getRusCharRealSN(char):
    if ord(char) <= ord('е'):
        return ord(char) - ord('а')
    if ord(char) <= ord('я'):
        return ord(char) + 1 - ord('а')
    return ord('е') + 1 - ord('а')


def getRusCharUTFBySN(serial_num):
    if serial_num <= 5:
        return chr(ord('а') + serial_num)
    if serial_num == 6:
        return 'ё'
    return chr(ord('а') + serial_num - 1)


def cycleMove(serial_num, delta):
    return (serial_num + delta) % 33


def viziner_step(string, key, encode=True):
    res = []
    key_len = len(key)
    key_index = 0
    for i in range(len(string)):
        char = string[i]
        if isRusChr(string[i]):
            delta = getRusCharRealSN(key[key_index])
            if not encode:
                delta = -delta
            new_sn = cycleMove(getRusCharRealSN(string[i]), delta)
            char = getRusCharUTFBySN(new_sn)
            key_index = (key_index + 1) % key_len
        res.append(char)
    return ''.join(res)


def main():
    string = "зск гддъ щляяды? стояъдян, ры жпат унтлшо юошмс ьэбцт асеаьёдь, црод щнаваглнё ксд гяпдц оабаи рыкипдцмлъ, щлоталц м ывфохмвучвфо хмв (02.05.2018) ъ крху бпсдсяадъся гймъсъ н фяоисняъш ийб готнм ийюэюхдрдит."
    key = "оиаипсне"
    times = 2
    for _ in range(times):
        string = viziner_step(string, key, encode=False)
    print(string)


if __name__ == '__main__':
    main()
