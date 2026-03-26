idf_component_register(
    SRCS "ulp_binary.S" "anemometer_ulp.cpp"
    INCLUDE_DIRS "."
    REQUIRES ulp esp_driver_gpio freertos esp_hw_support
)

target_include_directories(${COMPONENT_LIB} PUBLIC
    $ENV{IDF_PATH}/components/ulp/lp_core/lp_core/include
    $ENV{IDF_PATH}/components/ulp/lp_core/shared/include
)
