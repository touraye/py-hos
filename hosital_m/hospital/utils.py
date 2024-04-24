from enum import IntEnum

class SpecialtyTypes(IntEnum):
    DENTIST = 1
    CARDIOLOGY = 2
    PSYCHIATRY = 3
    
    
    @classmethod
    def specialties(cls):
        return [(key.value, key.name) for key in cls]
    