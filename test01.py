from src.system_manager import SystemManager
from src.users import Users, Mentee, Mentor
from src.group import Group
import pytest

class IdGenerator():

    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id

groupid_generator = IdGenerator()

@pytest.fixture(scope="session")
def system():
    system = SystemManager()
    return system

def test_add_mentee(system):
    mentee1 = Mentee(12345)
    mentee2 = Mentee(23456)
    
    assert(mentee1.tag == 2)
    assert(mentee2.tag == 2)
    assert(mentee1.zID == 12345)
    assert(mentee2.zID == 23456)
    assert(mentee1.groupID == 0)
    assert(mentee2.groupID == 0)

    system.add_mentee(mentee1)
    system.add_mentee(mentee2)

    assert(system.mentees[0] == mentee1)
    assert(system.mentees[1] == mentee2)

def test_add_mentor(system):

    mentor1 = Mentor(5209342)
    mentor2 = Mentor(2938492)

    assert(mentor1.tag == 1)
    assert(mentor1.zID == 5209342)
    assert(mentor1.groupID == 0)

    assert(mentor2.tag == 1)
    assert(mentor2.zID == 2938492)
    assert(mentor2.groupID == 0)

    system.add_mentor(mentor1)
    system.add_mentor(mentor2)

    assert(system.mentors[0] == mentor1)
    assert(system.mentors[1] == mentor2)

def test_get_mentor(system):
    mentor = system.get_mentor(5209342)

    assert(mentor == system.mentors[0])

def test_create_group(system):
    group1 = Group(groupid_generator.next(), system.get_mentor(5209342))
    group2 = Group(groupid_generator.next(), system.get_mentor(2938492))

    assert(group1.groupID == 1)
    assert(group1.mentor == system.mentors[0])
    assert(group1.mentee == [])
    assert(group1.picture == [])

    assert(group2.groupID == 2)
    assert(group2.mentor == system.mentors[1])
    assert(group2.mentee == [])
    assert(group2.picture == [])

def test_add_group_to_system(system):
    pass

    