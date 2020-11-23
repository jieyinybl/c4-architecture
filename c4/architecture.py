class Context():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.systems = []
        self.persons = []

    def add_system(self, system: 'System'):
        self.systems.append(system)

    def add_person(self, person: 'Person'):
        self.persons.append(person)


class System():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.containers = []
        self.usages = []

    def add_container(self, container: 'Container'):
        self.containers.append(container)

    def add_usage(self, target, description):
        self.usages.append(Usage(source=self, target=target, description=description))


class Person():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.usages = []

    def add_usage(self, target, description):
        self.usages.append(Usage(source=self, target=target, description=description))


class Container():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.components = []
        self.usages = []

    def add_component(self, component: 'Component'):
        self.components.append(component)

    def add_usage(self, target, description):
        self.usages.append(Usage(source=self, target=target, description=description))


class Component():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.usages = []

    def add_usage(self, target, description):
        self.usages.append(Usage(source=self, target=target, description=description))


class Usage():
    def __init__(self, source, target, description):
        self.source = source
        self.target = target
        self.description = description
