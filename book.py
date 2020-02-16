import re
import numpy as np

CLEAN_REGEX = re.compile('[^a-zA-Z\']')


class BookLoadingException(Exception):
    def __init__(self, book_info):
        self._book_info = book_info


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


class Book:
    def __init__(self, book_id, title, src):
        self._book_id = int(book_id)
        self._title = title
        self._src = src
        self._content = ""
        self._sentences = []
        self._windows = []
        self._happinesses = []

    def __str__(self):
        return "<{}, {}, {}>".format(self._book_id, self._title, self._src)

    def windows(self):
        return self._windows

    def happinesses(self):
        return self._happinesses

    def set_happinesses(self, happinesses):
        self._happinesses = happinesses

    def book_id(self):
        return self._book_id

    def title(self):
        return self._title

    def sentences(self):
        return [word for word in self._sentences if word != '']

    def calc_happiness(self, func):
        for window in self._windows:
            self._happinesses.append(func(window))

    def load(self, _dir="data/text/", _sentence_num=15):
        with open(_dir + self._src, encoding='iso8859') as f:
            self._content = CLEAN_REGEX.sub(' ', f.read()).lower()
            words = self._content.split()
            if len(words) < 12000:
                raise BookLoadingException(self)
            self._sentences = list(chunks(words, _sentence_num))

    def windowed(self, segment_num=200, window_num=10000):
        words = self._content.split()
        indexes = np.array_split(np.array(range(len(words) - window_num)), segment_num - 1)
        tops = [t[0] for t in indexes]
        for top in tops:
            self._windows.append(' '.join(words[top: top + window_num]))
        self._windows.append(' '.join(words[-window_num:]))
