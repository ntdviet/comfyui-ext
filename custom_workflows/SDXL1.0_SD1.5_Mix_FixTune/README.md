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

Models + LORAS used for my examples:
- RevAnimated: https://civitai.com/models/119330?modelVersionId=129614
- AbsoluteReality: https://civitai.com/models/81458?modelVersionId=132760
- Vietnamese long dress Aodai: https://civitai.com/models/112187?modelVersionId=121093
- Better Hands: https://civitai.com/models/112187?modelVersionId=121093
- Add Detail: https://civitai.com/models/112187?modelVersionId=121093

### Installation
Load "SDXL+1.5_FixTune.json" into ComfyUI client

### Observations
In most cases, the fixing and tuning sampler is delivering improved pictures, with acceptable result for fixing faces and hands
![D2_Riding_Example](https://github.com/ntdviet/comfyui-ext/assets/54492570/7d651fc4-0f47-4c97-9fed-adeb716d3151)

With a good LORA, swapping clothes works flawless. The Hand LORA however can not turn an alien hand into human's. It stays alien, but a nicely drawn one
![D1_heavy_damaged_Hands](https://github.com/ntdviet/comfyui-ext/assets/54492570/40505467-50c8-4464-bf59-61d34115f6da)

This one is a classic example of steady improvements after each resampling. HiRes Fix is only involved in 2nd image
![FantasyDreamy_Example](https://github.com/ntdviet/comfyui-ext/assets/54492570/1c2e78e2-0daa-4110-96fd-837e1f575830)

Some images already reach a nice quality (extreme sharp with fine details) after 2nd resampling, can't get much better after that. This is probably due to the prompt yielding a near exact copy of the training image
![FixingSampler_better_result](https://github.com/ntdviet/comfyui-ext/assets/54492570/a9c7be70-5d75-4832-ba46-feb57507f7b8)

By the way, don't do Latent Upscale. Though it's faster than Image Upscale, it grossly destroys image quality
![Upscaling_Method_Comparison](https://github.com/ntdviet/comfyui-ext/assets/54492570/5089ab64-a50f-420f-b591-80b2d1d0f9c1)

After series of Sampling, this is how I find out my favourite settings for the Refiner, which is included in the workflow JSON
![RefiningSamplers(1)](https://github.com/ntdviet/comfyui-ext/assets/54492570/602d3e03-96a6-4926-9dd6-d9beb8400e1e)

Some teasers, all images not yet ultimate SD upscaled:
![ComfyUI_temp_plxbj_00014_](https://github.com/ntdviet/comfyui-ext/assets/54492570/94489eb6-7380-4750-95d8-0309ec304551)
![ComfyUI_temp_cvhrv_00004_](https://github.com/ntdviet/comfyui-ext/assets/54492570/9835bb06-2475-42c0-b6ab-8dae32e4f9bc)
![ComfyUI_temp_qlote_00002_](https://github.com/ntdviet/comfyui-ext/assets/54492570/9faaa90d-5112-4695-90fc-adf0e6ac5ff4)
![ComfyUI_temp_sipsc_00010_](https://github.com/ntdviet/comfyui-ext/assets/54492570/c56090e7-fb19-4615-9318-bde85851e7ad)
![ComfyUI_temp_krqxm_00005](https://github.com/ntdviet/comfyui-ext/assets/54492570/b877b2c9-121d-4507-89e0-ca080df4ebcb)
![ComfyUI_temp_bcijy_00002](https://github.com/ntdviet/comfyui-ext/assets/54492570/bbf49cc0-4bf5-498b-a28f-8442ef8877d1)

