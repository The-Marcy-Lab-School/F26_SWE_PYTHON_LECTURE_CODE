# Predict, then run: What does this program print? Is it "right"?

is_on = "Yes"
has_power = "No"
generator_is_running = "Yes"

there_is_light = is_on and (has_power or generator_is_running)

print(f"The lights are on: {there_is_light}")
