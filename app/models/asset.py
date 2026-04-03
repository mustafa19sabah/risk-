class Asset:
    def __init__(self, asset_id, name, asset_type, criticality, owner):
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.criticality = criticality
        self.owner = owner
        self.vulnerabilities = []
        self.threats = []

    def add_vulnerability(self, vulnerability):
        """Adds a vulnerability to the asset's list of vulnerabilities."""
        self.vulnerabilities.append(vulnerability)

    def add_threat(self, threat):
        """Adds a threat to the asset's list of threats."""
        self.threats.append(threat)