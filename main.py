# /Evaluation-Engines/main.py
from engines.judgement import ComparisonEngine
from engines.reputation import ReputationTracker

class EvaluationSystem:
    def __init__(self):
        self.judgement = ComparisonEngine()
        self.reputation = ReputationTracker()

    def process_incoming_data(self, data):
        # 1. Judgement Phase
        variance = self.judgement.run_parity_check(data)
        
        # 2. Reputation Phase
        if variance.is_critical:
            self.reputation.penalize_node(data.entity_uid, variance.delta)
        else:
            self.reputation.update_score(data.entity_uid, success=True)

# Instantiate the system
eval_core = EvaluationSystem()
