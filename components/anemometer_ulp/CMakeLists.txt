idf_component_register(
    SRCS "anemometer_ulp.cpp"
    INCLUDE_DIRS "."
    REQUIRES ulp esp_driver_gpio freertos esp_hw_support
)

target_include_directories(${COMPONENT_LIB} PUBLIC
    /data/cache/platformio/packages/framework-espidf/components/ulp/lp_core/lp_core/include
    /data/cache/platformio/packages/framework-espidf/components/ulp/lp_core/shared/include
)
