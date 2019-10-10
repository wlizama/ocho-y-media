from PyInquirer import prompt, Validator, ValidationError
from terminaltables import SingleTable
import os
from ..controller.ActionController import ActionController


class ActionPathValidator(Validator):
    def validate(self, document):
        # validar ruta vacia
        is_empty = True if len(document.text.strip()) == 0 else False
        if is_empty:
            raise ValidationError(
                message='Debe ingresar la ruta del script.',
                cursor_position=len(document.text))  # Move cursor to end

        if not os.path.isfile(document.text):
            raise ValidationError(
                message=f'El archivo "{document.text}" no existe.',
                cursor_position=len(document.text))  # Move cursor to end


class ActionView:
    __QUESTIONS = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Nombre de acción',
            'validate': lambda val: 'El nombre de la tarea es obligatorio.' \
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
            'validate': ActionPathValidator
        }
    ]


    @staticmethod
    def display_new():
        answers = prompt(ActionView.__QUESTIONS)
        objActionController = ActionController()
        uid = objActionController.add_action(answers)
        print(f"""Se ingresó acción:
        ID   : {uid}
        Name : {answers["name"]}\
        """)


    @staticmethod
    def display_list():
        objActionController = ActionController()
        data = []
        data.append(("ID", "Name", "Description", "Script Source"))
        list = objActionController.get_actions_list()
        data.extend(list)
        table = SingleTable(data)
        print(table.table)

        if len(list) == 0:
            print(" No hay datos para mostrar")


