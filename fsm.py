from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'baby'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'kid'

    def on_enter_state1(self, update):
        update.message.reply_text("I am a baby.")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("I am a kid.")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
