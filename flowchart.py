class Box():
    def __init__(self, text, choices = {}):
        """text should be a string which is the text inside the box
        choices is a dictionary where each key is a string describing the choice
        and the value is the associated Box.
        """
        self.text = text
        self.choices = choices
    
    def run(self):
        print(self.text)
        if len(self.choices) == 0:
            return
        elif "" in self.choices:
            self.choices[""].run()
        else:
            for choice in self.choices.keys():
                print(choice)
            user_input = input("> ")
            self.choices[user_input].run()


end = Box(text="Buy a new pen")
sure = Box(text="Are you sure?", choices={"": end})
start = Box("Do you need another pen?", choices={"yes": end, "no": sure})

start.run()
