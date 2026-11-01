---
name: ultralytics-yolo
title: Ultralytics YOLO
url: "https://github.com/ultralytics/ultralytics"
category: framework
summary: "Unified real-time computer vision framework — object detection, instance/semantic segmentation, classification, pose estimation, oriented bounding boxes, and tracking; YOLO26 (latest) is NMS-free, DFL-free, 43% faster CPU inference than YOLO11; five model sizes (Nano to X-Large); CLI + Python API; export to ONNX/TensorRT/CoreML/TFLite; AGPL-3.0 (Enterprise license available)"
tags: [computer-vision, object-detection, segmentation, pose-estimation, classification, tracking, real-time, edge-inference, yolo, deep-learning, python]
reviewed: 2026-10-06
acquired: 2026-10-06
overlaps: []
license: AGPL-3.0
security_flags: []
source: unknown
---

## What it does

Ultralytics YOLO is a unified real-time vision framework covering detection, segmentation, classification, pose estimation, oriented bounding boxes, and object tracking. The current generation (YOLO26, Jan 2026) is NMS-free and DFL-free, with up to 43% faster CPU inference than YOLO11.

Five model sizes: Nano (2.6M params), Small, Medium, Large (24.8M params, mAP 55.0 at 640px), X-Large. Tasks: object detection, instance segmentation, semantic segmentation, image classification, pose estimation, oriented object detection.

Key YOLO26 improvements:
- **End-to-end NMS-free inference** via dual-head formulation (`nms=False` for NMS-free head)
- **DFL-free box regression** — simpler detection head, easier export
- **Small-Target-Aware Label Assignment (STAL)** for better small-object performance
- **MuSGD + Progressive Loss** training improvements

## Mechanical details

Install: `pip install ultralytics`. CLI: `yolo predict model=yolo26l.pt source=image.jpg`. Python: `from ultralytics import YOLO; model = YOLO("yolo26l.pt"); results = model.predict(source)`.

YOLO26L benchmarks (640px): mAP50-95 55.0, CPU ONNX 286ms, T4 TensorRT 6.2ms, 24.8M params, 86.8B FLOPs.

Export targets: ONNX, TensorRT, CoreML, TFLite, OpenVINO, NCNN, Edge TPU, Paddle. Supports training on custom datasets via YAML config.

Practitioner note: one frame with yolo26l.pt produced 5,040 prediction cells → 92 boxes above 0.25 confidence → 12 bird detections after NMS (IoU 0.7). With `nms=False` (NMS-free head), same frame returned 9 detections.

## Security

AGPL-3.0 for open-source use; Ultralytics Enterprise License for commercial deployment without AGPL obligations. No telemetry in inference path. Model weights downloaded from Ultralytics servers on first use.