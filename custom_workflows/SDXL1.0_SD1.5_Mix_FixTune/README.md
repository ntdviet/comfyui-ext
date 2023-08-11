## BRIEF

This ComfyUI workflow is an experiment to blend SD1.5 visual styles (determined by custom checkpoints and LORAs) and precision into SDXL1.0's fantastic compositions.
In the same rendering pipeline, artifacts and faulty image creation from SDXL1.0 base render shall automatically be removed as much as possible without the need for manual inpainting.
![ảnh](https://github.com/ntdviet/comfyui-ext/assets/54492570/7da20f9d-255b-4a6e-9af9-4f3f2241f936)

![ảnh](https://github.com/ntdviet/comfyui-ext/assets/54492570/f2b1c7ae-5c37-462f-9147-e39c5c55db59)

### Prerequisites
Custom nodes:
-	ComfyUI_Comfyroll_CustomNodes: <a>https://github.com/RockOfFire/ComfyUI_Comfyroll_CustomNodes</a>
-	WAS-node-suite-comfyui: <a>https://github.com/WASasquatch/was-node-suite-comfyui</a>
- gcLatentTunnel: https://github.com/ntdviet/comfyui-ext/tree/main/custom_nodes/gcLatentTunnel
  
Models + LORAS I was using for my examples:
- RevAnimated: https://civitai.com/models/119330?modelVersionId=129614
- AbsoluteReality: https://civitai.com/models/81458?modelVersionId=132760
- Vietnamese long dress Aodai: https://civitai.com/models/112187?modelVersionId=121093
- Better Hands: https://civitai.com/models/112187?modelVersionId=121093
- Add Detail: https://civitai.com/models/112187?modelVersionId=121093


### Installation
Load "SDXL+1.5_FixTune.json" into ComfyUI client

