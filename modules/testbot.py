
from subbot import SubBot

class TestBot(SubBot):
    
    name = "testbot"
    commands = {"!gamebottest"}
    description = "just a test if hot code loading works"
    
    def on_command(self, command, args, chan, *_args, **_kwargs):
        self.reply(chan, "TEEEEESTING")



BotModule = TestBot
