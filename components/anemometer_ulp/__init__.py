import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    STATE_CLASS_MEASUREMENT,
    ICON_WEATHER_WINDY,
)

CODEOWNERS = ["@you"]
MULTI_CONF = True

anemometer_ulp_ns = cg.esphome_ns.namespace("anemometer_ulp")
AnemometerULPComponent = anemometer_ulp_ns.class_(
    "AnemometerULPComponent", cg.PollingComponent
)

CONF_SUM = "sum"
CONF_MAX_VALUE = "max_value"
CONF_SPEED_FACTOR = "speed_factor"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(AnemometerULPComponent),
    cv.Optional(CONF_SUM): sensor.sensor_schema(
        unit_of_measurement="m/s",
        icon=ICON_WEATHER_WINDY,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_MAX_VALUE): sensor.sensor_schema(
        unit_of_measurement="m/s",
        icon=ICON_WEATHER_WINDY,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_SPEED_FACTOR, default=1.0): cv.float_,
}).extend(cv.polling_component_schema("60s"))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_SUM in config:
        sens = await sensor.new_sensor(config[CONF_SUM])
        cg.add(var.set_sum_sensor(sens))

    if CONF_MAX_VALUE in config:
        sens = await sensor.new_sensor(config[CONF_MAX_VALUE])
        cg.add(var.set_max_sensor(sens))

    cg.add(var.set_speed_factor(config[CONF_SPEED_FACTOR]))
