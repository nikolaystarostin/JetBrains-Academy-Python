from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class ToDo:
    def choose_action(self):
        action = int(input("1) Today's tasks\n"
                           "2) Week's tasks\n"
                           "3) All tasks\n"
                           "4) Missed tasks\n"
                           "5) Add task\n"
                           "6) Delete task\n"
                           "0) Exit\n"))
        if action == 1:
            self.today()
        elif action == 2:
            self.week()
        elif action == 3:
            self.all()
        elif action == 4:
            self.missed()
        elif action == 5:
            self.add()
        elif action == 6:
            self.delete()
        elif action == 0:
            exit()
        else:
            self.choose_action()

    def print_on_day(self, rows, include_day=False):
        if len(rows) == 0:
            print('Nothing to do!\n')
        else:
            for row in rows:
                if include_day:
                    date = row[2].strftime('%d %b').lstrip('0')
                    print(f'{row[0]}) {row[1]}. {date}')
                else:
                    print(f'{row[0]}) {row[1]}')
            print()

    def all(self):
        rows = session.query(Table.id, Table.task, Table.deadline).all()
        print('\nAll tasks')
        self.print_on_day(rows, include_day=True)
        self.choose_action()

    def today(self):
        rows = session.query(Table.id, Table.task).filter(Table.deadline == datetime.today().date()).all()
        print(f"Today {datetime.today().strftime('%d %b')}:")
        self.print_on_day(rows)
        self.choose_action()

    def week(self):
        for i in range(0, 7):
            day = datetime.today().date() + timedelta(days=i)
            rows = session.query(Table.id, Table.task).filter(Table.deadline == day).all()
            print(f"{day.strftime('%A %d %b')}:")
            self.print_on_day(rows)
        self.choose_action()

    def missed(self):
        rows = session.query(Table.id, Table.task, Table.deadline).filter(Table.deadline < datetime.today().date()).all()
        print('Missed tasks:')
        self.print_on_day(rows, include_day=True)
        self.choose_action()

    def add(self):
        new_row = Table(task=input('Enter task\n'),
                        deadline=datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d'))
        session.add(new_row)
        session.commit()
        print('The task has been added!\n')
        self.choose_action()

    def delete(self):
        rows = session.query(Table.id, Table.task, Table.deadline).all()
        print('Choose the number of the task you want to delete:')
        self.print_on_day(rows, include_day=True)
        rows = session.query(Table).all()
        row_to_delete = rows[int(input()) - 1]
        session.delete(row_to_delete)
        session.commit()
        print('The task has been deleted\n')
        self.choose_action()


todo_list = ToDo()
todo_list.choose_action()
