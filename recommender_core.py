import math

class CannabisRecommender:
    def __init__(self):
        # A sample of our "University Grade" database
        self.strain_database = [
            {
                "name": "Granddaddy Purple",
                "type": "Indica Dominant",
                "chemoprofile": {"thc": 23, "cbd": 0.1, "myrcene": 0.8, "caryophyllene": 0.5, "limonene": 0.1},
                "effects": ["sleep", "pain_relief", "relaxation"]
            },
            {
                "name": "Jack Herer",
                "type": "Sativa Dominant",
                "chemoprofile": {"thc": 19, "cbd": 0.2, "terpinolene": 0.9, "caryophyllene": 0.3, "pinene": 0.4},
                "effects": ["creativity", "focus", "energy"]
            },
            {
                "name": "ACDC",
                "type": "High CBD",
                "chemoprofile": {"thc": 1, "cbd": 20, "myrcene": 0.5, "pinene": 0.2, "caryophyllene": 0.2},
                "effects": ["anxiety_relief", "inflammation", "clear_headed"]
            }
        ]

    def calculate_similarity(self, user_prefs, strain_profile):
        """
        Calculates a 'Match Score' (0-100) based on chemical synergy.
        """
        score = 0
        total_weight = 0

        # Weighted matching for Cannabinoids (THC/CBD)
        for compound, target_value in user_prefs.get('cannabinoids', {}).items():
            strain_value = strain_profile.get(compound, 0)
            diff = abs(target_value - strain_value)
            # The closer the match, the higher the score (simple linear decay)
            score += max(0, 10 - diff) * 2  
            total_weight += 20

        # Weighted matching for Terpenes (The "Entourage Effect" Logic)
        for terpene, weight in user_prefs.get('terpenes', {}).items():
            strain_val = strain_profile.get(terpene, 0)
            if strain_val > 0.3: # Threshold for "significant presence"
                score += 15
            total_weight += 15

        return (score / total_weight) * 100 if total_weight > 0 else 0

    def recommend(self, user_request):
        results = []
        for strain in self.strain_database:
            match_score = self.calculate_similarity(user_request, strain['chemoprofile'])
            if match_score > 50: # Only return good matches
                results.append({
                    "strain": strain['name'],
                    "match_score": round(match_score, 1),
                    "reason": f"High chemical alignment with your request for {user_request.get('goal')}"
                })
        
        # Sort by best match
        return sorted(results, key=lambda x: x['match_score'], reverse=True)

# --- Example Usage for Testing ---
if __name__ == "__main__":
    engine = CannabisRecommender()
    
    # User wants to sleep (needs Myrcene + THC)
    user_night_profile = {
        "goal": "Sleep",
        "cannabinoids": {"thc": 20, "cbd": 0},
        "terpenes": {"myrcene": "high"}
    }
    
    print("Top Recommendations:", engine.recommend(user_night_profile))
