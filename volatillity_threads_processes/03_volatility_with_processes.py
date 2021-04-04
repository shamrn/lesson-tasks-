# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

# TODO тут ваш код в многопроцессном стиле
# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле

import os
import zipfile
from multiprocessing import Process, Pipe, Queue


class Volatility(Process):
    def __init__(self, zip_name, file_name,ticker_name,*args,**kwargs):
        super(Volatility, self).__init__(*args, **kwargs)
        self.zip_name = zip_name
        self.data_voluation = {}
        self.data_list_ticker = []
        self.file_name = file_name
        self.ticker_name = ticker_name
        self.open_ticker()


    def unzip(self):
        with zipfile.ZipFile(self.zip_name, 'r') as zfile:
            zfile.extractall()

    def open_ticker(self):
        path_ticker = os.path.join(self.file_name, self.ticker_name)
        ticker = open(path_ticker)
        for iter_, data in enumerate(ticker):
            if iter_ == 0:
                continue
            self.recor(data)

        self.valuation()
        self.data_list_ticker.clear()
        ticker.close()

    def recor(self, data):
        self.ticker = data.split(',')[0]
        price = data.split(',')[2]
        self.data_list_ticker.append(price)
        if self.ticker not in self.data_voluation:
            self.data_voluation[self.ticker] = []

    def valuation(self):
        max_ticker = float(max(self.data_list_ticker))
        min_ticker = float(min(self.data_list_ticker))
        avg_valutation = max_ticker + min_ticker / 2
        volat_valuation = ((max_ticker - min_ticker) / avg_valutation) * 100
        self.data_voluation[self.ticker] = round(volat_valuation, 2)

    def show(self):
        sort_data = sorted(self.data_voluation.items(), key=lambda key: key[1], reverse=True)

        def _print_result(data):
            for _tiker_name, _volatilty in data:
                print(f'\t{_tiker_name} - {_volatilty}')

        print('\nМаксимальная волатильность:')
        _print_result(sort_data[:3])
        print('\nМинимальная волатильность:')
        _print_result(sort_data[len(sort_data) - 3:])

        res_nul = [res[0] for res in sort_data if res[1] == 0.00]
        print('Нулевая волатильность',*res_nul)



files_ticker = os.listdir('trades')

volat = Volatility





if __name__ == '__main__':

    sizers = [volat(zip_name='', file_name='trades', ticker_name=line) for line in files_ticker]

    for sizer in sizers:
        sizer.start()

    for sizer in sizers:
        sizer.join()

