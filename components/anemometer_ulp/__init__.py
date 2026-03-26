import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

anemometer_ulp_ns = cg.esphome_ns.namespace("anemometer_ulp")
AnemometerULPComponent = anemometer_ulp_ns.class_(
    "AnemometerULPComponent", cg.PollingComponent
)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(AnemometerULPComponent),
}).extend(cv.polling_component_schema("60s"))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
