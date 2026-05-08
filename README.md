# Lab 13: Multi-threading & Frame Dropping in Codespaces

## 📌 Overview
In a real-time vision system, the camera (or video decoder) reads frames at 30-100 FPS, but your CPU might only run YOLOv10 at 5-10 FPS. If you process frames sequentially in a `while True` loop, your system will accumulate latency and eventually crash due to Out-Of-Memory (OOM) in GitHub Codespaces.

In this lab, you will build a **Producer-Consumer** architecture using Python's `threading` module and implement a **Frame Dropping** strategy using a bounded queue (`maxsize=1`).

## 🎯 Learning Objectives
1. Decouple I/O (Video Reading) from Computation (AI Inference) using `threading`.
2. Manage thread-safe data flow using `queue.Queue`.
3. Implement `queue.get_nowait()` to actively drop stale frames.

## 🛠️ Environment Setup
Because GitHub Codespaces is a "headless" environment (no monitor), we must use the headless version of OpenCV:
```bash
pip install ultralytics opencv-python-headless numpy
