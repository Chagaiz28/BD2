from teacher_crud import TeacherCRUD
from database import Database

class TeacherCLI:
    def __init__(self, teacher_model):
        self.teacher_model = teacher_model
        self.commands = {
            "create": self.create_teacher,
            "read": self.read_teacher,
            "update": self.update_teacher,
            "delete": self.delete_teacher,
        }

    def create_teacher(self):
        name = input("Enter the name: ")
        ano_nasc = int(input("Enter the birth year: "))
        cpf = input("Enter the CPF: ")
        self.teacher_model.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Enter the name: ")
        teacher = self.teacher_model.read(name)
        if teacher:
            print(f"Name: {teacher['name']}")
            print(f"Birth Year: {teacher['ano_nasc']}")
            print(f"CPF: {teacher['cpf']}")

    def update_teacher(self):
        name = input("Enter the name: ")
        newCpf = input("Enter the new CPF: ")
        self.teacher_model.update(name, newCpf)

    def delete_teacher(self):
        name = input("Enter the name: ")
        self.teacher_model.delete(name)

    def run(self):
        print("Welcome to the Teacher CLI!")
        print("Available commands: create, read, update, delete, quit")
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

if __name__ == "__main__":
    db = Database("bolt://18.234.76.182:7687", "neo4j", "weed-parties-battleship")
    teacher_crud = TeacherCRUD(db)
    cli = TeacherCLI(teacher_crud)
    cli.run()