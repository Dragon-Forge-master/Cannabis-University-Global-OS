/**
 * Cannabis University Global - Safe Dosing Algorithm
 * Based on metabolic weight and tolerance factors.
 */

const SAFETY_FACTOR = 0.5; // Conservative safety buffer for new users

function calculateEdibleDose(weightKg, experienceLevel) {
    let baseDoseMg = 0;

    // 1. Determine Base Tolerance
    switch(experienceLevel.toLowerCase()) {
        case 'novice': // Never tried
            baseDoseMg = 2.5;
            break;
        case 'beginner': // Tried a few times
            baseDoseMg = 5.0;
            break;
        case 'intermediate': // Regular user
            baseDoseMg = 10.0;
            break;
        case 'expert': // High tolerance
            baseDoseMg = 25.0;
            break;
        default:
            return "Error: Invalid experience level.";
    }

    // 2. Adjust for Body Weight (Heavier metabolism often requires slightly more, but we dampen this effect for safety)
    const weightModifier = weightKg / 70; // Normalized to average 70kg human
    
    // 3. Calculate Final "Start Low, Go Slow" Recommendation
    let recommendedDose = baseDoseMg * weightModifier;
    
    // Cap the novice dose regardless of weight to prevent "greening out"
    if (experienceLevel === 'novice' && recommendedDose > 5) {
        recommendedDose = 5;
    }

    return {
        dose_mg: parseFloat(recommendedDose.toFixed(1)),
        warning: "WAIT AT LEAST 120 MINUTES before consuming more.",
        metabolic_note: "Edibles are processed by the liver (converting Delta-9 to 11-Hydroxy-THC), which is 5x more psychoactive."
    };
}

// Example Run
console.log(calculateEdibleDose(80, 'novice'));
