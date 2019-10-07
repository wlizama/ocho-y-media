from PyInquirer import prompt
from ..controller.ActionExecutorController import ActionExecutorController

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
            'type': 'list',
            'name': 'action_lang',
            'message': '¿Que lenguaje ejecutará la acción?',
            'choices': ActionExecutorController.getActionTypeList()
        },
        {
            'type': 'input',
            'name': 'file_src',
            'message': 'Ingresar ubicación de archivo',
        }
    ]


    @staticmethod
    def displayNew():
        answers = prompt(ActionView.__QUESTIONS)
        print(answers)