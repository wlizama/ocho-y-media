class ActionModel:

    def __init__(self, uid, name, description, action_path):
        self.__uid = uid
        self.__name = name
        self.__description = description
        self.__action_path = action_path


    @property
    def uid(self):
        return self.__uid


    @property
    def name(self):
        return self.__name


    @property
    def description(self):
        return self.__description


    @property
    def action_path(self):
        return self.__action_path


    def __str__(self):
        return f"""\
        uid={self.__uid},
        name={self.__name},
        description={self.__description},
        action_path={self.__action_path}\
        """
