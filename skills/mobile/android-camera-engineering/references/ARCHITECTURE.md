# Reference Architecture

Recommended separation for Android camera apps:

UI / Camera Screen
→ Camera Controller
→ CameraX / Camera2 Interop
→ Capability Detection
→ Capture Coordinator
→ Computational Photography Pipeline
→ Optional AI Router
→ Timestamp / Overlay Renderer (when used)
→ Encoder
→ MediaStore

Keep Preview, Capture, Image Analysis, AI, Overlay and Storage pipelines independently testable. Prefer CameraX for lifecycle-friendly common operations and Camera2/Interop only when advanced hardware control provides measurable value.
