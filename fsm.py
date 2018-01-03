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

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'teenager'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'adult'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'elderly'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'dead'

    def on_enter_state1(self, update):
        update.message.reply_text("I am a baby.")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving baby')

    def on_enter_state2(self, update):
        update.message.reply_text("I am a kid.")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving kid')

    def on_enter_state3(self, update):
        update.message.reply_text("I am a teenager.")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving teenager')

    def on_enter_state4(self, update):
        update.message.reply_text("I am an adult.")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving adult')

    def on_enter_state5(self, update):
        update.message.reply_text("I am an elderly.")
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving elderly')

    def on_enter_state6(self, update):
        update.message.reply_text("I am dead.")
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving dead')

