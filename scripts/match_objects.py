class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.choices = None
        self.current_match = None
    
    def set_choices(self, choices):
        self.choices = choices
    
    def can_match_18(self):
        return self.age == "ADULT"
    
    def can_match_minor_only(self):
        return self.age == "MINOR"
    
    def set_current_match(self, work_id):
        self.current_match = work_id

    def has_match(self):
        return self.current_match is not None

    def __str__(self):
        if self.has_match():
            return f"{self.name} is matched with {self.current_match}"
        else:
            return f"{self.name} is not matched"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
    
class Work:
    def __init__(self, work_id, work_age):
        self.work_id = work_id
        self.work_age = work_age
        self.current_match = None
    
    def set_current_match(self, person_name):
        self.current_match = person_name
    
    def has_match(self):
        return self.current_match is not None
    
    def is_minor_only(self):
        return self.work_age == "MINORS ONLY"
    
    def is_adult_only(self):
        return self.work_age == "ADULTS ONLY"
    
    def __str__(self):
        if self.has_match():
            return f"Work {self.work_id} is matched with {self.current_match}"
        else:
            return f"Work {self.work_id} is not matched"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.work_id == other.work_id
    
    def __hash__(self):
        return hash(self.work_id)

class Choices:
    def __init__(self, timestamp, **kwargs):
        self.timestamp = timestamp
        self.choices = kwargs
    
    def __str__(self):
        return f"Choices made at {self.timestamp}: {self.choices}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.__str__() == other.__str__()
    
    def __hash__(self):
        return hash(self.__str__())