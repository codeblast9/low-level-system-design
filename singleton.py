class Logger:
    __instance = None


    def __new__(cls, file_name: str):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            cls.__instance.file_name = file_name
            cls.__instance.log_count = 0
            return cls.__instance

        else:
            return cls.__instance


    def log(self, msg:str):
        print(f"logging {msg} in file {self.file_name}")
        self.log_count += 1

    def get_log_count(self) -> int:
        return self.log_count

log1 = Logger("app.log")
log1.log("hello")

log2 = Logger("app.log")
log2.log("world")

log3 = Logger("app.log")
log3.log("bye")


print(log1.log_count)
    


        