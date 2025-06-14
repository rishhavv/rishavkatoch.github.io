---
title: "Distributed Task Scheduler"
date: 2024-03-20
description: "A Golang-based distributed task scheduling framework with support for multiple scheduling algorithms"
technologies: [Go, Docker, Prometheus, Azure]
github: "https://github.com/rishhavv/distributed-task-scheduler"
demo: "https://zenodo.org/records/14633463"
---

# Distributed Task Scheduler

A comprehensive distributed task scheduling framework implemented in Go, featuring multiple scheduling algorithms and extensive performance metrics.

## Features

- Multiple scheduling algorithms (Round-Robin, FCFS, Least-Loaded)
- Prometheus-based metrics collection
- Docker containerization
- Azure cloud deployment
- Comprehensive workload testing framework

## Technical Details

The system is built using:

- Go for high-performance task scheduling
- Docker for containerization
- Prometheus for metrics collection
- Azure VMs for deployment

## Results

The framework has been tested with various workloads:

- CPU-intensive tasks
- I/O-bound operations
- Memory-intensive processes

## Getting Started

```bash
# Clone the repository
git clone https://github.com/rishhavv/distributed-task-scheduler

# Build and run
cd distributed-task-scheduler
go build
./distributed-task-scheduler
```

## Future Work

- Add more scheduling algorithms
- Implement dynamic resource allocation
- Add support for more cloud providers
