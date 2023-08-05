## PURPOSE

This node flushes the GPU cache and empty cuda interprocess memory.
It's helpfull for low memory environment such as the free Google Colab, especially when the workflow VAE decode latents of the size above 1500x1500.

### Prerequisites

None

### Installation

Just copy the .py into your .../ComfyUI/custom_nodes folder and restart the UI.

### Example

Put it anywhere in the line of latents where you suspect an outburst use of memory (eg. after sampling or after decoding).
![ảnh](https://github.com/ntdviet/comfyui-ext/assets/54492570/c824b084-d5bf-4408-8575-7f2b362f7682)
