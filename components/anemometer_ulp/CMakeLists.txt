idf_component_register(
    SRCS "ulp_binary.S"
    INCLUDE_DIRS "."
    REQUIRES ulp driver esp_driver_gpio
)
