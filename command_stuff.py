__author__ = 'arthurnum'


class CommandStuff:
    def __init__(self):
        self.commands = []
        self.link_to_command_grid = None

    def delete_command(self, command, *args):
        self.link_to_command_grid.remove_widget(command.command_widget)
        self.commands.remove(command)
        i = 1
        for command in self.commands:
            command.cid = i
            command.update_widget()
            i += 1


global_command_stuff = CommandStuff()