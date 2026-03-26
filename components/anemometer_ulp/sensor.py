import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    STATE_CLASS_MEASUREMENT,
    UNIT_METER_PER_SECOND,
    ICON_WEATHER_WINDY,
)
from . import AnemometerULPComponent, anemometer_ulp_ns

CONF_SUM = "sum"
CONF_MAX_VALUE = "max_value"
CONF_SPEED_FACTOR = "speed_factor"
CONF_ANEMOMETER_ID = "anemometer_id"

DEPENDENCIES = ["anemometer_ulp"]

CONFIG_SCHEMA = cv.Schema({
    cv.Required(CONF_ANEMOMETER_ID): cv.use_id(AnemometerULPComponent),
    cv.Optional(CONF_SUM): sensor.sensor_schema(
        unit_of_measurement=UNIT_METER_PER_SECOND,
        icon=ICON_WEATHER_WINDY,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_MAX_VALUE): sensor.sensor_schema(
        unit_of_measurement=UNIT_METER_PER_SECOND,
        icon=ICON_WEATHER_WINDY,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_SPEED_FACTOR, default=1.0): cv.float_,
})

async def to_code(config):
    hub = await cg.get_variable(config[CONF_ANEMOMETER_ID])

    if CONF_SUM in config:
        sens = await sensor.new_sensor(config[CONF_SUM])
        cg.add(hub.set_sum_sensor(sens))

    if CONF_MAX_VALUE in config:
        sens = await sensor.new_sensor(config[CONF_MAX_VALUE])
        cg.add(hub.set_max_sensor(sens))

    cg.add(hub.set_speed_factor(config[CONF_SPEED_FACTOR]))
