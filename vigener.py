class VigenerCryptographer:
    def __init__(self, key, alphabet):
        self.key = key
        self.key_len = len(key)
        self.key_index = 0
        self.alphabet = alphabet
        self.alphabet_len = len(alphabet)

    def get_char_serial_number(self, char):
        return self.alphabet.find(char)

    def is_in_alphabet(self, char):
        return self.get_char_serial_number(char) != -1

    def get_UTF_from_char_serial_number(self, serial_num):
        return self.alphabet[serial_num]

    def get_new_char(self, char, delta):
        return self.alphabet[
            (self.get_char_serial_number(char) + delta) % self.alphabet_len
        ]

    @property
    def next_key_index(self):
        self.key_index += 1
        self.key_index %= self.key_len
        return self.key_index

    ENCODE = 1
    DECODE = -1

    def step(self, string, direction=1):
        res = []
        self.key_index = -1
        for char in string:
            if self.is_in_alphabet(char):
                delta = self.get_char_serial_number(self.key[self.next_key_index])
                if direction == self.DECODE:
                    delta = -delta
                char = self.get_new_char(char, delta)
            res.append(char)
        return ''.join(res)


def main():
    string = "зск гддъ щляяды? стояъдян, ры жпат унтлшо юошмс ьэбцт асеаьёдь, црод щнаваглнё ксд гяпдц оабаи рыкипдцмлъ, щлоталц м ывфохмвучвфо хмв (02.05.2018) ъ крху бпсдсяадъся гймъсъ н фяоисняъш ийб готнм ийюэюхдрдит."
    key = "оиаипсне"
    times = 2
    vigener_processor = VigenerCryptographer(key, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    for _ in range(times):
        string = vigener_processor.step(string, -1)
    print(string)


if __name__ == '__main__':
    main()
