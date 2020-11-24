import enum


class Type(enum.EnumMeta):
    CONTEXT = 'Context'
    SYSTEM = 'Software System'
    PERSON = 'Person'
    CONTAINER = 'Container'
    COMPONENT = 'Component'


class Context():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.systems = []
        self.persons = []
        self.type = Type.CONTEXT

    def add_system(self, system: 'System'):
        self.systems.append(system)

    def add_person(self, person: 'Person'):
        self.persons.append(person)


class System():
    def __init__(self, name, description, internal=True):
        self.name = name
        self.description = description
        self.containers = []
        self.relationships = []
        self.type = Type.SYSTEM
        self.internal = internal

    def add_container(self, container: 'Container'):
        self.containers.append(container)

    def add_relationship(self, target, description, method=None):
        self.relationships.append(Relationship(source=self, target=target, description=description, method=method))


class Person():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.relationships = []
        self.type = Type.PERSON

    def add_relationship(self, target, description, method=None):
        self.relationships.append(Relationship(source=self, target=target, description=description, method=method))


class Container():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.components = []
        self.relationships = []
        self.type = Type.CONTAINER

    def add_component(self, component: 'Component'):
        self.components.append(component)

    def add_relationship(self, target, description, method=None):
        self.relationships.append(Relationship(source=self, target=target, description=description, method=method))


class Component():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.relationships = []
        self.type = Type.COMPONENT

    def add_relationship(self, target, description, method=None):
        self.relationships.append(Relationship(source=self, target=target, description=description, method=method))


class Relationship():
    def __init__(self, source, target, description, method=None):
        self.source = source
        self.target = target
        self.description = description
        self.method = method
