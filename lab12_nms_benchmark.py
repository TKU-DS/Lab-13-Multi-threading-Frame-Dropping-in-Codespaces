import cv2
import time
from ultralytics import YOLO
import urllib.request
import os

# =================================================================
# Course: Data Engineering (CSIE, Tamkang University)
# Lab 12: Object Detection Post-processing Analysis
# =================================================================

def download_test_image():
    url = "https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/assets/bus.jpg"
    img_path = "test.jpg"
    if not os.path.exists(img_path):
        print("[*] Downloading test image...")
        urllib.request.urlretrieve(url, img_path)
    return img_path

def benchmark_model(model_variant, img_path, conf_threshold=0.25):
    print(f"\n--- Benchmarking {model_variant} (Conf: {conf_threshold}) ---")
    
    # Load model (Auto-downloads .pt file)
    model = YOLO(model_variant)
    
    # Warmup
    model(img_path, verbose=False)
    
    # Run Inference
    results = model(img_path, conf=conf_threshold, verbose=False)
    
    # Extract timing metadata (in milliseconds)
    # Ultralytics results.speed dictionary contains:
    # 'preprocess', 'inference', 'postprocess'
    speed = results[0].speed
    
    print(f"    - Pre-process:  {speed['preprocess']:.2f} ms")
    print(f"    - Raw Inference: {speed['inference']:.2f} ms")
    print(f"    - Post-process (NMS): {speed['postprocess']:.2f} ms")
    
    total_time = sum(speed.values())
    print(f"    - Total Pipeline: {total_time:.2f} ms (approx. {1000/total_time:.1f} FPS)")
    
    return speed

if __name__ == "__main__":
    test_img = download_test_image()
    
    # ---------------------------------------------------------
    # PART 1: The NMS Tax in YOLOv8
    # Observe how lowering the threshold increases NMS time 
    # because more boxes enter the NMS loop.
    # ---------------------------------------------------------
    print("\n[PART 1] Investigating YOLOv8 NMS Bottleneck")
    benchmark_model("yolov8n.pt", test_img, conf_threshold=0.01) # Many boxes
    benchmark_model("yolov8n.pt", test_img, conf_threshold=0.5)  # Few boxes
    
    # ---------------------------------------------------------
    # PART 2: The NMS-Free Revolution (YOLOv10)
    # Observe how YOLOv10 eliminates the post-processing gap.
    # ---------------------------------------------------------
    print("\n[PART 2] Benchmarking YOLOv10 (NMS-Free)")
    # Note: YOLOv10-Nano is extremely efficient on CPU
    benchmark_model("yolov10n.pt", test_img, conf_threshold=0.25)
