#pragma once
#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esp_sleep.h"
#include "ulp_lp_core.h"
#include "ulp_anemometer_bin.h"

// Embedded by board_build.embed_files — symbol derived from filename only
extern const uint8_t _binary_ulp_anemometer_bin_start[];
extern const uint8_t _binary_ulp_anemometer_bin_end[];

// RTC memory variables from ULP program (ulp_ prefix auto-added by IDF)
extern uint32_t ulp_sum;
extern uint32_t ulp_max_value;

namespace esphome {
namespace anemometer_ulp {

class AnemometerULPComponent : public PollingComponent {
 public:
  void set_sum_sensor(sensor::Sensor *s)  { sum_sensor_ = s; }
  void set_max_sensor(sensor::Sensor *s)  { max_sensor_ = s; }
  void set_speed_factor(float f)          { speed_factor_ = f; }

  void setup() override {
    if (esp_sleep_get_wakeup_cause() != ESP_SLEEP_WAKEUP_TIMER) {
      ESP_LOGI("anemometer_ulp", "First boot, loading ULP");
      load_ulp_();
    } else {
      ESP_LOGI("anemometer_ulp", "Timer wakeup, reading counters");
    }
  }

  void update() override {
    if (sum_sensor_)  sum_sensor_->publish_state(ulp_sum / 120.0f * speed_factor_);
    if (max_sensor_)  max_sensor_->publish_state(ulp_max_value * speed_factor_);
  }

 private:
  sensor::Sensor *sum_sensor_{nullptr};
  sensor::Sensor *max_sensor_{nullptr};
  float speed_factor_{1.0f};

  void load_ulp_() {
    ESP_ERROR_CHECK(ulp_lp_core_load_binary(ulp_anemometer_bin, ulp_anemometer_bin_len));
  }
};

}  // namespace anemometer_ulp
}  // namespace esphome
