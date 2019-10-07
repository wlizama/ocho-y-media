from PyInquirer import prompt
from ..controller.ActionController import ActionController

class ActionView:
    __QUESTIONS = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Nombre de acción',
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Ingrese descripción',
        },
        {
            'type': 'input',
            'name': 'action_path',
            'message': 'Ubicación de script a ejecutar',
        }
    ]


    @staticmethod
    def displayNew():
        answers = prompt(ActionView.__QUESTIONS)
        objActionController = ActionController()
        uid = objActionController.execAddAction(answers)
        # ActionController.execAddAction(answers)


    @staticmethod
    def displayList():
        pass