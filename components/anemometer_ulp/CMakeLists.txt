idf_component_register(
    SRCS "anemometer_ulp.cpp"
    INCLUDE_DIRS "."
    REQUIRES ulp esp_driver_gpio freertos esp_hw_support
)
