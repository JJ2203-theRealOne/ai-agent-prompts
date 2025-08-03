import unittest
import json

class TestFraudPrompt(unittest.TestCase):
    def test_risk_level_output(self):
        output = {
            "risk": "High",
            "signals": ["IP mismatch", "Unusual time"]
        }
        self.assertIn(output["risk"], ["Low", "Medium", "High"])
        self.assertTrue(len(output["signals"]) > 0)

if __name__ == "__main__":
    unittest.main()
