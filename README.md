# Lab 13: Multi-threading & Frame Dropping in Codespaces

## 📌 Overview
In a real-time vision system, the camera (or video decoder) reads frames at 30-100 FPS, but your CPU might only run YOLOv10 at 5-10 FPS. If you process frames sequentially in a simple `while True` loop, your system will accumulate latency (lag) and eventually crash due to Out-Of-Memory (OOM) errors in the GitHub Codespaces environment.

In this lab, you will build a **Producer-Consumer** architecture using Python's `threading` module and implement a **Frame Dropping** strategy using a bounded queue (`maxsize=1`) to ensure the system always processes the freshest data.

## 🎯 Learning Objectives
1. Decouple I/O (Video Reading) from Computation (AI Inference) using `threading`.
2. Manage thread-safe data flow between threads using `queue.Queue`.
3. Implement an active **Frame Drop** logic using `queue.get_nowait()` to prevent memory overflow and latency drift.

## 🛠️ Environment Setup
Since GitHub Codespaces is a "headless" environment (no physical monitor), we must use the headless version of OpenCV. Install the required packages:
```bash
pip install ultralytics opencv-python-headless numpy
```

## 🚀 Lab Tasks
Open `lab13_threaded_pipeline.py` and complete the following TODOs:

1. **TODO 1**: Initialize a thread-safe `queue.Queue` with `maxsize=1`.
2. **TODO 2**: In the **Producer Thread**, implement the "Drop-and-Replace" logic:
   - Attempt to put a new frame into the queue.
   - If the queue is full, catch the exception, discard the stale frame, and insert the new one.
3. **TODO 3**: In the **Consumer Thread**, retrieve the latest frame from the queue with a timeout and run the YOLOv10 inference.

## ✅ Expected Deliverable
- A functional Python script that runs without freezing or crashing.
- A screenshot of your Terminal showing:
  - The **Producer** reading frames rapidly.
  - The **Consumer** processing frames at a stable AI FPS.
  - No increasing lag in detection results.
