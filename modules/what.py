
from subbot import SubBot

class WhatBot(SubBot):
    
    name = "what"
    commands = {"!what"}
    description = "Get the description of some word by calling other bots and using duckduckgo"
    
    def on_command(self, command, args, chan, *_args, **_kwargs):
        self.reply(chan, "!define " + args)
        self.reply(chan, ",ud " + args)
        ddgbot = self.bot.commands["!ddg"]
        answer = ddgbot.explain(args)
        if answer:
            self.reply(chan, answer)
        self.reply(chan, "!acronym " + args)
        self.reply(chan, ",wolfram " + args)
        



BotModule = WhatBot
