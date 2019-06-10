"""
Class that loads a list of proxy servers
"""
import random

class ProxieList():

    def __init__(self):

        self.proxie_list = []
        with open('myproxies', 'r') as fp:
            for line in fp:
                text = str(line).rstrip()
                self.proxie_list.append(text)

    def get_proxy(self):
        return(random.choice(self.proxie_list))
