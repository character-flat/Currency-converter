import json
import requests


class Change:

    def __init__(self):
        self.money_user = None
        self.money_change = None
        self.have_money = None
        self.write_file = {}


    def money_currency(self):
        self.money_user = input().lower()
        self.money_change = input().lower()
        self.have_money = float(input())
        if self.money_user == 'usd' or self.money_change == 'usd':
                    print("Checking the cache...")
                    self.euro = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new_euro = self.euro.text
                    self.new_euro = json.loads(self.new_euro)
                    self.changed_euro = self.new_euro['eur']['rate']
                    self.write_file['eur'] = self.changed_euro

                    self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new = self.r.text
                    self.new = json.loads(self.new)
                    self.changed = self.new[self.money_change]['rate']
                    self.changed_money = self.have_money * self.changed
                    self.write_file[self.money_change] = self.changed
                    print(f"Oh! It is in the cache!\nYou received {round(self.changed_money, 2)} {self.money_change.upper()}.")

        elif self.money_user != 'usd' and self.money_user != 'eur':
                        print("Checking the cache...")
                        self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                        self.new = self.r.text
                        self.new = json.loads(self.new)
                        self.changed = self.new[self.money_change]['rate']
                        self.changed_money = (self.have_money * self.changed)
                        self.write_file[self.money_change] = self.changed
                        print(f"Sorry, but it is not in the cache!\nYou received {round(self.changed_money, 2)} {self.money_change.upper()}.")


        elif self.money_user == 'eur' or self.money_change == 'eur':
                    print("Checking the cache...")
                    self.usd = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new_usd = self.usd.text
                    self.new_usd = json.loads(self.new_usd)
                    self.changed_usd = self.new_usd['usd']['rate']
                    self.write_file['usd'] = self.changed_usd

                    self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                    self.new = self.r.text
                    self.new = json.loads(self.new)
                    self.changed = self.new[self.money_change]['rate']
                    self.changed_money = self.have_money * self.changed
                    self.write_file[self.money_change] = self.changed
                    print(f"Oh! It is in the cache!\nYou received {round(self.changed_money, 2)} {self.money_change.upper()}.")

        self.next_currency()

    def next_currency(self):
        self.money_usered = input().lower()
        while True:
            if len(self.money_usered) == 0:
                exit()
            if self.money_usered not in self.write_file.keys():
                        self.have_money = float(input())
                        print("Checking the cache...")
                        self.r = requests.get(f'http://www.floatrates.com/daily/{self.money_user}.json')
                        self.new = self.r.text
                        self.new = json.loads(self.new)
                        self.changed = self.new[self.money_usered]['rate']
                        self.changed_money = (self.have_money * self.changed)
                        self.write_file[self.money_usered] = self.changed
                        print(f"Sorry, but it is not in the cache!\nYou received {round(self.changed_money, 2)} {self.money_usered.upper()}.")
                        self.next_currency()
            elif self.money_usered in self.write_file.keys():
                        self.have_money = float(input())
                        print("Checking the cache...")
                        self.money_dict = self.write_file.get(self.money_usered)
                        self.changed_money = self.have_money * self.money_dict
                        print(f"Oh! It is in the cache!\nYou received {round(self.changed_money, 2)} {self.money_usered.upper()}.")
                        self.next_currency()






p = Change()
p.money_currency()