# FKD214711 — Pemrograman Sistem Embedded
**Embedded Systems Programming** | 3 SKS (Satuan Kredit Semester)

## Overview

Embedded systems programming (pemrograman sistem embedded) provides the skills to build hardware-software systems that interface with sensors, process data in real time, and control actuators — the backbone of modern geophysical instrumentation, IoT environmental monitoring, and industrial automation. This course covers microcontroller architectures (Arduino, STM32), real-time operating systems (RTOS), sensor integration, and real-time signal processing. Students will build complete embedded projects from concept through deployment.

---

## 1. Microcontroller Architectures (Arsitektur Mikrokontroler)

### 1.1 Arduino Platform (ATmega328P)

The Arduino Uno uses an 8-bit AVR microcontroller:

|| Feature | Specification |
||---|---|
|| CPU | 8-bit AVR @ 16 MHz |
|| Flash | 32 KB (program memory) |
|| SRAM | 2 KB (runtime data) |
|| EEPROM | 1 KB (persistent storage) |
|| ADC | 10-bit, 6 channels, 15 ksps |
|| GPIO | 14 digital (6 PWM), 6 analog |
|| Interfaces | I²C, SPI, UART |

|**Arduino sketch (contoh program)**:

```cpp
// Read thermocouple and log to SD
#include <SPI.h>
#include <SD.h>

const int TC_PIN = A0;
const float V_REF = 5.0;
const float TC_SENSITIVITY = 0.041; // V/°C (Type K)

void setup() {
 Serial.begin(9600);
 SD.begin(10);
 analogReference(EXTERNAL); // Use 1.1V for precision
}

void loop() {
 int raw = analogRead(TC_PIN);
 float voltage = raw * 1.1 / 1023.0;
 float temperature = voltage / TC_SENSITIVITY;

 File f = SD.open("data.csv", FILE_WRITE);
 if (f) {
 f.print(millis());
 f.print(",");
 f.println(temperature);
 f.close();
 }
 delay(1000); // 1 Hz sampling
}
```

### 1.2 STM32 Platform (ARM Cortex-M4)

The STM32F407 (used in higher-performance instrumentation):

|| Feature | Specification |
||---|---|
|| CPU | 32-bit ARM Cortex-M4F @ 168 MHz |
|| Flash | 1 MB |
|| SRAM | 192 KB |
|| ADC | 12-bit, 16 channels, 2.4 Msps |
|| DAC | 2 × 12-bit |
|| DMA | 16 streams (zero-CPU data transfer) |
|| Interfaces | I²C, SPI, UART, CAN, USB OTG, Ethernet |

|**STM32 HAL example (DMA-based ADC)**:

```c
// HAL ADC with DMA for continuous sampling
uint16_t adc_buffer[256]; // Circular buffer
void start_adc_dma(void) {
 HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_buffer, 256);
}

// DMA complete callback (called automatically)
void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef* hadc) {
 // Process 256 samples — runs in ISR context
 for (int i = 0; i < 256; i++) {
 float voltage = adc_buffer[i] * 3.3f / 4096.0f;
 process_sample(voltage); // User-defined DSP
 }
}
```

### 1.3 Platform Comparison

|| Criterion | Arduino (AVR) | STM32 (Cortex-M4) | ESP32 |
||---|---|---|---|
|| Clock speed | 16 MHz | 168 MHz | 240 MHz |
|| Power consumption | 15 mA | 100 mA | 80 mA |
|| ADC resolution | 10-bit | 12-bit | 12-bit |
|| Cost (module) | 5 USD | 8 USD | 3 USD |
|| Best for | Prototyping | Precision control | Wireless IoT |
|| Learning curve | Low | Medium | Medium |

---

## 2. Real-Time Operating Systems (Sistem Operasi Real-Time)

### 2.1 Why RTOS?

An RTOS (sistem operasi real-time) provides deterministic task scheduling, ensuring critical tasks meet deadlines. Contrast with Arduino's bare-metal `loop()`:

|| Feature | Bare Metal | RTOS |
||---|---|---|
|| Timing guarantee | No (manual delay) | Yes (priority preemptive) |
|| Multitasking | Pseudo (cooperative) | True (preemptive) |
|| Resource management | Manual | Mutex, semaphore |
|| Code complexity | Low | Medium–High |
|| Memory overhead | Minimal | 2–10 KB RAM |

### 2.2 FreeRTOS Task Management

FreeRTOS is the dominant RTOS for microcontrollers. Core concepts:

```cpp
// FreeRTOS task creation on ESP32/STM32
void sensor_task(void* param) {
 while (1) {
 float temp = read_sensor();
 xQueueSend(data_queue, &temp, portMAX_DELAY);
 vTaskDelay(pdMS_TO_TICKS(100)); // 10 Hz
 }
}

void logging_task(void* param) {
 float temp;
 while (1) {
 if (xQueueReceive(data_queue, &temp, portMAX_DELAY)) {
 log_to_sd(temp);
 }
 }
}

void setup() {
 xTaskCreatePinnedToCore(sensor_task, "Sensor", 2048, NULL, 2, NULL, 0);
 xTaskCreatePinnedToCore(logging_task, "Logger", 4096, NULL, 1, NULL, 1);
}
```

### 2.3 Scheduling Policies

|| Policy (Kebijakan) | Description | Use Case |
||---|---|---|
|| Fixed priority preemptive | Higher priority preempts lower | Most RTOS (FreeRTOS, Zephyr) |
|| Rate monotonic (RM) | Period inversely proportional to priority | Periodic real-time tasks |
|| Earliest deadline first (EDF) | Nearest deadline gets priority | Dynamic priorities |
|| Cooperative | Tasks yield voluntarily | Simple, no preemption overhead |

---

## 3. Sensor Integration (Integrasi Sensor)

### 3.1 Communication Protocols

|| Protocol | Speed | Distance | Topology | Wires |
||---|---|---|---|---|
|| I²C | 100–400 kHz | 1 m (typical) | Bus (multi-master) | 2 (SDA, SCL) |
|| SPI | 1–50 MHz | 1–10 m | Bus (1 master, N slaves) | 4+ (MOSI, MISO, SCK, CS) |
|| UART | 300–115200 baud | 15 m | Point-to-point | 2 (TX, RX) |
|| 1-Wire | 16 kbps | 100 m | Bus | 1 + GND |
|| CAN | 1 Mbps | 1 km | Bus (multi-master) | 2 (CAN_H, CAN_L) |

### 3.2 I²C Sensor Interface Example

```cpp
// Read BME280 (temperature, humidity, pressure) over I²C
#include <Wire.h>
#define BME280_ADDR 0x76

float read_temperature() {
 Wire.beginTransmission(BME280_ADDR);
 Wire.write(0xFA); // Temperature register
 Wire.endTransmission();
 Wire.requestFrom(BME280_ADDR, 3);

 uint32_t raw = (Wire.read() << 12) | (Wire.read() << 4) | (Wire.read() >> 4);
 float temp = raw / 65536.0 * 200.0 - 50.0; // Simplified conversion
 return temp;
}
```

### 3.3 Timing Requirements

For a seismic data acquisition system sampling at $f_s = 200 $ Hz: $ T_{\text{sample}} = \frac{1}{f_s} = 5\;\text{ms} $$$

Within this 5 ms window, the MCU must:

1. Read ADC (DMA, ~0.1 ms)
2. Apply FIR filter (50 taps, ~0.05 ms on Cortex-M4)
3. Pack data for transmission (~0.1 ms)
4. Write to SD card (sector-aligned, ~2 ms worst case)

Total: ~2.25 ms < 5 ms ✓ (45% CPU utilization for data path)

---

## 4. Real-Time Processing Techniques

### 4.1 Interrupt-Driven Sampling

Using hardware timer interrupts for precise sampling:

```cpp
// Timer interrupt for precise 1 kHz sampling
void setup_timer_1kHz() {
 TIM2->PSC = 84 - 1; // 84 MHz / 84 = 1 MHz
 TIM2->ARR = 1000 - 1; // 1 MHz / 1000 = 1 kHz
 TIM2->DIER |= TIM_DIER_UIE; // Enable update interrupt
 NVIC_EnableIRQ(TIM2_IRQn);
 TIM2->CR1 |= TIM_CR1_CIE; // Start timer
}

void TIM2_IRQHandler(void) {
 if (TIM2->SR & TIM_SR_UIF) {
 TIM2->SR &= ~TIM_SR_UIF; // Clear flag
 uint16_t adc_val = ADC1->DR; // Read ADC (no blocking call)
 ring_buffer_push(&adc_ring, adc_val); // Lock-free ring buffer
 }
}
```

### 4.2 Case Study: Autonomous Ocean-Bottom Seismometer

An ocean-bottom seismometer (OBS, seismometer dasar laut) deployment off Mentawai Islands uses:

- **MCU**: STM32H7 (Cortex-M7 @ 480 MHz)
- **Sensor**: 3-component broadband geophone + hydrophone
- **Sampling**: 200 sps continuous, 24-bit ADC
- **Storage**: 2 × 256 GB microSD cards (RAID-1 redundancy)
- **Power**: 18650 Li-ion battery pack, 48 Ah total
- **Deployment duration**: 12 months
- **Data volume**: ~60 GB per station
- **Total system cost**: ~15,000 USD (vs. 100,000+ USD for commercial OBS)

The firmware implements a state machine: *SLEEP → ACQUIRE → STORE → TELEMETRY*, switching every 10 minutes. During ACQUIRE, DMA transfers sensor data to a circular buffer while the main core applies a 2-pole Butterworth anti-aliasing filter in software before SD card writes.

---

## References

1. Mazidi, M. A., Chen, S., & Ghaemi, E. (2019). *AVR Microcontroller and Embedded Systems*. Pearson.
2. Yiu, J. (2013). *The Definitive Guide to ARM Cortex-M3 and Cortex-M4 Processors*, 3rd ed. Newnes.
3. Barry, R. (2020). *Mastering the FreeRTOS Real Time Kernel*, 3rd ed. Real Time Engineers Ltd.
4. Mueller, F. (2017). *Making Embedded Systems*, 2nd ed. O'Reilly Media.
5. Massa, B. (2019). *Embedded Systems with ARM Cortex-M Microcontrollers in Assembly and C*. ERTS Press.
6. LAPAN-BRIN (2023). "Development of Ocean-Bottom Seismometer for Mentawai Subduction Zone." Technical Report, Bandung.
