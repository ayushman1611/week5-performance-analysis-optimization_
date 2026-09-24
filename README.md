# Week 5 – Performance Analysis and Optimization Strategy

## Internship Project
**Internal Communication Platform**

This GitHub project supports the Week 5 Junior Systems Analyst task.

### Important note
All performance values are **simulated academic data** because no production monitoring data was supplied. The numbers demonstrate the analysis method and should not be presented as measurements from a real production system.

## Project contents

- `report/` – final Word report for submission
- `docs/` – 200+ word submission description
- `data/` – simulated baseline and optimization-target datasets
- `analysis/` – Python script for basic calculations
- `diagrams/` – charts and performance architecture diagram

## Metrics
1. P95 response time
2. Throughput
3. CPU utilization
4. Memory utilization
5. Database latency
6. Error rate
7. Cache efficiency and connection utilization as secondary diagnostic metrics

## Optimization strategy
- Database indexing and query optimization
- Redis caching
- Connection-pool tuning
- Pagination and payload reduction
- Background/asynchronous processing
- Horizontal application scaling
- Monitoring, alerting and regression testing

## Reproduce the basic analysis

```bash
pip install pandas
python analysis/analyze_performance.py
```

## Week 5 requirement coverage

The report explicitly covers all 15 task lines shown in the internship portal, from the objective through the final systems-analysis understanding requirement.
