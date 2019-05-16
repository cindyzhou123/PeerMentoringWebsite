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
    mentee1 = Mentee(12345, "Allen")
    mentee2 = Mentee(23456, "May")
    
    assert(mentee1.tag == 2)
    assert(mentee2.tag == 2)
    assert(mentee1.zID == 12345)
    assert(mentee2.zID == 23456)
    assert(mentee1.groupID == 0)
    assert(mentee2.groupID == 0)
    assert(mentee1.name == "Allen")
    assert(mentee2.name == "May")

    system.add_mentee(mentee1)
    system.add_mentee(mentee2)

    assert(system.mentees[0].name == "Allen")
    assert(system.mentees[1].zID == 23456)

def test_add_mentor(system):

    mentor1 = Mentor(5209342, "Cindy")
    mentor2 = Mentor(2938492, "Jason")

    assert(mentor1.tag == 1)
    assert(mentor1.zID == 5209342)
    assert(mentor1.groupID == 0)
    assert(mentor1.name == "Cindy")

    assert(mentor2.tag == 1)
    assert(mentor2.zID == 2938492)
    assert(mentor2.groupID == 0)
    assert(mentor2.name == "Jason")

    system.add_mentor(mentor1)
    system.add_mentor(mentor2)

    assert(system.mentors[0].zID == 5209342)
    assert(system.mentors[1].name == "Jason")

def test_get_user(system):
    mentor1 = system.get_mentor_by_ID(5209342)
    assert(mentor1.name == "Cindy")
    mentor2 = system.get_mentor_by_name("Jason")
    assert(mentor2.zID == 2938492)

    mentee1 = system.get_mentee_by_ID(12345)
    assert(mentee1.name == "Allen")
    mentee2 = system.get_mentee_by_name("May")
    assert(mentee2.zID == 23456)

def test_create_group(system):
    group1 = Group(groupid_generator.next(), system.get_mentor_by_name("Cindy"))
    group2 = Group(groupid_generator.next(), system.get_mentor_by_ID(2938492))

    assert(group1.groupID == 1)
    assert(group1.mentor == system.mentors[0])
    assert(group1.mentee == [])
    assert(group1.picture == [])
    assert(group1.name == "Please give me a name")

    assert(group2.groupID == 2)
    assert(group2.mentor == system.mentors[1])
    assert(group2.mentee == [])
    assert(group2.picture == [])
    assert(group2.name == "Please give me a name")

    system.add_group(group1)
    system.add_group(group2)

    group1.name = "R2D2"
    group2.name = "Woolies rules"

    assert(system.groups[0].name == "R2D2")
    assert(system.groups[1].groupID == 2)

def test_get_group(system):
    group1 = system.get_group_by_ID(1)
    assert(group1.name == "R2D2")
    group2 = system.get_group_by_name("Woolies rules")
    assert(group2.groupID == 2)

def test_mentee_to_group(system):
    group = system.get_group_by_ID(2)
    group.add_mentee(system.get_mentee_by_name("Allen"))
    group.add_mentee(system.get_mentee_by_ID(23456))

    assert(system.mentees[0].groupID == 2)
    assert(system.mentees[1].groupID == 2)
