from typing import List

class TextMomento:
    def __init__(self,text):
        self.__saved_text = text

    def get_saved_text(self):
        return self.__saved_text


class History:
    def __init__(self):
        self.__history: List[TextMomento] =[]

    def save_state(self,tm:TextMomento):
        self.__history.append(tm)

    def undo(self)-> TextMomento:
        if len(self.__history)> 0:
            self.__history.pop()
            if len(self.__history) == 0:
                return TextMomento("")
            else:
                return self.__history[-1]
        else:
            return TextMomento("")

    def get_history(self):
        for i in range(len(self.__history)):
            print(f"{i} = {self.__history[i].get_saved_text()}")

class TextEditor:
    def __init__(self):
        self.__text = ""

    def write(self,new_text):
        self.__text += new_text

    def display_text(self):
        return self.__text

    def save(self) -> TextMomento:
        return TextMomento(self.__text)

    def restore(self,tm:TextMomento):
        self.__text = tm.get_saved_text()

