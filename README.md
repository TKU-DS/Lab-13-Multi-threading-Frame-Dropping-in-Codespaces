# Lab 12: Object Detection & The NMS Latency Tax

## 📌 Overview
In previous labs, we focused on "Inference" speed. However, in Object Detection, the story doesn't end when the model finishes its forward pass. [cite_start]The system must then run **Non-Maximum Suppression (NMS)** to filter out thousands of redundant candidate boxes.

In a CPU-bound environment like GitHub Codespaces, NMS can become a significant bottleneck. [cite_start]This lab will compare the traditional YOLOv8 (with NMS) against the state-of-the-art YOLOv10 (NMS-Free).

## 🎯 Learning Objectives
1. Profile the end-to-end latency: Pre-process vs. Inference vs. Post-process (NMS).
2. [cite_start]Understand how the `Confidence Threshold` affects NMS computation time.
3. [cite_start]Benchmark the performance gain of YOLOv10's NMS-Free architecture.

## 🛠️ Instructions
1. **Setup**:
   `pip install ultralytics numpy opencv-python`
2. **Execute**:
   Run `python lab12_nms_benchmark.py`.
3. **Analyze**:
   - Observe the `Post-process` time for YOLOv8 as you change the `conf` threshold.
   - Compare it with YOLOv10's post-processing time.

## ✅ Expected Deliverable
Submit a short report with a table showing:
- Model Name
- Confidence Threshold
- Raw Inference Time (ms)
- Post-process (NMS) Time (ms)
- Total FPS
