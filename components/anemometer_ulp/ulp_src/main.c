#include <stdint.h>
#include <stdbool.h>
#include "ulp_lp_core.h"
#include "ulp_lp_core_gpio.h"

#define ANEMOMETER_PIN LP_IO_NUM_2

#define DEBOUNCE_TICKS 1        // ~10ms (same as poll rate)
#define SAMPLE_TICKS   500      // 5 seconds (500 * 10ms)
#define WINDOW_SIZE    120

uint32_t pulse_count = 0;
bool previous = false;

// sampling
uint32_t samples[WINDOW_SIZE] = {0};
uint32_t sample_index = 0;
uint32_t sum = 0;
uint32_t max_value = 0;

uint32_t tick_count = 0;
uint32_t debounce_counter = 0;

int main(void)
{
    // -------- Pulse counting --------
    bool current = (bool)ulp_lp_core_gpio_get_level(ANEMOMETER_PIN);

    if (debounce_counter > 0) {
        debounce_counter--;
    }

    if (current && !previous && debounce_counter == 0) {
        pulse_count++;
        debounce_counter = DEBOUNCE_TICKS;
    }

    previous = current;

    // -------- 5-second sampling --------
    tick_count++;

    if (tick_count >= SAMPLE_TICKS) {
        tick_count = 0;

        uint32_t old = samples[sample_index];

        sum -= old;

        samples[sample_index] = pulse_count;
        sum += pulse_count;

        pulse_count = 0;

        sample_index = (sample_index + 1) % WINDOW_SIZE;

        // recompute max
        max_value = 0;
        for (int i = 0; i < WINDOW_SIZE; i++) {
            if (samples[i] > max_value) {
                max_value = samples[i];
            }
        }
    }

    return 0;
}
