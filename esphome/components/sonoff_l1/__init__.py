import esphome.codegen as cg
import esphome.config_validation as cv

sonoff_l1_ns = cg.esphome_ns.namespace('sonoff_l1')
SonoffL1 = sonoff_l1_ns.class_('SonoffL1', cg.Component)

CONFIG_SCHEMA = cv.Schema({}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
