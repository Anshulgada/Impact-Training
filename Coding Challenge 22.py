def simulate_training(Xena_strength, Ragnar_strength, Galahad_strength, Xena_intensity, Ragnar_intensity, Galahad_intensity):
    sessions = 0
    while Xena_strength != Ragnar_strength or Ragnar_strength != Galahad_strength:
        Xena_strength += Xena_intensity
        Ragnar_strength += Ragnar_intensity
        Galahad_strength += Galahad_intensity
        sessions += 1

        # Check if strengths diverge infinitely
        if sessions > 1000:
            return -1

    return sessions


# Read input values
Xena_strength = int(input())
Ragnar_strength = int(input())
Galahad_strength = int(input())
Xena_intensity = int(input())
Ragnar_intensity = int(input())
Galahad_intensity = int(input())

# Call the function and print the result
sessions_needed = simulate_training(Xena_strength, Ragnar_strength, Galahad_strength, Xena_intensity, Ragnar_intensity, Galahad_intensity)
print(sessions_needed)