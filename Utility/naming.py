from random import randint, choices

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
              'ch', 'gh', 'ph', 'rh', 'sh', 'th', 'yh',
              'bl', 'cl', 'fl', 'gl', 'pl', 'sl', 'yl']
vowels = ['a', 'e', 'i', 'o', 'u', 'y',
          'aa', 'ae', 'ai', 'ao', 'au', 'ay',
          'ea', 'ee', 'ei', 'eo', 'eu', 'ey',
          'ia', 'ie', 'ii', 'io', 'iu', 'iy',
          'oa', 'oe', 'oi', 'oo', 'ou', 'oy',
          'ua', 'ue', 'ui', 'uo', 'uu', 'uy']


def produceName():
    size = randint(1, 5)
    name = ""
    for i in range(size):
        consonant = choices(consonants, weights=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 1, 1, 1, 1, 1,
                                                 5, 1, 1, 1, 5, 5, 1,
                                                 1, 1, 1, 1, 1, 1, 1])
        name += consonant[0]

        vowel = choices(vowels, weights=[10, 10, 10, 10, 10, 3,
                                         2, 3, 3, 3, 3, 1,
                                         3, 2, 3, 3, 3, 1,
                                         3, 3, 2, 3, 3, 1,
                                         3, 3, 3, 2, 3, 1,
                                         3, 3, 3, 3, 2, 1])
        name += vowel[0]

    return name.capitalize()

