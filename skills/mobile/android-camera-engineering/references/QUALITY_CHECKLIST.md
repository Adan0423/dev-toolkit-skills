# Camera Image Quality Checklist

## Capture
- Verify autofocus reliability and capture latency.
- Validate exposure, AE/AWB stability, orientation, zoom and lens switching.
- Test daylight, indoor, backlight, night, motion, faces, vegetation, text and artificial lights.

## Processing
- Check HDR alignment and ghosting.
- Check denoise/detail balance.
- Detect halos, oversharpening, clipping, banding and color shifts.
- Preserve natural skin tones and textures.

## AI
- AI enhancement must be optional: OFF / AUTO / ON where appropriate.
- Prefer on-device inference.
- Benchmark latency, RAM, thermal impact and battery use.
- Avoid hallucinated detail and unnecessary model execution.

## Performance
- Keep preview and shutter responsive.
- Avoid heavy work on the main thread.
- Reuse buffers and close ImageProxy correctly.
- Adapt processing to device capability and thermal state.
