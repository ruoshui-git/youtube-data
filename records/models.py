#%%
import enum
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Enum, DateTime, TypeDecorator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType


Base = declarative_base()

class IntEnum(TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """
    impl = Integer

    def __init__(self, enumtype, *args, **kwargs):
        super(IntEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):
            return value

        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    cname = Column(String(30), nullable=False)
    pinyin = Column(String(30), nullable=False)
    initials = Column(String(5), nullable=False)
    birthday = Column(Date)

    member_history = relationship('MemberHistory', back_populates='user')
    posts = relationship('Post', back_populates='author')
    bad_checkins = relationship('BadCheckin', back_populates='user')

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    member_history = relationship('MemberHistory', back_populates='group')
    posts = relationship('Post', back_populates='group')
    seminars = relationship('Seminar', back_populates='group')
    bad_checkins = relationship('BadCheckin', back_populates='group')
    tasks = relationship('Task', back_populates='parent_group')

class MemberHistory(Base):
    __tablename__ = 'member_history'

    class Type(enum.IntEnum):
        join = 1
        quit = -1
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    is_special = Column(Boolean, nullable=False, default=False)
    is_staff = Column(Boolean, nullable=False, default=False)
    type = Column(ChoiceType(Type, impl=Integer), nullable=False)

    user = relationship('User', back_populates='member_history')
    group = relationship('Group', back_populates='member_history')

class Seminar(Base):
    __tablename__ = 'seminar'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    stime = Column(DateTime)
    etime = Column(DateTime)

    group = relationship('Group', back_populates='seminars')

    tparts = relationship('Post', back_populates='seminar')
    tasks = relationship('Task', back_populates='parent_seminar')
    vparts = relationship('VerbalPart', back_populates='seminar')

class BadCheckIn(Base):
    __tablename__ = 'bad_check_in'

    class Status(enum.Enum):
        late = 0
        missing = 1

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'), primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)
    status = Column(ChoiceType(Status), nullable=False)

    user = relationship('User', back_populates='bad_checkins')
    group = relationship('Group', back_populates='bad_checkins')

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    seminar_id = Column(Integer, ForeignKey('seminar.id'))
    description = Column(String)
    timestamp = Column(DateTime)

    posts = relationship('Post', back_populates='task')

    parent_group = relationship('Group', back_populates='tasks')
    parent_seminar = relationship('Seminar', back_populates='tasks')

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    seminar_id = Column(Integer, ForeignKey('seminar.id'))
    task_id = Column(Integer, ForeignKey('task.id'))
    is_effective = Column(Boolean, default=True)


    author = relationship('User', back_populates='posts')
    group = relationship('Group', back_populates='posts')
    seminar = relationship('Seminar', back_populates='tparts')
    task = relationship('Task', back_populates='posts')

class VerbalPart(Base):
    '''
    上麦发言
    '''
    __tablename__ = 'verbal_part'

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    seminar_id = Column(Integer, ForeignKey('seminar.id'), nullable=False)
    is_effective = Column(Boolean, default=True)
    summary = Column(String)

    user = relationship('User', back_populates='vparts')
    seminar = relationship('Seminar', back_populates='vparts')



from sqlalchemy import create_engine
# engine = create_engine('sqlite+pysqlite:///data.sqlite3', future=True)
engine = create_engine('sqlite+pysqlite://', future=True)
Base.metadata.create_all(engine)


# %%
ruosh = User(cname='毛若水', pinyin='maoruoshui', initials='mrs')
rising2 = Group(name='雄起群2')
from sqlalchemy.orm import Session

with Session(engine) as session:
    session.add(ruosh)
    session.commit()
# %%
