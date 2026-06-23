from backend.app.evaluation.regression_tester import (
    RegressionTester
)

tester = RegressionTester()

tester.run_test(
    question="What is Redis?",
    expected="Redis is an in-memory database",
    actual="Redis is an in-memory database"
)

tester.run_test(
    question="What is PostgreSQL?",
    expected="PostgreSQL is relational",
    actual="PostgreSQL is relational"
)

tester.run_test(
    question="What is ChromaDB?",
    expected="Vector database",
    actual="Document database"
)

print(
    tester.summary()
)