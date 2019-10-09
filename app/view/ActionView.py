from PyInquirer import prompt
from ..controller.ActionController import ActionController

class ActionView:
    __QUESTIONS = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Nombre de acción',
            'validate': lambda val: 'El nombre de la tarea es obligatorio' \
                if len(val.strip()) == 0 else True
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
            'validate': lambda val: 'Debe ingresar la ruta del script' \
                if len(val.strip()) == 0 else True
        }
    ]


    @staticmethod
    def displayNew():
        answers = prompt(ActionView.__QUESTIONS)
        objActionController = ActionController()
        uid = objActionController.execAddAction(answers)
        print(f"""Se ingresó acción:
        ID   : {uid}
        Name : {answers["name"]}\
        """)


    @staticmethod
    def displayList():
        pass