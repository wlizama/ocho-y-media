from PyInquirer import prompt
from ..controller.OchoYMediaController import OchoYMediaController
from ..view.ActionView import ActionView

class MainMenuView:
    __QUESTIONS = [
        {
            'type': 'list',
            'name': 'opciones',
            'message': '¿Que tarea realizarás?',
            'choices': [
                {
                    'value': 'exc',
                    'name': 'Ejecutar 08:30',
                    'action': OchoYMediaController.fnTest
                },
                {
                    'value': 'add',
                    'name': 'Agregar nueva accion',
                    'action': ActionView.displayNew
                },
                {
                    'value': 'lst',
                    'name': 'Mostar lista de acciones',
                    # 'action': ActionController.execListAction
                }
            ]
        }
    ]


    def __getAnswer(self):
        return prompt(self.__QUESTIONS)
    

    def __executeAction(self, action_val):
        choices = self.__QUESTIONS[0]["choices"]
        choice_val = action_val["opciones"]
        selected_choice = None
        for choice in choices:
            if choice["value"] == choice_val:
                selected_choice = choice
        
        if selected_choice:
            selected_choice["action"]()


    def display(self):
        answer = self.__getAnswer()
        self.__executeAction(answer)