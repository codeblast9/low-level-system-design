from abc import ABC, abstractmethod

class DataParsor(ABC):
    def _parser(self):
        self._open()
        self._dataparsor()
        self._close()

    def _open(self):
        print("Opening the file")

    def _close(self):
        print("closing the file")

    @abstractmethod
    def _dataparsor(self):
        pass

class CSVParse(DataParsor):
    def _dataparsor(self):
        print("parsing the csv file.....")


csv=CSVParse()
csv._parser()