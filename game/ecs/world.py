from .entity import Entity

class World:
    """Manages all entities, components, and systems."""
    def __init__(self):
        self._entities = {}
        self._components = {}
        self._systems = []
        self._next_entity_id = 0

    def create_entity(self):
        """Creates a new entity and returns its ID."""
        entity_id = self._next_entity_id
        self._entities[entity_id] = Entity(entity_id)
        self._components[entity_id] = {}
        self._next_entity_id += 1
        return entity_id

    def add_component(self, entity_id, component):
        """Adds a component to a specific entity."""
        component_type = type(component)
        self._components[entity_id][component_type] = component

    def get_component(self, entity_id, component_type):
        """Gets a component of a specific type for an entity."""
        return self._components[entity_id].get(component_type)

    def get_entities_with_component(self, component_type):
        """Returns a list of entity IDs that have a specific component."""
        return [entity_id for entity_id, components in self._components.items()
                if component_type in components]

    def add_system(self, system):
        """Adds a system to the world."""
        self._systems.append(system)

    def update(self, dt):
        """Updates all systems."""
        for system in self._systems:
            system.update(self, dt)
