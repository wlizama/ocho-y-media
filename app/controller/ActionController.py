from ..dao.SQLServerConnection import SQLServerConnection

class ActionController:

    def execAddAction(self, action_vals):
        """
        Agregar nueva acción
        :return:
        """
        print("Ejecutar Agregar acción")
        sqc = SQLServerConnection()
        sqc.connect()
        return 1

    def execListAction():
        print("Ejecutar accion Listar")
