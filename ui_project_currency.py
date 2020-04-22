import requests
from bs4 import BeautifulSoup
import currency_ui
import sys


class Currency:
    def __init__(self, name, buy, sell, change, time):
        self.name = name
        self.buy = buy
        self.sell = sell
        self.change = change
        self.time = time

    def __str__(self):
        return """
{}
Purchasing Value: {}
Sale Value: {}
Change: {}
Update Time: {}
""".format(self.name, self.buy, self.sell, self.change, self.time)


class Index:
    def __init__(self, name, value, change, time):
        self.name = name
        self.value = value
        self.change = change
        self.time = time

    def __str__(self):
        return """
{}
Value: {}
Change: {}
Update Time: {}
""".format(self.name, self.value, self.change, self.time)


def chunks(list_to_divide, n):  # This function divides a list into lists with length of n.
    # For item i in a range that is a length of l,
    for k in range(0, len(list_to_divide), n):
        # Create an index range for l of n items:
        yield list_to_divide[k:k + n]


app = currency_ui.QtWidgets.QApplication(sys.argv)
main_window = currency_ui.QtWidgets.QMainWindow()
ui = currency_ui.Ui_main_window()
ui.setupUi(main_window)
main_window.show()
# Setting up the User Interface


# That function gets data from url and updates ui.
def update_ui():
    ui.text_currency.clear()
    ui.text_gold.clear()
    ui.text_index.clear()

    url_currency = "https://kur.currency.com/"
    response_currency = requests.get(url_currency)
    html_currency = response_currency.content
    soup_currency = BeautifulSoup(html_currency, "html.parser")
    list_currency = list()

    for i in soup_currency.find_all("td"):
        i = i.text.strip()
        if i != '' and i != ' ' and i != '\n':
            list_currency.append(i)

    list_currency = chunks(list_currency, 7)

    for i in list_currency:
        currency = Currency(i[0], i[1], i[2], i[5], i[6])

        if currency.name == "USD - Amerikan Doları":
            ui.text_currency.append(currency.__str__())
            print(currency)

        elif currency.name == "EUR - Euro":
            ui.text_currency.append(currency.__str__())
            print(currency)

    url_gold = "https://altin.currency.com/"
    response_gold = requests.get(url_gold)
    html_gold = response_gold.content
    soup_gold = BeautifulSoup(html_gold, "html.parser")
    list_gold = list()

    for i in soup_gold.find_all("td"):
        i = i.text.strip()
        if i != '' and i != ' ' and i != '\n':
            list_gold.append(i)

    list_gold = chunks(list_gold, 5)

    for i in list_gold:
        currency = Currency(i[0], i[1], i[2], i[3], i[4])

        if currency.name == "Çeyrek Altın":
            ui.text_gold.append(currency.__str__())
            print(currency)

        elif currency.name == "Yarım Altın":
            ui.text_gold.append(currency.__str__())
            print(currency)

        elif currency.name == "Tam Altın":
            ui.text_gold.append(currency.__str__())
            print(currency)

        elif currency.name == "Cumhuriyet Altını":
            ui.text_gold.append(currency.__str__())
            print(currency)

    url_index = "https://borsa.currency.com/endeksler"
    response_index = requests.get(url_index)
    html_index = response_index.content
    soup_index = BeautifulSoup(html_index, "html.parser")
    list_index = list()

    for i in soup_index.find_all("td"):
        i = i.text.strip()
        if i != '' and i != ' ' and i != '\n':
            list_index.append(i)
            print(i)

    list_index = chunks(list_index, 6)

    for i in list_index:
        index = Index(i[0], i[3], i[4], i[5])

        if index.name == "XU030 - BIST 30":
            ui.text_index.append(index.__str__())
            print(index)

        elif index.name == "XU050 - BIST 50":
            ui.text_index.append(index.__str__())
            print(index)

        elif index.name == "XU100 - BIST 100":
            ui.text_index.append(index.__str__())
            print(index)


ui.button_update.clicked.connect(update_ui)
# The function is added to ui with a click listener.
# It runs after the clicking update button.

sys.exit(app.exec_())
