class RegressionTester:

    def __init__(self):

        self.results = []

    def run_test(
        self,
        question,
        expected,
        actual
    ):

        passed = (
            expected.lower().strip()
            ==
            actual.lower().strip()
        )

        result = {
            "question": question,
            "passed": passed
        }

        self.results.append(
            result
        )

        return result

    def summary(
        self
    ):

        total = len(
            self.results
        )

        passed = sum(
            1
            for item in self.results
            if item["passed"]
        )

        failed = (
            total - passed
        )

        return {
            "total_tests": total,
            "passed": passed,
            "failed": failed
        }