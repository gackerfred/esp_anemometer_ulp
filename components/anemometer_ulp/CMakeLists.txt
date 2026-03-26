idf_component_register(
    SRCS "anemometer_ulp.cpp"
    INCLUDE_DIRS "."
    REQUIRES ulp driver esp_driver_gpio
)

# ULP LP Core build
set(ulp_app_name ulp_${COMPONENT_NAME})
set(ulp_sources "ulp/main.c")
set(ulp_exp_dep_srcs "anemometer_ulp.cpp")

ulp_embed_binary(${ulp_app_name} "${ulp_sources}" "${ulp_exp_dep_srcs}")
