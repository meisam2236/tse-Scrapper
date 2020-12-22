from selenium  import webdriver
import json
import time

class StockGetter:
    def __init__(self, url):
        self.driver = webdriver.Chrome('C:/chromedriver.exe')
        self.driver.get(url)
        self.getter()

    def getter(self):
        i = 0
        while i<20:
            try:
                self.title = self.driver.find_element_by_css_selector('div.bigheader').text.split('-')[0]
                closePriceSection = self.driver.find_element_by_id('d03').text.split(' ')
                self.closePrice = closePriceSection[0]
                closePriceColor = self.driver.find_elements_by_css_selector('span')[7].get_attribute('style').split(';')[-2].split(':')[-1].strip()
                closePricePercentage = closePriceSection[-1].replace('[', '').replace(']', '')
                self.closePricePercentageWithSign = f'+{closePricePercentage}' if closePriceColor == 'green' else f'-{closePricePercentage}'
                self.openPrice = self.driver.find_element_by_id('d05').text
                tradePriceSection = self.driver.find_element_by_id('d02').text.split(' ')
                self.tradePrice = tradePriceSection[0]
                tradePriceColor = self.driver.find_elements_by_css_selector('span')[9].get_attribute('style').split(';')[-2].split(':')[-1].strip()
                tradePricePercentage = tradePriceSection[-1].replace('[', '').replace(']', '')
                self.tradePricePercentageWithSign = f'+{tradePricePercentage}' if tradePriceColor == 'green' else f'-{tradePricePercentage}'
                self.driver.quit()
            except:
                time.sleep(1)
                i += 1
                print('Trying...')
                continue
            break
        
    def print(self):
        print(f'Title-> \t\t\t{self.title}')
        print(f'Close Price-> \t\t\t{self.closePrice}')
        print(f'Close Price Percentage-> \t{self.closePricePercentageWithSign}')
        print(f'Open Price-> \t\t\t{self.openPrice}')
        print(f'Trade Price-> \t\t\t{self.tradePrice}')
        print(f'Trade Price Percentage-> \t{self.tradePricePercentageWithSign}')

    def json_dump(self):
        jsonFile = {'title': self.title, 'close price': self.closePrice, 'close price percentage': self.closePricePercentageWithSign, 'open price': self.openPrice, 'trade price': self.tradePrice, 'trade price percentage': self.tradePricePercentageWithSign}
        with open('data.json', 'w') as f:
            json.dump(jsonFile, f)


if __name__=='__main__':
    url = 'http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=65883838195688438'
    stockGetter = StockGetter(url)
    stockGetter.print()
    # stockGetter.json_dump()
