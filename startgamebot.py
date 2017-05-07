#!/usr/bin/python3 -u

from gamebot import GameBot
import irc.client
from loaderbot import LoaderBot


if __name__ == '__main__':
    channels = [
        #'#tildetown',
        '#bots_test',
        '#grunk',
        '#lostpig',
        '#bots',
        '#games',
        '#gamebot'
    ]
    bots = [
        'loaderbot',
        'adminbot',
        'helpbot',
        'grunkbot'
    ]
    
    reactor = irc.client.Reactor()
    client = reactor.server().connect("localhost", 6667, "gamebot")
    
    bot = GameBot(reactor, channels)
    loader = LoaderBot()
    bot.add_subbot(loader, 'loaderbot')
    for bot in bots:
        loader.load(bot)
    
    reactor.process_forever()
    
    
    
    #client = IRCClient("gamebot", "localhost")
    #bot = GameBot(client, channels)
    #loader = LoaderBot()
    #bot.add_subbot(loader, 'loaderbot')
    #for bot in bots:
        #loader.load(bot)
    #client.start()
