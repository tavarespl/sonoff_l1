import esphome.codegen as cg
import esphome.config_validation as cv

from esphome.components import light
from esphome.const import CONF_ID

sonoff_l1_ns = cg.esphome_ns.namespace('sonoff_l1')
SonoffL1 = sonoff_l1_ns.class_('SonoffL1', light.LightOutput, cg.Component)

CONFIG_SCHEMA = light.RGB_LIGHT_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(SonoffL1),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield light.register_light(var, config)
