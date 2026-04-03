class Threat:
    def __init__(self, threat_id, name, threat_type, probability, impact):
        self.threat_id = threat_id
        self.name = name
        self.threat_type = threat_type
        self.probability = probability  # Should be a value between 0 and 1
        self.impact = impact  # Typically a numerical value representing the impact level

    def calculate_severity(self):
        # Severity can be determined by some calculation involving probability and impact
        return self.probability * self.impact

    def calculate_risk_level(self):
        severity = self.calculate_severity()
        if severity < 1:
            return 'Low'
        elif severity < 3:
            return 'Medium'
        else:
            return 'High'