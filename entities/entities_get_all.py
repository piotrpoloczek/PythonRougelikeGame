from entities.entities_get import get_attribute
from entities.entities_const import SYMBOL, COORDINATES


def get_entity_by_attribute(entities, attribute, attribute_value):
    for entity in entities:
        print('entity attribute: ', get_attribute(entity, attribute))
        print('attribute value: ', attribute_value)
        if attribute_value in get_attribute(entity, attribute):
            return entity

def get_entity_by_symbol(entities, symbol):
    return get_entity_by_attribute(entities, SYMBOL, symbol)

def get_entity_by_coordinates(entities, coordinates):
    return get_entity_by_attribute(entities, COORDINATES, coordinates[0])

def get_list_attributes_from_entities(entities, attribute):
    list_attributes = []
    for entity in entities:
        list_attributes.append(get_attribute(entity, attribute))
    return list_attributes

def get_list_symbols_from_entities(entities):
    return get_list_attributes_from_entities(entities, SYMBOL)

def get_list_coordiantes_from_entities(entities):
    return get_list_attributes_from_entities(entities, COORDINATES)

