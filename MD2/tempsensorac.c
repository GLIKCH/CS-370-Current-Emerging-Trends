/* Additional note - The stdio.h header defines three variable types, several macros, 
and various functions for performing input and output. 
C Library -. (n.d.). Tutorialspoint. 
https://www.tutorialspoint.com/c_standard_library/stdio_h.htm*/

#include <stdio.h>

// Define the temperature thresholds in Fahrenheit
#define UPPER_TEMP_THRESHOLD_F 86.0 // 30.0 degrees Celsius
#define LOWER_TEMP_THRESHOLD_F 68.0 // 20.0 degrees Celsius

// Define the states of the state machine
typedef enum {
    STATE_IDLE,
    STATE_COOLING
} State;

// Function prototypes for state functions
void state_idle(float currentTempF);
void state_cooling(float currentTempF);

// Function pointer to hold the current state function
void (*currentState)(float);

int main() {
    float currentTemperatureF = 77.0; // Initialize with a starting temperature in Fahrenheit

    currentState = state_idle; // Start with the idle state

    while (1) {
        // Simulate temperature reading (you would get this from a temperature sensor)
        // For the sake of this example, let's assume the temperature changes gradually
        currentTemperatureF += 0.1;

        // Call the current state function with the current temperature in Fahrenheit
        currentState(currentTemperatureF);
    }

    return 0;
}

void state_idle(float currentTempF) {
    if (currentTempF > UPPER_TEMP_THRESHOLD_F) {
        currentState = state_cooling; // Transition to the cooling state
        printf("Temperature above threshold. Cooling system activated.\n");
    }
}

void state_cooling(float currentTempF) {
    if (currentTempF < LOWER_TEMP_THRESHOLD_F) {
        currentState = state_idle; // Transition back to the idle state
        printf("Temperature below threshold. Cooling system turned off.\n");
    }
    else {
        // Perform cooling actions here
        // For the sake of this example, we'll just print a message
        printf("Cooling system is ON. Current temperature: %.2fF\n", currentTempF);
    }
}
