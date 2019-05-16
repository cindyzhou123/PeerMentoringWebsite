from system_manager import SystemManager
from users import Users, Mentee, Mentor
from group import Group
import pytest

@pytest.fixture
def system():
    system = SystemManager()
    return system

def test_create_mentee():
    print("Creating mentees...\n")
    mentee1 = Mentee(12345)
    print(mentee1)
    mentee2 = Mentee(23456)
    print(mentee2)
    
    assert(mentee1.tag == 2)
    assert(mentee2.tag == 2)
    assert(mentee1.zID == 12345)
    assert(mentee2.zID == 23456)

def test_add_mentor():

def test_create_group():

def test_add_group_to_system():

def test_get_mentor():
    